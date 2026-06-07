"""RabbitMQ Event Consumer for Blueprint Service (Phase 2)"""

import os
import pika
import json
import logging
import threading
from typing import Callable, Dict, Any

logger = logging.getLogger(__name__)

_event_handlers: Dict[str, Callable] = {}


def register_handler(event_type: str, handler: Callable):
    _event_handlers[event_type] = handler
    logger.info(f"Registered handler for {event_type}")


def on_user_created(event):
    try:
        logger.info(f"[Blueprint] User created: {event.get('user_id')}")
    except Exception as e:
        logger.error(f"Error: {e}")


def on_diagnostics_completed(event):
    try:
        logger.info(f"[Blueprint] Diagnostics completed: {event.get('diagnostic_id')}")
    except Exception as e:
        logger.error(f"Error: {e}")


register_handler("user.created", on_user_created)
register_handler("diagnostics.completed", on_diagnostics_completed)


def start_consumer():
    try:
        connection = pika.BlockingConnection(
            pika.URLParameters(os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/"))
        )
        channel = connection.channel()
        logger.info("[Blueprint Consumer] Connected")

        channel.exchange_declare(exchange="user.events", exchange_type="topic", durable=True)
        channel.exchange_declare(exchange="diagnostics.events", exchange_type="topic", durable=True)

        channel.queue_declare(queue="blueprint_user_events", durable=True)
        channel.queue_declare(queue="blueprint_diagnostics_events", durable=True)

        channel.queue_bind(exchange="user.events", queue="blueprint_user_events", routing_key="user.*")
        channel.queue_bind(exchange="diagnostics.events", queue="blueprint_diagnostics_events", routing_key="diagnostics.*")

        def on_message(ch, method, properties, body):
            try:
                event = json.loads(body)
                event_type = event.get("event_type")
                if event_type in _event_handlers:
                    _event_handlers[event_type](event.get("data", {}))
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                logger.error(f"Error: {e}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

        channel.basic_consume(queue="blueprint_user_events", on_message_callback=on_message, auto_ack=False)
        channel.basic_consume(queue="blueprint_diagnostics_events", on_message_callback=on_message, auto_ack=False)
        channel.start_consuming()
    except Exception as e:
        logger.error(f"Consumer error: {e}")
        raise


def start_consumer_thread():
    thread = threading.Thread(target=start_consumer, daemon=True)
    thread.start()
    return thread
