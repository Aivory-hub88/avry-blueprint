"""
JSON Assembly Service
Assembles blueprint JSON structures from components
"""

import logging
from typing import Dict, List, Optional
import json

logger = logging.getLogger(__name__)


class JSONAssemblyService:
    """
    Service for assembling and managing blueprint JSON structures
    """

    @staticmethod
    async def assemble_blueprint(
        snapshot_data: Dict,
        ai_analysis: Dict,
        system_info: Dict
    ) -> Dict:
        """
        Assemble complete blueprint JSON from components
        
        Args:
            snapshot_data: Snapshot data from diagnostic
            ai_analysis: AI-generated analysis
            system_info: System information
            
        Returns:
            Complete blueprint JSON structure
        """
        try:
            logger.info("Assembling blueprint JSON")
            
            blueprint = {
                "version": "1.0.0",
                "created_at": None,
                "snapshot_data": snapshot_data,
                "ai_analysis": ai_analysis,
                "system_info": system_info,
                "sections": []
            }
            
            return blueprint
        except Exception as e:
            logger.error(f"Error assembling blueprint: {e}")
            raise

    @staticmethod
    async def validate_blueprint_structure(blueprint: Dict) -> bool:
        """
        Validate blueprint JSON structure
        
        Args:
            blueprint: Blueprint JSON to validate
            
        Returns:
            True if valid, raises exception if invalid
        """
        try:
            required_fields = ["version", "snapshot_data", "ai_analysis"]
            for field in required_fields:
                if field not in blueprint:
                    raise ValueError(f"Missing required field: {field}")
            
            return True
        except Exception as e:
            logger.error(f"Blueprint validation failed: {e}")
            raise

    @staticmethod
    def merge_blueprints(blueprints: List[Dict]) -> Dict:
        """
        Merge multiple blueprint structures
        
        Args:
            blueprints: List of blueprint JSONs to merge
            
        Returns:
            Merged blueprint
        """
        try:
            if not blueprints:
                raise ValueError("No blueprints to merge")
            
            merged = blueprints[0].copy()
            for blueprint in blueprints[1:]:
                # Merge sections and analysis
                if "sections" in blueprint:
                    merged.setdefault("sections", []).extend(blueprint["sections"])
            
            return merged
        except Exception as e:
            logger.error(f"Error merging blueprints: {e}")
            raise
