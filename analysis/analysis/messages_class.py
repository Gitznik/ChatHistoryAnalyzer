from dataclasses import dataclass

@dataclass
class Message:
    """Class for keeping a structured message."""
    message_sent_time: datetime.datetime
    author: str
    message: str