import psutil
from models.cpu_info import CPUInfo
from models.ram_info import RAMInfo
from models.disk_info import DiskInfo

class SystemMonitor:
    def __init__(self):
        # "Heats" the CPU reading to avoid returning 0 at the first usage
        psutil.cpu_percent(interval=None)

        disk_io = psutil.disk_io_counters()

        self.last_read_bytes = disk_io.read_bytes
        self.last_write_bytes = disk_io.write_bytes

        network = psutil.net_io_counters()

        self.last_sent_bytes = network.bytes_sent
        self.last_received_bytes = network.bytes_recv

    def get_cpu_info(self) -> CPUInfo:
        usage = psutil.cpu_percent(interval=None)

        freq = psutil.cpu_freq()

        if freq and freq.current :
            frequency = f"{freq.current / 1000:.2f} GHz"
        else:
            frequency = "N/A"

        temperature = self._get_cpu_temperature()

        cores = psutil.cpu_count(logical=False) or 0
        threads = psutil.cpu_count(logical=True) or 0

        return CPUInfo(
            usage=usage,
            temperature=temperature,
            frequency=frequency,
            cores=cores,
            threads=threads
        )
    
    def _get_cpu_temperature(self) -> str :
        try:
            temps = psutil.sensors_temperatures()
        except (AttributeError, NotImplementedError):
            return "N/A"
        
        if not temps:
            return "N/A"
        
        for sensors_list in temps.values():
            for sensor in sensors_list:
                current = getattr(sensor, "current", None)
                if current is not None:
                    return f"{current:.1f} ºC"
                
        return "N/A"
    
    def get_ram_info(self) -> RAMInfo :
        memory = psutil.virtual_memory()

        gb = 1024 ** 3

        total = memory.total / gb
        used = memory.used / gb
        available = memory.available / gb
        percent = memory.percent
        
        cached = getattr(memory, "cached", None)

        if cached is not None:
            cached = cached / gb
        else:
            cached = 0.0

        return RAMInfo(
            total=total,
            used=used,
            available=available,
            percent=percent,
            cached=cached
        )
    
    def get_disk_info(self) -> DiskInfo :
        disk = psutil.disk_usage("/")

        gb = 1024 ** 3

        total = disk.total / gb
        free = disk.free / gb
        usage = disk.percent

        disk_io = psutil.disk_io_counters()

        current_read = disk_io.read_bytes
        current_write = disk_io.write_bytes

        delta_read = current_read - self.last_read_bytes
        delta_write = current_write - self.last_write_bytes

        seconds = 0.25
        mb = 1024 ** 2

        read_speed = (delta_read / seconds) / mb
        write_speed = (delta_write / seconds) / mb

        self.last_read_bytes = current_read
        self.last_write_bytes = current_write

        return DiskInfo(
            usage=usage,
            total=total,
            free=free,
            read_speed=read_speed,
            write_speed=write_speed
        )