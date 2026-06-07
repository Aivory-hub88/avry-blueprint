"""
Metadata Embedding Service
Embeds metadata and tags in blueprint JSON
"""

import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class MetadataEmbeddingService:
    """
    Service for embedding metadata in blueprints
    """

    @staticmethod
    async def embed_metadata(blueprint: Dict, metadata: Dict) -> Dict:
        """
        Embed metadata in blueprint JSON
        
        Args:
            blueprint: Blueprint JSON structure
            metadata: Metadata to embed
            
        Returns:
            Blueprint with embedded metadata
        """
        try:
            logger.info("Embedding metadata in blueprint")
            
            blueprint["metadata"] = {
                "created_by": metadata.get("created_by", "system"),
                "version": metadata.get("version", "1.0.0"),
                "tags": metadata.get("tags", []),
                "keywords": metadata.get("keywords", []),
                "author": metadata.get("author", "Aivory AI"),
                "license": metadata.get("license", "proprietary")
            }
            
            return blueprint
        except Exception as e:
            logger.error(f"Error embedding metadata: {e}")
            raise

    @staticmethod
    async def add_tags(blueprint: Dict, tags: List[str]) -> Dict:
        """
        Add tags to blueprint
        
        Args:
            blueprint: Blueprint JSON structure
            tags: Tags to add
            
        Returns:
            Blueprint with tags
        """
        try:
            logger.info(f"Adding tags: {tags}")
            
            if "metadata" not in blueprint:
                blueprint["metadata"] = {}
            
            blueprint["metadata"]["tags"] = tags
            
            return blueprint
        except Exception as e:
            logger.error(f"Error adding tags: {e}")
            raise

    @staticmethod
    async def extract_keywords(content: str) -> List[str]:
        """
        Extract keywords from blueprint content
        
        Args:
            content: Blueprint content
            
        Returns:
            List of extracted keywords
        """
        try:
            logger.info("Extracting keywords from blueprint")
            
            # Simple keyword extraction
            keywords = []
            common_terms = ["AI", "automation", "integration", "system", "process"]
            
            for term in common_terms:
                if term.lower() in content.lower():
                    keywords.append(term)
            
            return keywords
        except Exception as e:
            logger.error(f"Error extracting keywords: {e}")
            raise
