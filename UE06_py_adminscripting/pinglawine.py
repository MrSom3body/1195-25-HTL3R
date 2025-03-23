__author__ = "Karun Sandhu"

import subprocess
import ipaddress

address_string = input("Enter the network address: ")
subnet_suffix_string = input("Enter the subnet suffix: ")

address = ipaddress.IPv4Network(f"{address_string}/{subnet_suffix_string}")

print("Hosts online:")
for ip in address.hosts():
    res = subprocess.call(
        ["ping", "-c", "1", "-q", str(ip)], stdout=subprocess.DEVNULL
    )

    if res == 0:
        print(str(ip))
