"""Python 3 loopback server"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep, perf_counter_ns, strftime, localtime, time

import psutil
from socket import gethostname, gethostbyname
import http.cookies
import random
import cgi
from colorama import Fore, Back
from deprecated import deprecated
from functools import cache
from progressbar_ import bar
from tqdm import tqdm

# Variables
exception_curr: str = ''
req_s: int = 0
reql: list = []
clients: list = []
idx: int = 0
for file in ("C:/Network/f/"):
    idx += 1
file_to_open: str = ''
verifiedADDR: str = '127.0.0.1, '
serverVerifiedAddr: str = '127.0.0.1'
RLHostName: str = gethostname()
RLHostIPBaseAddr: str = gethostbyname(RLHostName)
hostName: str = "localhost"
ip_addr: str = "127.0.0.1"
serverPort: int = 8000
chc: list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
response: int = 200
R_LIMIT: int = 10000

seperateIntefaceIP: list = []

DDoSAttackPreventionBanIPList: list = []

CLI_REQs: list[list] = [["0.0.0.0", 0]]

MODS: list = [
    "-s",
    "-d",
    "-v",
    "-t",
    "-m",
    "-r"
]

TT_IDENTIFIER: str = "IDENTIFIER"

MOD_KEYWORDS: list = [
    "system",
    "data",
    "variable",
    "time",
    "maintenance",
    "request"
]

KEYWORDS: list = []


# Decorators
def timedata(func):
    """Times any function"""

    def wrapper(*args, **kwargs):
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

        KBrecv: float = recv / 1024
        KBsent: float = sent / 1024
        KBtotal: float = total / 1024

        fprint(f'{total_time} ms | {KBrecv:.3f}/{KBsent:.3f}/{KBtotal:.3f} KB R/S/T | {psutil.cpu_percent(total_time / 1000)} %CPU', 'INFO', Fore.GREEN)
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

@cache
def fprint(text, aux, col) -> object:
    """Print using color"""
    print((f'{col}[{aux}] {text}{Fore.WHITE}' if aux != '' else f"{col}{text}{Fore.WHITE}"))


@cache
def fprint_s(text, aux, stat):
    """Print using status"""
    if 100 <= stat <= 299:
        col = Fore.GREEN
    elif 300 <= stat <= 399:
        col = Fore.YELLOW
    elif 400 <= stat <= 599:
        col = Fore.RED

    print((f'{col}[{aux}] {text}{Fore.WHITE}' if aux != '' else f"{col}{text}{Fore.WHITE}"))


@deprecated
def connect(ip: str = "127.0.0.1", port: int = 8000) -> object:
    connection: list = [ip, port]
    return connection


# Server
# @cache
@timedata
class LoopbackServer(BaseHTTPRequestHandler):
    global file_to_open, verifiedADDR, req_s, CLI_REQs, exception_curr

    def do_GET(self):

        global req_s, response, verifiedADDR, CLI_REQs, exception_curr
        req_s += 1

        # GET cmd

        response = 200

        fprint(f"GET request {self.path}", 'SERVER', Fore.CYAN)
        file_to_open: str = '/'
        # CLI request tracking
        i = 0
        for idx, (ip, reqs) in enumerate(CLI_REQs):

            if not CLI_REQs[idx][0] == self.client_address[0]:
                i += 1
                if i == (len(CLI_REQs)):
                    CLI_REQs.append([self.client_address[0], 1])
                    print(f"REQl {CLI_REQs[idx]} +")
                    break

            else:
                print('h', end=' ')
                if CLI_REQs[idx][0] == self.client_address[0]:
                    reqs += 1
                    CLI_REQs[idx][1] = reqs
                    print(f"REQl {CLI_REQs[idx]} A")
                    if CLI_REQs[idx][1] >= R_LIMIT:
                        response = 429
                        fprint(f"Service denied to {self.client_address[0]} due to possible DDoS Attack", "WARNING", Fore.LIGHTRED_EX)
                        DDoSAttackPreventionBanIPList.append(self.client_address[0])

        self.send_response(response)
        fprint_s('HDR', response, response)
        self.send_header("Content-type", "text/html")
        cookie = http.cookies.SimpleCookie()
        cookie['ID'] = str(
            random.choice(chc) +
            random.choice(chc) +
            random.choice(chc) +
            random.choice(chc) +
            random.choice(chc)
        )

        for morsel in cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())

        fprint(f'PATH: {self.path}', 'SERVER', Fore.CYAN)

        if self.path == '/favicon.ico':
            file_des = open("C:/Network/favicon.ico", 'rb')  # as binary
            icon_stream = file_des.read()
            response = 200
            self.send_response(response)
            fprint_s('HDR', response, response)
            self.send_header("Content-type", "image/vnd.microsoft.icon")
            self.end_headers()
            self.wfile.write(icon_stream)

        if self.path == '/server/server_side_interface.html?':
            self.path = '/server/server_side_interface.html'

        if self.path == '/':
            fprint('/ request. - switching to /server/index.html', 'INFO', Fore.GREEN)
            self.path = '/server/index.html'
        elif self.path == '/f/upload':
            fprint('/f/upload request. - switching to /server/upload.html', 'INFO', Fore.GREEN)
            self.path = '/server/upload.html'
        elif self.path == '/f/download':
            fprint('/f/download request. - switching to /server/download.html', 'INFO', Fore.GREEN)
            self.path = '/server/download.html'
        elif self.path == '/db':
            fprint('/db request. - switching to /server/database.html', 'INFO', Fore.GREEN)
            self.path = '/server/database.html'
        elif self.path == '/dbverify':
            fprint('/dbverify request. - switching to /server/database_verification.html', 'INFO', Fore.GREEN)
            self.path = '/server/database_verification.html'

        if not '?' in self.path and not self.path == '/favicon.ico':
            try:
                if '/db' in self.path:
                    fprint(
                        f"Secure Area Access Request from IP {self.client_address[0]}, PORT {self.client_address[1]} - {'VERIFIED' if self.client_address[0] in verifiedADDR else 'UNVERIFIED'}",
                        'WARNING', Fore.YELLOW)
                    if self.client_address[0] in verifiedADDR:
                        fprint(
                            f"Secure Area Access Request from IP {self.client_address[0]}, PORT {self.client_address[1]} - OK", "WARNING", Fore.YELLOW
                        )
                        response = 200
                    else:
                        fprint(
                            f"Secure Area Access Request from IP {self.client_address[0]}, PORT {self.client_address[1]} - DENIED", "WARNING", Fore.YELLOW
                        )
                        response = 401

                if '/server' in self.path and self.path != '/server/index.html':
                    if self.client_address[0] in serverVerifiedAddr:
                        fprint(
                            f"Secure Area Access Request from IP {self.client_address[0]}, PORT {self.client_address[1]} - OK", "WARNING", Fore.YELLOW
                        )
                        response = 200
                    else:
                        fprint(
                            f"Secure Area Access Request from IP {self.client_address[0]}, PORT {self.client_address[1]} - DENIED", "WARNING", Fore.YELLOW
                        )
                        response = 401

                if response == 200:
                    file_to_open = open("C:/Network/" + self.path).read()
                elif self.path == '/server/database_verification.html' and response != 200:
                    file_to_open = open("C:/Network/" + self.path).read()
                else:
                    file_to_open = '<head><style>body{margin:4px;font-family:"OCR A";font-size:"75"}</style></head><body> %s Access Denied </body>' % response

                fprint(f'FTO: C:/Network/{self.path}', "SERVER", Fore.CYAN)

                self.send_response(response)
                fprint_s('HDR', response, response)
                fprint(f"Successfully loaded file {self.path}", 'INFO', Fore.GREEN)

            except Exception(FileExistsError) as e:
                file_to_open = 'File not found'
                response = 404
                self.send_response(response)
                fprint_s('HDR', response, response)
                fprint(f"Requested file '{self.path}' not found. {e}", 'ERROR', Fore.RED)
                fprint(f"Either Server Error or C:/Network{self.path}' unavailable", 'SERVER', Fore.RED)

            fprint(f"SERVER: {str(ip_addr + ':' + str(serverPort))}", 'SERVER', Fore.CYAN)
            fprint('/' + self.path[1:], 'SERVER', Fore.CYAN)
            self.end_headers()

        elif '?' in self.path and not self.path == '/favicon.ico':
            response = 500
            self.send_response(response)
            fprint_s('HDR', response, response)
            self.end_headers()
            self.wfile.write(
                bytes(
                    f'<html><body><h4>{self.path}<h4><p>Exception occurred during processing of request from {self.client_address}</p><p>{exception_curr}</p></body></html>',
                    "utf-8"))
            fprint(f'Exception occurred during processing of request from {self.client_address}', 'ERROR', Fore.RED)

        if self.path.endswith("/db"):
            self.wfile.write(bytes(file_to_open, 'utf-8'))
            fprint(f'WRITE/STR C:/Network/{self.path} TO CLI @ {self.client_address}', 'SERVER', Fore.CYAN)
        unused_a: str = ("\n"
                         "        elif self.path.endswith(\"/dbverify\"):\n"
                         "self.wfile.write(bytes('<head><style>body{margin:4px;font-family:\"OCR A\";}</style></head><body><h1>IP Verification</h1><h3>IP "
                         "Verification"
                         "for database access from %s</h3></form><input type=\"submit\" value=\"VERIFY\"></body>' % str(self.client_address), 'utf-8'))\n"
                         "            fprint(f'WRITE/STR C:/Network/{self.path} TO CLI @ {self.client_address}', 'SERVER', Fore.CYAN) \n"
                         "        ")

        if '/db/' in self.path and not self.path in ('/server/database.html', '/db', '/server/scan/db_scanned.html'):
            self.wfile.write(bytes('<head><style>body{margin:4px;font-family:"OCR A";}</style></head><body><pre><plaintext>%s' % str(file_to_open), 'utf-8'))
            fprint(f'WRITE/STR C:/Network/{self.path} TO CLI @ {self.client_address}', 'SERVER', Fore.CYAN)

        elif '/server/' in self.path and not ((('/server/index.html' in self.path) or ('/server/database_verification.html' in self.path)) or (
                '/server/database.html' in self.path) or self.path == '/server/scan/db_scanned.html' or self.path == '/server/scan/main_scanned.html' or self.path == '/server/server_side_interface.html' or self.path == '/server/download.html' or self.path == '/server/upload.html'):
            self.wfile.write(bytes('<head><style>body{margin:4px;font-family:"OCR A";}</style></head><body><plaintext>%s' % str(file_to_open), 'utf-8'))
            fprint(f'WRITE/STR C:/Network/{self.path} TO CLI @ {self.client_address}', 'SERVER', Fore.CYAN)

        else:
            self.wfile.write(bytes(file_to_open, 'utf-8'))
            fprint(f'WRITE C:/Network/{self.path} TO CLI @ {self.client_address}', 'SERVER', Fore.CYAN)

        fprint_s('HDR', response, response)

    def do_POST(self):
        global req_s, verifiedADDR
        req_s += 1
        fprint(f"POST request {self.path}", 'SERVER', Fore.CYAN)

        if self.path.endswith('/dbverify' or '/server/database_verification.html'):
            ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            pdict['boundary'] = bytes(pdict["boundary"], 'utf-8')
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new = self.client_address[0]
                verifiedADDR += f'{new}, '

        # TODO: Fix upload system so that it is usable

        elif self.path.endswith('/upload'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict["boundary"], 'utf-8')
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_file = fields.get('nwfile')

            self.send_response(301)
            self.send_header("Content-type", "text/html")
            self.send_header('Location', f'/f/{new_file}')
            self.end_headers()

    def do_HEAD(self):
        global req_s
        req_s += 1
        fprint(f"HEAD request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(200, "OK")
        self.send_header("Content-type", "text/html")
        cookie = http.cookies.SimpleCookie()
        cookie['ID'] = str(
            random.choice(chc) +
            random.choice(chc) +
            random.choice(chc) +
            random.choice(chc) +
            random.choice(chc)
        )

        for morsel in cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())
        self.end_headers()

    def do_PUT(self):
        global req_s
        req_s += 1
        fprint(f"PUT request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint("Function Unsupported 'PUT'", 'ERROR', Fore.RED)

    def do_DELETE(self):
        global req_s
        req_s += 1
        fprint(f"DELETE request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint("Function Unsupported 'DELETE'", 'ERROR', Fore.RED)

    def do_CONNECT(self):
        global req_s
        req_s += 1
        fprint(f"CONNECT request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint("Function Unsupported 'CONNECT'", 'ERROR', Fore.RED)

    def do_OPTIONS(self):
        global req_s
        req_s += 1
        fprint(f"OPTIONS request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint("Function Unsupported 'OPTIONS'", 'ERROR', Fore.RED)

    def do_TRACE(self):
        global req_s
        req_s += 1
        fprint(f"TRACE request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        date = strftime("%m-%d-%Y %H:%M:%S", localtime(time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))
        fprint("Function Unsupported 'TRACE'", 'ERROR', Fore.LIGHTRED_EX)

    def do_PATCH(self):
        global req_s
        req_s += 1
        fprint(f"PATCH request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do__s(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint('-s request', 'SERVER', Fore.CYAN)

    def do__d(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint('-d request', 'SERVER', Fore.CYAN)

    def do__v(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint('-v request', 'SERVER', Fore.CYAN)

    def do__t(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint('-t request', 'SERVER', Fore.CYAN)
        date = strftime("%m-%d-%Y %H:%M:%S", localtime(time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

    def do__m(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint('-m request', 'SERVER', Fore.CYAN)

    def do__r(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint('-r request', 'SERVER', Fore.CYAN)

    def do_signon(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_SeperateInterfaceID(self):
        seperateIntefaceIP.append([self.client_address[0], self.path])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        items = list(range(0, 12))
        l = len(items)

        for i in tqdm(range(100), ncols=50):
            sleep(0.025)
        self.end_headers()
        self.wfile.write(bytes(f"ID {[self.client_address[0], self.path]} Approved", "utf-8"))
        fprint(f"SeperateInterfaceID {self.path} @ {self.client_address[0]}", 'SERVER', Fore.CYAN)


if __name__ == "__main__":

    fprint('', '', Back.RESET)
    fprint("Loopback Testing Server - Isolated Run Only", "INFO", Fore.YELLOW)
    fprint("Features of this server are in development and not intended for full use.\nFor more information, visit avrx-ucs.com/py_loopback", "", Fore.YELLOW)
    items = list(range(0, 50))
    l = len(items)

    bar(0, l, prefix='Loading:           ', suffix="Complete", length=25, data=True)
    for i, item in enumerate(items):
        # Do stuff...
        sleep(0.1)
        # Update Progress Bar
        bar(i + 1, l, prefix='Loading:           ', suffix='Complete', length=25, data=True)

    IH: int = 0
    stats = ["i7_1185G7/C0_C1_C2_C3", "i7-1185G7/C4_C5_C6_C7", "NVMe0                ", "RAM0                ", "CS0                ", "Done                "]
    statsI3 = ["i3_7350K/C0", "i3_7350K/C1", "NVMe0            ", "RAM0            ", "CS0            ", "Done            "]

    bar(0, l, prefix='Hardware Processes:', suffix=stats[0], length=25)
    for i, item in enumerate(items):
        # Do stuff...
        suffix: str = stats[round(IH / 10)]
        sleep(0.1)
        # Update Progress Bar
        bar(i + 1, l, prefix='Hardware Processes:', suffix=suffix, length=25)
        IH += 1

    stats = ["Allocating Space            ", "Compiling A            ", "Compiling B            ", "Server Startup Items            ",
             "Initializing            ", "Started            "]
    bar(0, l, prefix='Starting:          ', suffix=stats[0], length=25)

    IH: int = 0

    for i, item in enumerate(items):
        # Do stuff...
        suffix: str = stats[round(IH / 10)]
        sleep(0.1)
        # Update Progress Bar
        bar(i + 1, l, prefix='Starting:          ', suffix=suffix, length=25)
        IH += 1

    webServer: HTTPServer = HTTPServer((hostName, serverPort), LoopbackServer)
    fprint(f"Server started http://{hostName}:{serverPort} @ {ip_addr}", 'SERVER', Fore.CYAN)
    fprint(f"Server started http://{RLHostName}:{serverPort} @ {RLHostIPBaseAddr}", 'SERVER', Fore.CYAN)
    fprint(f'Listening on port {serverPort} ...', 'INFO', Fore.GREEN)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    sleep(0)
    print("Server stopped.")

unused_b: str = ("\n"
                 "        self.send_response(200, \"OK\")\n"
                 "        self.send_header(\"Content-type\", \"text/html\")\n"
                 "        cookie = http.cookies.SimpleCookie()\n"
                 "        cookie['ID'] = str(\n"
                 "            random.choice(chc) + \n"
                 "            random.choice(chc) + \n"
                 "            random.choice(chc) + \n"
                 "            random.choice(chc) + \n"
                 "            random.choice(chc)\n"
                 "            )\n"
                 "\n"
                 "        for morsel in cookie.values():\n"
                 "            self.send_header(\"Set-Cookie\", morsel.OutputString())\n"
                 "        self.end_headers()\n"
                 "        self.wfile.write(bytes(\"<head><title>LoopbackServerA1</title></head>\", \"utf-8\"))\n"
                 "        self.wfile.write(bytes(\"<p>Request: %s</p>\" % self.path, \"utf-8\"))\n"
                 "        self.wfile.write(bytes((\"<p>CLIENT: %s<p>\" % str(self.client_address)), \"utf-8\"))\n"
                 "        self.wfile.write(bytes((\"<p>SERVER: %s<p>\" % str(ip_addr + \":\" + str(serverPort))), \"utf-8\"))\n"
                 "        self.wfile.write(bytes((\"<p>CONNECTION: %s<p>\" % str(self.connection)), \"utf-8\"))\n"
                 "        self.wfile.write(bytes((\"<p>COMMAND: %s<p>\" % str(self.command)), \"utf-8\"))\n"
                 "        self.wfile.write(bytes((\"<p>HEADERS: %s<p>\" % str(self.headers)), \"utf-8\"))\n"
                 "        print(\"CLIENT: \", self.client_address)\n"
                 "        print(\"CONNECTION: \", self.connection)\n"
                 "        print(\"COMMAND: \", self.command)\n"
                 "        print(\"HEADERS: \n\", self.headers)\n")
