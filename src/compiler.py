from src.items.header_item import HeaderItem
from src.parser.bytes import Bytes
 
bytes = Bytes(4, 0)
  
file = open("test.txt", "wb")
  
file.write(bytes.getBinary())

header = HeaderItem()
print header.getItemOffset(5)