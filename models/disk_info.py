from dataclasses import dataclass

@dataclass
class DiskInfo:
    usage: float
    total: float
    free: float
    read_speed: float
    write_speed: float