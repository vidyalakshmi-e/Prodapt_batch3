#AI chatbot receiving mixed inputs-union, sequence

from typing import Union,Sequence
InputData=Union[str,bytes]

def chatbots(inputs:Sequence[InputData]):
    for item in inputs:
        if isinstance(item,str):
            print("User Text: ",item)
        else:
            print("Image uploaded : (",len(item),"bytes)")

conversation=(
    "Hi",
    "Show me nearby restaurants",
    b'\xff\xd8\xff',#jpeg 3 bytes b'/x89PNG - png image 4 bytes
    "Explain this iamge"
)

chatbots(conversation)