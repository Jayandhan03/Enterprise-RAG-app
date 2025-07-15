# logger.py
import logging
import os

# Ensure the logs/ directory exists
os.makedirs("logs", exist_ok=True)

# Create a custom logger
logger = logging.getLogger("RAGBot")
logger.setLevel(logging.DEBUG)  # Capture everything, control output via handlers

# Format for logs
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Only show info+ on console
console_handler.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler("logs/rag_bot.log")
file_handler.setLevel(logging.DEBUG)  # Save everything to file
file_handler.setFormatter(formatter)

# Avoid duplicate logs if multiple imports
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
