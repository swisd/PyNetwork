import psutil
from time import perf_counter, perf_counter_ns
from printmods import Fore, fprint_s, fprint

def timedata(func):
    """Times any function"""

    def wrapper(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        recv0 = psutil.net_io_counters().bytes_recv
        sent0 = psutil.net_io_counters().bytes_sent
        start_time = perf_counter_ns()

        func(*args, **kwargs)

        end_time = perf_counter_ns()
        total_time = round((end_time - start_time) / 1000000, 3)
        recv1 = psutil.net_io_counters().bytes_recv
        sent1 = psutil.net_io_counters().bytes_sent
        recv = recv1 - recv0
        sent = sent1 - sent0
        total = recv + sent

        kb_recv: float = recv / 1024
        kb_sent: float = sent / 1024
        kb_total: float = total / 1024
        fprint(f'{total_time} ms | {kb_recv:.3f}/{kb_sent:.3f}/{kb_total:.3f} KB R/S/T | {psutil.cpu_percent(total_time / 1000)} %CPU', 'INFO', Fore.GREEN)
        if total_time > 30000:
            fprint("Server timed out.", "ERROR", Fore.RED)
        print('\n')

    return wrapper


# def deprecated(func):
#     """Makes function deprecated"""

#     def wrapper(*args, **kwargs) -> None:
#         pass

#     return wrapper


# Functions



def connect(ip: str = "127.0.0.1", port: int = 8000) -> list:
    """Connect to IP and Port"""
    connection: list = [ip, port]
    return connection


def handle(clientIP: object, serverIP: str = '127.0.0.1', header: object = None, limit: object = None, key: object = None) -> object:
    connection = connect()
    fprint(f"connnected {serverIP}, {clientIP} on {connection}", "HANDLER", Fore.YELLOW)
    fprint(f"Handling request @{clientIP}", "HANDLER", Fore.YELLOW)
    return connection, limit, header