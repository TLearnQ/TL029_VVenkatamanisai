import logging
import json

logging.basicConfig(filename="parse.log", level=logging.INFO)

def log_event(event, data):
    logging.info(json.dumps({"event": event, "data": data}))