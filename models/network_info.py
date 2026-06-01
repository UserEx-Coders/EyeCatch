from dataclasses import dataclass

@dataclass
class NetworkInfo:
    sent_speed: float
    received_speed: float

    total_sent: float
    total_received: float