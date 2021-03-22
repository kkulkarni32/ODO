"""Code to send data to Max"""
import socket
import sys
import json
from pythonosc import udp_client #need to install this in the system "pip install python-osc"
# Create a UDP socket

def send_data_to_max(tag,message,ip,port):
	"""This is function to send the osc-udp messages:
	@param string tag 				This indicates the message type. For example if it is a simple response from chatbot then the tag can be "/ame_chatbot". Likewise 
									it is message to display something then the tag can be "/ame_display". The max system will be able to filter the message and act 
									accordingly on the basis of the tag.
	@param string message			The message that needs to be send
	@param string ip				The ip address of the systme to which the message is to be sent
	@param int port					The port to which the message has to be sent
	@return boolean 				Returns true after completing the code
"""
	try:
		client = udp_client.SimpleUDPClient(ip, port)
		client.send_message(tag, message)
	finally:
		return True

#tag "/stop" #sample tag
#message = "abcd26872    09u7iuogh" #sample message
while(1):
	tag = input("enter tag")
	message = input("enter message")
	ip = "192.168.0.48" #sample ip
	port = 7403 #sample port
	send_data_to_max(tag,message,ip,port) #sample call
