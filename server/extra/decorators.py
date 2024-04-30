from time import sleep, perf_counter
from functools import wraps

def get_time(func):
    """Times any function"""

    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        func(*args, **kwargs)

        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)

        print(f'{total_time} s')
    
    return wrapper

@get_time
def connect(ip: str, ports: list) -> None:
    sleep(1)
    connected = False
    if not connected:
        print('Could not connect to the internet')

if __name__ == '__main__':
    connect('127.0.0.1', [8000, 8080])