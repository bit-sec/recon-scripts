import os
import time
from multiprocessing import Process
def dnsEnumWorker(host, port):
    """ 
    Gathers DNS information from <host>, <port>
    """
    print('Not yet implemented')
def nmapTcpScan(ipAddress)
    ipAddress = ipAddress.strip()
    print "[*] Running TCP nmap scan for %s" % (ipAddress)
    servDict = {}
    scanCommand = ""
    scanResult = subprocess.check_output(scanCommand, shell=True)
    scanLines = scanResult.split("\n")
    for scanLine in scanLines:
        ports = []
        scanLine = scanLine.strip()
        if ("tcp" in scanLine) and ("open" in scanLine) and not ("Discovered" in line):
            while "  " in scanLine:
                scanLine = scanLine.replace("  ", " ")
            scanLineSplit = scanLine.split(" ")
            service = scanLineSplit[2]
            port = scanLineSplit[0]
            if service in servDict:
                port = servDict[service]
            ports.append(port)
            servDict[service] = ports
    for service in servDict:
        ports = servDict[service]
        print "%s: found service %s" % (ipAddress, service)
        for port in ports:
            port = port.split("/")[0]
            print "port %s" % (port)
def main():
    f = open('', 'r')
    for scanip in f:
        jobs = []
        p = multiprocessing.Process(target=nmapTcpScan, args=(scanip,))
        jobs.append(p)
        p.start()
    f.close()
