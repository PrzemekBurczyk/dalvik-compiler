from src.items.bytes import Bytes
from src.items.header_item import HeaderItem
from src.items.string_id_item import StringIdItem


bytes = Bytes(None, 2, 0x278)

file = open("test.txt", "wb")
  
file.write(bytes._data)

# arr = [Bytes(1, 3), Bytes(1, 64)]
# for x in arr: 
#     print x.data
#     file.write(x.data) 

header = HeaderItem(None)
print header.getIndexOffset(5)
print header.getBytesCount()

header.signature._data.append(Bytes(None, 1))

print header.getIndexOffset(5)
print header.getBytesCount()

print header.data_off.value
print header.data_off.bytesCount
print header.data_off.data

header.data_off.bytesCount = 8

print header.data_off.value
print header.data_off.bytesCount
print header.data_off.data

header.data_off.bytesCount = 4
header.data_off.value = 0x12345678

print header.data_off.value
print header.data_off.bytesCount
print header.data_off.data

stringId = StringIdItem(None)
print
print stringId.getBytesCount()
print stringId.getIndexOffset(0)

