import sys

number=sys.argv[1]

a=0
b=1
sum=0
count=1
print("Fibonacci series :" , end=" ")
while count<=number :
    print(sum , end=" ")
    count=count+1
    a=b
    b=sum
    sum=a+b
# Onemax=0
# count=1
# Zeromax=0
# for i in  range(len(inpt)-1):
#     if inpt[i]==inpt[i+1]:
#         count=count+1
#         if  inpt[i+1]== "0":

#             if(count>Zeromax):
#                 Zeromax=count
#         else:
#             if(count>Onemax):
#                 Onemax=count
#     else:
#         count=1

# if(Zeromax<Onemax):
#     for i in range(Onemax):
#         print("1" , end="")

# else:
  
#     for i in range(Zeromax):
#         print("0" , end="")  



