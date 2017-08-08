#!/usr/bin/python3

import socket

if __name__ == '__main__':
	hostname = input("Enter hostname(www.example.com):\t")
	sevc_query = input("What service woulr you like(\'domain\'):\t")
	addr = socket.gethostbyname(hostname)
	service = socket.getservbyname(sevc_query)
	print('The IP address of {} is {}'.format(hostname, addr))
	print('The {} service is running on Port {}'.format(sevc_query, service))
