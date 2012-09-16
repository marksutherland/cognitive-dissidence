import socket
import unittest
from socket_utils import port_string_length, source_address_length, zero_pad

class SocketTest(unittest.TestCase):

  def setUp(self):
    self.node_socket = 1234
    self.listen_socket = 1235
    self.host_ip = socket.gethostbyname(socket.gethostname())
    self.node_address = (self.host_ip, self.node_socket)
    self.test_address = (self.host_ip, self.listen_socket)
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    self.listener.bind(self.test_address)
    self.listener.settimeout(1)
    self.listener.listen(5)

  def tearDown(self):
    pass

  def test_connect(self):
    self.client.connect(self.node_address)
    self.client.send(zero_pad(str(self.listen_socket), port_string_length))
    self.client.close()
    incoming, address = self.listener.accept()
    expected_sources = incoming.recv(1)
    incoming.close()
    source_table = set()
    for i in range(int(expected_sources)):
      source_socket, address = self.listener.accept()
      source_address_string = source_socket.recv(source_address_length)
      source_address_string = source_address_string.lstrip('0')
      source_host, partition, source_port = source_address_string.partition(':')
      self.assertNotEqual(source_host, "")
      self.assertNotEqual(partition, "")
      self.assertNotEqual(source_port, "")
      source_table.add((source_host, int(source_port)))
    self.assertTrue(self.test_address in source_table)

if __name__ == '__main__':
  unittest.main()
