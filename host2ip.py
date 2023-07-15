#!/usr/bin/env python3

import os
import sys
import socket
from colorama import Fore

print('''
██╗░░██╗░█████╗░░██████╗████████╗██████╗░██╗██████╗░
██║░░██║██╔══██╗██╔════╝╚══██╔══╝╚════██╗██║██╔══██╗
███████║██║░░██║╚█████╗░░░░██║░░░░░███╔═╝██║██████╔╝
██╔══██║██║░░██║░╚═══██╗░░░██║░░░██╔══╝░░██║██╔═══╝░
██║░░██║╚█████╔╝██████╔╝░░░██║░░░███████╗██║██║░░░░░
╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝╚═╝░░░░░''')
print(Fore.GREEN + 'Author: Freddy Phoenix Mills')
print(Fore.GREEN + 'E-Mail: phoenixgibson007@gmail.com\n' + Fore.RESET)
def usage():
     print("This tool is used to convert the hostname/website name to the IPaddress")
     print("To use host2ip,Use: \n" + sys.argv[0] + " WebsiteName")

try:
    host = sys.argv[1]
    ip = socket.gethostbyname(host)
    print(Fore.BLUE + "The ip address for " + sys.argv[1] + ' is: \n' + Fore.GREEN + ip + Fore.RESET)
except IndexError:
    usage()
