a = float(input("a kenarını gir "))
b = float(input("b kenarını gir "))
c = float(input("c kenarını gir "))

if(a==b==c):
    print("eşkenar Üçgen")

elif(a==b or a==c or b==c):
    print("ikizkenar Üçgen")

elif(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
    print("dik üçgen")

elif(a!=b and a!=c and b!=c):
    print("çesitkenar Üçgen")