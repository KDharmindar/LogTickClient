"""
Author: Dharmindar Devsidas
Company: DJVSOFT CONCEPTS
URL: http://www.djvsoft.com
Blog: http://www.programmingmyths.com

Description: This class utilizes sockets library and provides easy to use API
for developers to create servers and clients and communicate to each other. The 
calls are non-blocking and multiple clients can connect to the server.

To create a server you need to provide following attributes other than network_address 
which is a tuple for host and port values.
1. is_server : It is a boolean value which if set to True will generate a Socket Server.
2. max_clients_allowed : It is a number of clients allow 

"""

import socket, select
import pickle

class NetworkCommunicationHandler:
    received_data = None
    buffer = []
    is_client = None
    trace_messages = []
    server_socket = None
    # If is_server is set to True then it will generate SERVER else it CLIENT
    def __init__(self, network_address, is_server=None, max_clients_allowed=None):
        
        self.trace_messages.append('Creating a network communication handler')
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if is_server == False or is_server is None:
            self.server_socket.connect(network_address)
            self.is_client = True
            self.trace_messages.append('Client created.')
        else:
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(network_address)
            self.server_socket.listen(max_clients_allowed)
            self.is_client = False
            self.trace_messages.append('Server created')
            

    def __del__(self):
        self.server_socket.close()
        
    def send_data(self, data):
        try:
            self.trace_messages.append('send is started')
            self.server_socket.sendall(data)
            self.trace_messages.append('send is done')
        except Exception as e:
            self.trace_messages.append(e)
            self.error_message = str(e.args[0])
            
    def receive_data(self):
        try:
            self.trace_messages.append('Entering to receive data.')
            socket_list = [self.server_socket]
            while socket_list:
                self.trace_messages.append('Starting to select')
                ready_to_read, ready_to_write, in_error = select.select(socket_list, [], socket_list)
                self.trace_messages.append('Select successfully run')
                
                for sock in ready_to_read:
                    self.trace_messages.append(sock)
                    if sock == self.server_socket:
                        self.trace_messages.append('Establishing connection')
                        connection, client_address = sock.accept()
                        self.trace_messages.append('Connection established')
                        connection.setblocking(0)
                        socket_list.append(connection)
                        self.trace_messages.append('appended to server list')
                    else:
                        self.trace_messages.append('Data receiving is to start')
                        data = []
                        while 1:
                            self.trace_messages.append('Entered in socket loop')
                            data = sock.recv(4096)
                            if data:
                                self.trace_messages.append('has data')
                                self.buffer.append(data)
                                self.trace_messages.append('Data appended to buffer')
                            else:
                                self.trace_messages.append('No data')
                                break
                        if data is not None:
                            try:
                                self.trace_messages.append('Starting deserialization of data')
                                self.received_data = pickle.loads(b''.join(data))
                                self.trace_messages.append('Data deserialized')
                            except(EOFError):
                                self.trace_messages.append('EOFError occured')
                                break
                    socket_list.remove(connection)
                    self.trace_messages.append('connection removed from the socket_list')            
        except Exception as e:
            self.error_message = str(e.args[0])
            self.trace_messages.append('Exception occured' - e.args[0].__str__())        