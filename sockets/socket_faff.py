import socket
from socket_utils import port_string_length, source_address_length, zero_pad

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind((socket.gethostname(), 1234))
listener.listen(5)

source_table = set()

def get_return_address_from_client(listener):
  client, address = listener.accept()
  return_port = client.recv(port_string_length)
  client.close()
  print "greeting from %s, return port %s" % (str(address), return_port)
  return (address[0], int(return_port))

def print_table(table):
  for address in table:
    print str(address)

def send_table_length(client_address, table_length):
  table_length_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  table_length_socket.connect(client_address)
  table_length_socket.send(str(table_length))
  table_length_socket.close()

def pad_source_address(source_address):
  return zero_pad("%s:%s" % (source_address[0], str(source_address[1])),
                  source_address_length)


def send_source_address(client_address, source_address):
  table_length_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  table_length_socket.connect(client_address)
  table_length_socket.send(pad_source_address(source_address))
  table_length_socket.close()

while True:
  client_address = get_return_address_from_client(listener)
  source_table.add(client_address)
  print "source table:"
  print_table(source_table)
  send_table_length(client_address, len(source_table))
  for address in source_table:
    send_source_address(client_address, address) 
