from bytes import Bytes

print "Hello World"

bytes = Bytes(4, 128)

file = open("test.txt", "wb")

file.write(bytes.getBinary())