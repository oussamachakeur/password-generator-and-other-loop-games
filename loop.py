'''
#hight average calculator

hights_input = (input('please enter the hights of all the student in cm separated with a space : '))
hights_list = hights_input.split()
hights= [int(i) for i in hights_list]
print(hights)
sum = 0
x=0
for x in hights :
    sum = sum + x

average = (sum /len(hights))
print(average)
'''
'''
# hoghst score in a list

class_grades= input('please enter all the grades of the class separated with a scpace: ')
grade = class_grades.split()
grade_list = [float(i) for i in grade]
print(grade_list)
#print(max(grade_list))
big = -1
for x in grade_list :
    if x > big :
        big = x
print(big)
    
'''
'''
#fizzbazz game 

for x in range(1,101):
    if (x % 3 == 0) and (x % 5 ==0):
        print('fizzbazz')        
    if x % 3 ==0:
        print("fizz")
    elif x % 5 ==0:
        print('bazz') 
    else :
        print(x)    
'''
# password generator
import random

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols= ['!',"@",'#','$','%','^','&','*','(',')','_','+','-','=']

print("welcome to password generator ")
al = int(input('how many alphabets u want: '))
num = int(input("how many digits us want: "))
sym = int(input("how many symbols u want : "))


password_list=[]

for x in range(0 , al):
    select1 = random.randint(0,(len(alphabets)-1))
    alphabet_selcted = alphabets[select1]
    password_list.append(alphabet_selcted)

for x in range(0 , num):
    select2= random.randint(0,(len(numbers)-1))
    number_selcted = numbers[select2]
    password_list.append(number_selcted)

for x in range(0 , sym):
    select3= random.randint(0,(len(symbols)-1))
    symbols_selcted = symbols[select3]
    password_list.append(symbols_selcted)

random.shuffle(password_list)
password = ''.join(password_list)
print('your password is : '+password)
   
