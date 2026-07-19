import json
import os
from typing import Dict, Any
from core.logger import get_logger

logger = get_logger("Memory")

class Memory:
    def __init__(self, memory_file: str = "outputs/memory.json"):
        self.memory_file = memory_file
        self.state: Dict[str, Any] = {
            "business_context": None,
            "synthetic_source_pack": None,
            "business_analysis": None,
            "marketing_strategy": None,
            "weekly_plan": None,
            "generated_assets": {
                "posts": [],
                "videos": []
            },
            "status": "initialized"
        }
        self._load()

    def _load(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r") as f:
                    self.state = json.load(f)
            except json.JSONDecodeError:
                logger.warning("Could not load memory, starting fresh.")
        else:
            self._save()

    def _save(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.state, f, indent=4)

    def set(self, key: str, value: Any):
        self.state[key] = value
        self._save()
        logger.debug(f"Memory updated for key: {key}")

    def get(self, key: str) -> Any:
        return self.state.get(key)
        
    def add_asset(self, asset_type: str, asset_data: Any):
        if asset_type in self.state["generated_assets"]:
            self.state["generated_assets"][asset_type].append(asset_data)
            self._save()
            logger.debug(f"Asset added to memory: {asset_type}")

memory = Memory()
