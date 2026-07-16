#a company is building ai virutal assistant
#it has to accept different input format-text audio image
from typing import Union
def process_input(data: Union[str,bytes])->None:
    if isinstance(data,str):
        print("Processing Text: ",data)
    elif isinstance(data,bytes):
        print("Processing Image/Audio Bytes: ",data)

process_input("Artifical Intelligence")
process_input(b'\x89PNG\r\n')

#union-one varibale can accept different data types
#89 non printable byte used to identify PNG image
#\r Carriage return
#isinstance- checking the input type
