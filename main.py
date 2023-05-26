import nmap
import os
import socket
import re
import requests


def nmap_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, '10-81')
    for host in scanner.all_hosts():
        for port in scanner[host].all_tcp():
           if scanner[host]['tcp'][port]['state'] == 'open':
              print(f"Port {port} is open.")


def enumerate_services(target, port):
    try:
        print(f"Enumerating services on {target}:{port}...")
        service_name = socket.getservbyport(int(port))
        print(f"Service name: {service_name}")
    except socket.error:
        print("Unknown service")


def find_directories(url,usr):
    with open(usr, 'r') as word:
         for line in word:
             directory = line.strip()
             url2 = f"{url}/{directory}"
             response = requests.get(url2)
             if response.status_code==200:
                print(f"Working directory: {url2}")


if __name__ == "__main__":
    target = input("Write your IP address: ")
    if target:
        print("Scanning for open ports...")
        nmap_scan(target)
    else:
        print("No IPv4 address found.")
    port = input("Choose one of your open ports: ")
    enumerate_services(target, port)
    print("Now we will find directories of found web server...")
    url = f"http://{target}"
    usr = "/usr/share/wordlists/dirb/common.txt"
    find_directories(url,usr)
