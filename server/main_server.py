# Python 3 loopback server 
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep, perf_counter_ns, strftime, localtime, time
import psutil
from socket import gethostname, gethostbyname
import http.cookies
import random
import os
import cgi
from colorama import Fore, Back
import loopback_ssi
from functools import cache
from deprecated import deprecated



# Variables

req_s = 0
reql = []
clients = []
idx = 0
for file in ("C:/Network/f/"):
    idx += 1
file_to_open = ''
verifiedADDR = '127.0.0.1, '
hostName = gethostname()
ip_addr = gethostbyname(hostName)
RLHostName: str = gethostname()
RLHostIPBaseAddr: str = gethostbyname(RLHostName)
serverPort = 8000
chc = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
response = 200
serverVerifiedAddr: str = '127.0.0.1'

R_LIMIT = 10000

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

        KBrecv = recv / 1024
        KBsent = sent / 1024
        KBtotal = total / 1024

        fprint(f'{total_time} ms | {KBrecv:.3f}/{KBsent:.3f}/{KBtotal:.3f} KB R/S/T | {psutil.cpu_percent(total_time/1000)} %CPU', 'INFO', Fore.GREEN)
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
    print((f'{col}[{aux}] {text}{Fore.WHITE}' if aux != '' else f"{col}{text}{Fore.WHITE}"))

@cache
def fprint_s(text, aux, stat):
    if (stat >= 100 and stat <= 299):
        col = Fore.GREEN
    elif (stat >= 300 and stat <= 399):
        col = Fore.YELLOW
    elif (stat >= 400 and stat <= 599):
        col = Fore.RED

    print((f'{col}[{aux}] {text}{Fore.WHITE}' if aux != '' else f"{col}{text}{Fore.WHITE}"))

@deprecated
def connect(ip: str="127.0.0.1", port: int=8000) -> object:
    connection: list = [ip, port]
    return connection




# Server
@timedata
class LoopbackServer(BaseHTTPRequestHandler):
    global file_to_open, verifiedADDR, req_s, CLI_REQs

    @cache
    def do_GET(self):

        global req_s, response, verifiedADDR, CLI_REQs
        req_s += 1

        # GET cmd

        response = 200

        fprint(f"GET request {self.path}", 'SERVER', Fore.CYAN)
        file_to_open = '/'
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
                if ('/db' in self.path):
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


            except:
                file_to_open = 'File not found'
                response = 404
                self.send_response(response)
                fprint_s('HDR', response, response)
                fprint(f"Requested file '{self.path}' not found", 'ERROR', Fore.RED)
                fprint(f"Either Server Error or C:/Network{self.path}' unavailable", 'SERVER', Fore.RED)

            fprint(("SERVER: %s" % str(ip_addr + ":" + str(serverPort))), 'SERVER', Fore.CYAN)
            fprint('/' + self.path[1:], 'SERVER', Fore.CYAN)
            self.end_headers()

        elif '?' in self.path and not self.path == '/favicon.ico':
            response = 500
            self.send_response(response)
            fprint_s('HDR', response, response)
            self.end_headers()
            self.wfile.write(
                bytes('<html><body><h4>%s<h4><p>Exception occurred during processing of request from %s</p></body></html>' % (self.path, self.client_address),
                      "utf-8"))
            fprint(f'Exception occurred during processing of request from {self.client_address}', 'ERROR', Back.RED)
            fprint('', '', Back.RESET)

        if self.path.endswith("/db"):
            self.wfile.write(bytes(file_to_open, 'utf-8'))
            fprint(f'WRITE/STR C:/Network/{self.path} TO CLI @ {self.client_address}', 'SERVER', Fore.CYAN)
        """
        elif self.path.endswith("/dbverify"):
            self.wfile.write(bytes('<head><style>body{margin:4px;font-family:"OCR A";}</style></head><body><h1>IP Verification</h1><h3>IP Verification for database access from %s</h3></form><input type="submit" value="VERIFY"></body>' % str(self.client_address), 'utf-8'))
            fprint(f'WRITE/STR C:/Network/{self.path} TO CLI @ {self.client_address}', 'SERVER', Fore.CYAN) 
        """

        if '/db/' in self.path and not (self.path == '/server/database.html' or self.path == '/db' or self.path == '/server/scan/db_scanned.html'):
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
        Back.RESET

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
                verifiedADDR += '%s, ' % new

        

        elif self.path.endswith('/upload'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict["boundary"], 'utf-8')
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_file = fields.get('nwfile')

            self.send_response(301)
            self.send_header("Content-type", "text/html")
            self.send_header('Location', '/f/%s' % new_file)
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
        fprint(f"Function Unsupported 'PUT'", 'ERROR', Fore.RED)

    def do_DELETE(self):
        global req_s
        req_s += 1
        fprint(f"DELETE request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f"Function Unsupported 'DELETE'", 'ERROR', Fore.RED)

    def do_CONNECT(self):
        global req_s
        req_s += 1
        fprint(f"CONNECT request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f"Function Unsupported 'CONNECT'", 'ERROR', Fore.RED)

    def do_OPTIONS(self):
        global req_s
        req_s += 1
        fprint(f"OPTIONS request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f"Function Unsupported 'OPTIONS'", 'ERROR', Fore.RED)

    def do_TRACE(self):
        global req_s
        req_s += 1
        fprint(f"TRACE request {self.path}", 'SERVER', Fore.CYAN)
        self.send_response(503)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        date = strftime("%m-%d-%Y %H:%M:%S", localtime(time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))
        fprint(f"Function Unsupported 'TRACE'", 'ERROR', Fore.LIGHTRED_EX)

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
        fprint(f'-s request', 'SERVER', Fore.CYAN)

    def do__d(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f'-d request', 'SERVER', Fore.CYAN)

    def do__v(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f'-v request', 'SERVER', Fore.CYAN)
    
    def do__t(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f'-t request', 'SERVER', Fore.CYAN)
        date = strftime("%m-%d-%Y %H:%M:%S", localtime(time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

    def do__m(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f'-m request', 'SERVER', Fore.CYAN)

    def do__r(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        fprint(f'-r request', 'SERVER', Fore.CYAN)

    def do_signon(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


    def do_SeperateInterfaceID(self):
        seperateIntefaceIP.append([self.client_address[0], self.path])
        self.send_response_only(200)
        self.end_headers()




if __name__ == "__main__":

    fprint('', '', Back.RESET)
    webServer = HTTPServer((hostName, serverPort), LoopbackServer)
    fprint(f"Server started http://{hostName}:{serverPort} @ {ip_addr}", 'SERVER', Fore.CYAN)
    fprint(f"Server started http://{RLHostName}:{serverPort} @ {RLHostIPBaseAddr}", 'SERVER', Fore.CYAN)
    fprint('Listening on port %s ...' % serverPort, 'INFO', Fore.GREEN)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    sleep(0)
    print("Server stopped.")

"""
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
        self.wfile.write(bytes("<head><title>LoopbackServerA1</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes(("<p>CLIENT: %s<p>" % str(self.client_address)), "utf-8"))
        self.wfile.write(bytes(("<p>SERVER: %s<p>" % str(ip_addr + ":" + str(serverPort))), "utf-8"))
        self.wfile.write(bytes(("<p>CONNECTION: %s<p>" % str(self.connection)), "utf-8"))
        self.wfile.write(bytes(("<p>COMMAND: %s<p>" % str(self.command)), "utf-8"))
        self.wfile.write(bytes(("<p>HEADERS: %s<p>" % str(self.headers)), "utf-8"))
        print("CLIENT: ", self.client_address)
        print("CONNECTION: ", self.connection)
        print("COMMAND: ", self.command)
        print("HEADERS: \n", self.headers)
"""





