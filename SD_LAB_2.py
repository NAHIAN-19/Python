#While loop in python
i=1
print("While Loop part START----->")
while i < 6:
    print(i,end=" ")
    if (i == 3):
        print("")
        break
    i+=1
print("<-----While Loop part END")
#->for loop in python    
print("<-----For Loop part START----->")
arr=["My","Name","is","Nahian","Nazeeb"]
for n in arr:
    if n == "Nazeeb":
        break
    print("\t",n,end=" ")
print("")
print("<-----For Loop part END----->")
print("<-----Taking Input From Console----->")
x=input('Enter Any Junk : ')
print("<-----Printing X----->")#any datatype
print("             "+x)
print("<-----X Printed Successfully----->")
#######PERSONAL########