b=""
a=0
while True:
    a+=1
    b+=str(a)
    if len(b)>=1000000:
        break
print(int(b[0])*int(b[9])*int(b[99])*int(b[999])*int(b[9999])*int(b[99999])*int(b[999999]))

