from database.queue_db.database import create_db
from model.queue_db import queue_in, queue_out, rejected


def create_queue_db() -> None:
    create_db()
