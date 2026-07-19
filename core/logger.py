import logging
import os
from datetime import datetime

# Ensure outputs directory exists
os.makedirs("outputs", exist_ok=True)

# Configure the root logger
logger = logging.getLogger("AgenticPlatform")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# File handler
file_handler = logging.FileHandler("outputs/execution_trace.log", mode='a')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add handlers
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def get_logger(module_name: str) -> logging.Logger:
    """Returns a configured logger for a specific module."""
    return logger.getChild(module_name)
