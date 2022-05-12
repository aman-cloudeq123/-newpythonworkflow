import sys


first_number = int(sys.argv[1])
last_number = int(sys.argv[2])




for number in range(first_number,last_number+1):

    if number > 1:
        for i in range(2, number):
            if(number%i==0):
                break
        else:
            print("prime numbers:",number)

