bt=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
a=0
b=0
ab=0
o=0
for i in bt:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='AB':
        ab+=1
    else:
        o+=1
print(f"a:{a}, b:{b}, ab:{ab}, o:{o}")