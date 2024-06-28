import random

print("Who are you?")
name = input()
print('Hello,',name,'!')
print('Tossing a coin...')
Head = 0
Tail = 0
for i in range(0,3):
    num = random.randint(0,1)
    if(num):
        value = 'Heads'
        Head += 1
    else:
        value = 'Tails'
        Tail += 1
    print('round',i+1,':',value)
print('Heads:',Head,'Tails:',Tail) 
    