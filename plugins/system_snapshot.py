import psutil

def snapshot(disk_path="C:/"):
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage(disk_path)

    mem_gb_used = mem.used / (1024 ** 3)
    mem_gb_total = mem.total / (1024 ** 3)
    disk_gb_free = disk.free / (1024 ** 3)

    return (
        f"CPU {cpu:.0f}% | "
        f"RAM {mem.percent:.0f}% ({mem_gb_used:.1f}/{mem_gb_total:.1f} GB) | "
        f"Disk free {disk_gb_free:.1f} GB"
    )

def battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        return "No battery detected (desktop, or not supported on this device)."
    state = "charging" if battery.power_plugged else "on battery"
    return f"Battery: {battery.percent:.0f}% ({state})"