#!/usr/bin/env python3
"""
Main file
"""
import sys
sys.path.append('/root/holbertonschool-web_back_end/pagination')
Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(6473, 3))
print("---")
print(server.get_hyper(3000, 100))


