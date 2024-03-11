
a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))


print("1.sumar")
print("2.restar")
print("3.multiplicar")
print("4.dividir")

print("ingrese la operacion a realizar: ")
c=(input())
print("resultado: ")

if c=="1":
     print(a + b)

if c=="2":
    print(a-b)
if c=="3":
    print(a*b)
if c=="4":
    print(a/b)