import time
import psutil

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    new_recieved = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    mb_new_recieved = new_recieved / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024

    print(f"\r{mb_new_recieved:.3f} MB recv, {mb_new_sent:.3f} MB sent, {mb_new_total:.3f} MB total", end='   ')

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total

    time.sleep(0.1)

