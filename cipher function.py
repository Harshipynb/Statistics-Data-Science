




def ciph(user):
    return chr(ord("A")+(ord(user)-ord('A')+3)%26)

inpu=input("enter string")
inpu=inpu.upper()
new=''
for i in inpu:
    
    if i in ", ." :
        new+=i
    else:
        new+=ciph(i)
print(new)
