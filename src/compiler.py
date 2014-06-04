from src.items.bytes import Bytes
from src.items.header_item import HeaderItem


bytes = Bytes(4, 0x12345678)
  
file = open("test.txt", "wb")
  
file.write(bytes.data)

# arr = [Bytes(1, 3), Bytes(1, 64)]
# for x in arr: 
#     print x.data
#     file.write(x.data) 

header = HeaderItem()
print header.getItemOffset(5)
print header.getBytesCount()