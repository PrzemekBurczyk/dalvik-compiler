from bytes import Bytes

print "Hello World"

bytes = Bytes(20, 0x030c5e)

file = open("test.txt", "wb")

file.write(bytes.getBinary())
