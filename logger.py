import logging

logging.basicConfig(
    filename="toolkit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    logging.info(message)