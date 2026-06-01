from dataclasses import dataclass

@dataclass
class CPUInfo:
    usage: float
    temperature: str
    frequency: str
    cores: int
    threads: int