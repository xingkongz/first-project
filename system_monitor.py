import psutil
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def format_bytes(size):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024

def main():
    prev_net = psutil.net_io_counters()
    while True:
        clear_screen()

        # CPU
        cpu_percent = psutil.cpu_percent(interval=0.5)
        cpu_count = psutil.cpu_count()

        # Memory
        mem = psutil.virtual_memory()

        # Disk
        disk = psutil.disk_usage('/')

        # Network speed
        net = psutil.net_io_counters()
        upload_speed = net.bytes_sent - prev_net.bytes_sent
        download_speed = net.bytes_recv - prev_net.bytes_recv
        prev_net = net

        print("=== System Monitor CLI ===\n")
        print(f"CPU 使用率: {cpu_percent}% ({cpu_count} 核心)")
        print(f"内存: {mem.percent}% ({format_bytes(mem.used)} / {format_bytes(mem.total)})")
        print(f"磁盘: {disk.percent}% ({format_bytes(disk.used)} / {format_bytes(disk.total)})")
        print(f"上传速度: {format_bytes(upload_speed)}/s")
        print(f"下载速度: {format_bytes(download_speed)}/s")

        time.sleep(1)

if __name__ == "__main__":
    main()
