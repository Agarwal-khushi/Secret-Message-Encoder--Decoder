# Secret Message Encoder & Decoder
message=input(" Enter the message here : ")
special=input("enter the special you want to use : ")
length=len(message)//2
first=message[length:]
second=message[:length]
rearrange=second+special+first+special
encode=rearrange[::-1]
print("encoded message : ",encode)
back= encode[::-1]
parts=back.split(special)
if len(parts) >= 2:
    decoded = parts[0] + parts[1]
    print("Decoded Message:", decoded)
else:
    print("Error in decoding. Special character not found properly.")