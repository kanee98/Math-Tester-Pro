#Kanishka Udapitiya - KUDKC152

import random

total = 0
finaltotal = 0
x =0

print('Welcome to Maths Tester Pro.')
print('----------------------------')
print('Select a difficulty:')
print('1) Easy')
print('2) Medium')
print('3) Hard')
print()

def genarateQuestions(maxNum):

    global answer 
    number1 = random.randint(1,maxNum)
    number2 = random.randint(1,maxNum)
    op = random.randint(1,2)
    
    if op == 1:
        answer = number1 + number2
    elif op == 2:
        answer = number1 - number2
        
    if op == 1:
        ops = '+'
    elif op == 2:
        ops = '-'
        
    print('what is ',number1,ops, number2,'?', '(Answer is only for testing:', answer,')')
    return ''

option = int(input())

while option != 1 and option != 2 and option != 3 and option !=0:
    print ('Invalid input! Please enter a valid number.')
    option = int(input())
    
if option == 1:
    lives = 3
    maxNum = 10
    print('You have selected Easy')
    print()
    
    while x<10:
        x += 1
    
        print('Question',x,'of 10, ',lives,'lives remaining',)
        print(genarateQuestions(maxNum))
    
        userinput = int(input())
    
        if answer == userinput:
            total += 1
        else:
            lives = lives - 1
        if lives == 0:
            print ('You are out of lives. Game over')
            break 
    
    print()        
    print('Results:'"\n"'You scored ',total,'/ 10.')
    finaltotal = total/10*100

    if finaltotal >= 50:
        print(finaltotal,'% - You pass!')
    else:
        print(finaltotal,'% - You fail!')

    
if option == 2:
    lives = 2
    maxNum = 25
    print('You have selected Medium')
    print()

    while x<10:
        x += 1
        
        print('Question',x,'of 10, ',lives,'lives remaining',)
        print(genarateQuestions(maxNum))
        
        userinput = int(input())
        
        if answer == userinput:
            total += 1
        else:
            lives = lives - 1  
        if lives == 0:
            print ('You are out of lives. Game over')
            break 
        
    print()        
    print('Results:'"\n"'You scored ',total,'/ 10.')
    finaltotal = total/10*100

    if finaltotal >= 50:
        print(finaltotal,'% - You pass!')
    else:
        print(finaltotal,'% - You fail!')

    
if option == 3:
    lives = 1
    maxNum = 50
    print('You have selected Hard')
    print()

    while x<10:
        x += 1
        
        print('Question',x,'of 10, ',lives,'lives remaining',)
        print(genarateQuestions(maxNum))
        
        userinput = int(input())
        
        if answer == userinput:
            total += 1
        else:
            lives = lives - 1
        if lives == 0:
            print ('You are out of lives. Game over')
            break 
        
    print()        
    print('Results:'"\n"'You scored ',total,'/ 10.')
    finaltotal = total/10*100

    if finaltotal >= 50:
        print(finaltotal,'% - You pass!')
    else:
        print(finaltotal,'% - You fail!')
    
if option == 0:
    print ('Thank you for using Maths Tester Pro!'+'\nHope to see you soon!')



    
