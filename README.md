# script_python

Team members: Zhansaya, Nuray, Ainara

We choose Python language to write our automation script. Our script includes three common tasks such as scanning for open ports, enumeration services on chosen port and retrieving a list of working directories. 

1) Port scanning: The nmap_scan function uses the nmap module to perform a port scan on the specified target IP address. It scans for open ports within the range of 10 to 81 (inclusive) and prints the open ports it finds. 
2) Enumerating services:  The enumerate_services function uses the socket module to retrieve the service name associated with a specific port on the provided target IP address. It prints the service name if it is known, and shows an "Unknown service" message if an error occurs or the service is unknown.
3) Finding directories on a web server: The find_directories function reads a wordlist file containing directories to be appended to the provided URL. It sends HTTP GET requests to the generated URLs and prints the ones that return a status code of 200, indicating a working directory.
4) Dependencies: The code relies on the nmap, socket and requests modules. Make sure you have these modules installed before running the script. You can install any missing modules using pip install <module_name>.
5) Wordlist: The find_directories function assumes a wordlist file located at "/usr/share/wordlists/dirb/common.txt" by default.

Link to the demonstration video: https://youtu.be/riQcfu13sb4
More detailed report in the Word file.
