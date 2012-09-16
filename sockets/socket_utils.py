# ports will be no longer than 5 characters and ports < 1000 will be 0 padded at
# the start
port_string_length = 5
# this is enough for a full IPv4 address dotted quad, a semicolon and the port
# as above: "123.456.789.123:12345"
source_address_length = 21

def zero_pad(num_string, length):
  """Pads a string representation of a number with zeros at the start of the
  string until the string is length characters long."""
  result = ""
  if len(num_string) < length:
    for i in range(length - len(num_string)):
      result = result + '0'
    result = result + num_string
  return result
