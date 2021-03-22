"""Code to receive data from max"""
from oscpy.server import OSCThreadServer # need to install this library "pip install oscpy"
from time import sleep
def callback_sample_commmands_on_the_basis_of_tag(values):
	#Do something. Here we are just printing
        print("got values: {}".format(values))

def receive_data_from_max(ip,port):
        """
        A function to revieve the data from the Max_system:
        @param string ip				The ip address of the systme to which the message is to be sent
        @param int port					The port to which the message has to be send
        """
        osc = OSCThreadServer()
        sock = osc.listen(address=ip, port=port, default=True)
        #Here the function "callback_sample_commmands_on_the_basis_of_tag" is called on the basis of the tag's value
        osc.bind(b"/chat", callback_sample_commmands_on_the_basis_of_tag)
        osc.bind(b"/start", callback_sample_commmands_on_the_basis_of_tag)
        osc.bind(b"/names", callback_sample_commmands_on_the_basis_of_tag)
        osc.bind(b"/stop", callback_sample_commmands_on_the_basis_of_tag)
        osc.bind(b"/rgb", callback_sample_commmands_on_the_basis_of_tag)
        osc.bind(b"/haiku", callback_sample_commmands_on_the_basis_of_tag)
        osc.bind(b"/emotions", callback_sample_commmands_on_the_basis_of_tag)
        osc.bind(b"/jump", callback_sample_commmands_on_the_basis_of_tag)
        # osc.bind(b"/filter", callback_sample_commmands_on_the_basis_of_tag)
        #while(True): #always listining
        #	n=1
        sleep(1000)
        osc.stop()

receive_data_from_max("192.168.0.48",7400)
# while(True):
        # receive_data_from_max("192.168.0.48",7400)