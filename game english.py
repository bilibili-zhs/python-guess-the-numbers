from random import randint as random_number
from time import sleep as wait
import pyttsx3
from rich import print
talker = pyttsx3.init()
def chat(chat):
    talker.say(chat)
    talker.runAndWait()
end = ''
time_list = []
times = 0
time0 = 0
def output():
    print('''

    ''')
    print('Record:')
    print('Times', 'Used')
    for a1 in range(times):
        print(a1 + 1, '       ', time_list[a1])

star = '''__________________________________________________________________
Powered By:
_____  __ __  _____    
|     T|  T  T/ ___/  
l__/  ||  l  (   \\_  
|   __j|  _  |\\__  T 
|  /  ||  |  |/  \\ |  
|     ||  |  |\\    |   
l_____jl__j__j \\___j    
    BILIBILI:UID:1851635221 NAME:coding's zhs'''
print(f'[red]{star}[/red]')
chat('Please enter the minimum range:')
a = int(input('Please enter the minimum range:'))
chat('Please enter the maximum range:')
b = int(input('Please enter the maximum range:'))

while True:
    num = random_number(a, b)
    time0 = 0
    player = None
    chat('What is your number:')
    player = int(input('What is your number:'))
    print('🤔🤔🤔')
    wait(0.3)
    if player != num:
        time0 += 1
        if player < num:
            print('Too small')
            chat('Too small')
        else:
            print('Too big')
            chat('Too small')
    else:
        time0 += 1
        print(f'Congratulations, you are right! The number is {player}!!!')
        chat(f'Congratulations, you are right! The number is {player}!!!')
        print(f'You used {time0} times to answer correctly...........')
        time_list.append(time0)
        input('Press enter to continue')
        times += 1
        user_input = ''
        while not user_input:
            user_input = input('Enter[1] to try again, enter[2] to exit:')
            if not user_input:
                print('Input cannot be empty, please re-enter')
        user_input = int(user_input)
        if user_input == 2:
            output()
            break
