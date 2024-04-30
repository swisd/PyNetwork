import socket
import os
import sys
import platform
import statistics
import uuid


print("| Python " + platform.python_version() + " |")
print("IPv:", socket.IPPROTO_IPV4)
print("Name: " + socket.gethostname())
print("FQDN: " + socket.getfqdn())
print("System Platform: "+sys.platform)
print("Machine: " + platform.machine())
print("Node " + platform.node())
print("Platform: "+platform.platform())
print("Processor: " + platform.processor())
print("System OS: "+platform.system())
print("Release: " + platform.release())
print("Version: " + platform.version())
# print("Number of CPUs: " + str(psutil.cpu_count()))
# print("Number of Physical CPUs: " + str(psutil.cpu_count(logical=False)))
# Need  Model of Computer i.e.  HP Compaq 8100 Elite SFF, HP X600 workstation
# need Ram
# need Disk space
# Need Manufacturer i.e. HP, Dell, Lenova
