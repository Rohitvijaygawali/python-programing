print("Enter the subject mark")
m=[]
for i in range(1,5):
    a=int(input(f"Enter the mark {i}:"))
    m.append(a)

for i in range(4):
    if m[i]<50:
        print(f"failed in {i+1} subject")
        break;


s=sum(m)
per=s/4

if(per>80):
    print("A")
elif(per>70):
    print("B") 
elif(per>60):
    print("C")
else:
    print("Fail")   