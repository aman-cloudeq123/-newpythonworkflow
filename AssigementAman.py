# find largest len

lst= ["11","0000001","88","345","1045"]
count=0
for i in lst:
    if len(lst)>count:
        count=len(i)
        word=i
print("Largest Element is : " ,  word)        



# Assigement 
# 1 program
number1=int(input("ENTER THE  FIRST NUMBER : "))
number2=int(input("ENTER THE  FIRST NUMBER : "))

lst=[]

for number in range(number1,number2+1):
    if (number%5!= 0 and number % 7==0) :
        lst.append(str(number))
print(','.join(lst) )       

# 2 program

inpt="00011111110000000000011110001111"
Onemax=0
count=1
Zeromax=0
for i in  range(len(inpt)-1):
    if inpt[i]==inpt[i+1]:
        count=count+1
        if  inpt[i+1]== "0":

            if(count>Zeromax):
                Zeromax=count
        else:
            if(count>Onemax):
                Onemax=count
    else:
        count=1

if(Zeromax<Onemax):
    for i in range(Onemax):
        print("1" , end="")

else:
  
    for i in range(Zeromax):
        print("0" , end="")       



#3rd program

lst_number   =  [10,12,1,3,10,12,5,6,6,3,7,7]
def remove_dup(duplist):
    noduplist=[]

    for i in duplist:
        if i not in noduplist:
            noduplist.append(i)

    return noduplist

print(remove_dup(lst_number))       



# 4th program

number=int(input("ENTER THE VALUE OF NUMBER : "))

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









# 5th program

participants_list = [
    ["Sam","Emma","Joan","Krish","John","Desmond","Tom","Nikole"],
    ["Brad","Walter","Sam","Krish","Desmond","Jennifer"],
    ["Tom","Krish","Emma","Mia","Nikole","Sam","Desmond"],
    ["Desmond","Sam","Krish","Mia","Harry"],
    ["Ron","Ginney","Ted","Krish","Mia","Sam","Sachin","Desmond","Kapil"],
    ["Krish","Brad","Walter","Jennifer","Desmond","Harry","Nikole","Sem"]
]
#firsdt part


lst_3= ["Sam","Emma","Joan","Krish","John","Desmond","Tom","Nikole"]

lst_4=[["Brad","Walter","Sam","Krish","Desmond","Jennifer"],
    ["Tom","Krish","Emma","Mia","Nikole","Sam","Desmond"],
    ["Desmond","Sam","Krish","Mia","Harry"],
    ["Ron","Ginney","Ted","Krish","Mia","Sam","Sachin","Desmond","Kapil"],
    ["Krish","Brad","Walter","Jennifer","Desmond","Harry","Nikole","Sam"]]

lst_5=[item for element in lst_4 for item in element]
# print(lst_5)


noduplist_1=[]
    
for c in lst_3:
    x=0
    for d in lst_5:
            if c==d:
                x+=1
                if x>=5:
                    break
    if x==5:        
            noduplist_1.append(c)
print("daily participants  : ", noduplist_1)          


#2nd part

lst=[item for element in participants_list for item in element]
# print(lst)
def remove_dup(duplist):
    noduplist_2=[]

    for i in duplist:
        c=0
        for j in duplist:
            if i==j:
                c=c+1
                if c>=2:
                    break
        if c!=2:        
            noduplist_2.append(i)

    return noduplist_2

print("only one time : ", remove_dup(lst))   

#3rd part
list_1= ["Sam","Emma","Joan","Krish","John","Desmond","Tom","Nikole"]

lst_2=[["Brad","Walter","Sam","Krish","Desmond","Jennifer"],
    ["Tom","Krish","Emma","Mia","Nikole","Sam","Desmond"],
    ["Desmond","Sam","Krish","Mia","Harry"],
    ["Ron","Ginney","Ted","Krish","Mia","Sam","Sachin","Desmond","Kapil"],
    ["Krish","Brad","Walter","Jennifer","Desmond","Harry","Nikole","Sem"]]

lst_3=[item for element in lst_2 for item in element]

# print(lst_3)


noduplist_3=[]
    
for a in list_1:
    c=0
    for b in lst_3:
            if a==b:
                c+=1
                if c>=1:
                   break
    if c!=1:        
            noduplist_3.append(a)
print("only first day participants  : ", noduplist_3)          






# 6th program


def odd_even( lst1,lst2):
    return [lst1[1: :2] , lst2[::2]]


lst1=[2,3,6,7,8,9,11,66,0,99,100,100001] 
lst2=[2,35,63,7,85,9,11,66,0,99,100,10]     

a=list()



print("ODD INDEX ELEMT IN FIRST LIST IS : and even ", odd_even(lst1) , odd_even(lst2))
# print("EVEN INDEX ELEMT IN SECOND LIST IS : " ,odd_even(lst2))

a=odd_even(lst1) + odd_even(lst2)

print(a)





#7th question

test_list=[{'aman' : 1 , 'aviral' : 3},
{'aman' : 2 , 'aviral' : 4},
{'saloni' : "5"}
]
print(" the original list : " + str(test_list) )


k='aman'

res=[ele for ele in test_list if k in ele]
print(" List after filtration : " + str(res) ) 



