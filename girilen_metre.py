a = int(input("metre uzunluğu giriniz "))

print("1 = mm, 2 = cm, 3 = dm, 4 = km")

sec = int(input("seciminizi yapınız "))
if(sec==1):
    b = 1000*a
elif(sec==2):
    b = 100*a
elif(sec==3):
    b = 10*a
elif(sec==4):
    b = a/1000

print(b)

