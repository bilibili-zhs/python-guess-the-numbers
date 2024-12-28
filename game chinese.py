from random import randint as 随机数
from time import sleep as 等待
import pyttsx3
from rich import print
talker=pyttsx3.init()
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
    print('战绩：')
    print('第几次', '用了几次')
    for a1 in range(times):
        print(a1 + 1,'       ',time_list[a1])

star='''__________________________________________________________________
Powered By:
_____  __ __  _____    
|     T|  T  T/ ___/  
l__/  ||  l  (   \\_  
|   __j|  _  |\\__  T 
|  /  ||  |  |/  \\ |  
|     ||  |  |\\    |   
l_____jl__j__j \\___j    
    BILIBILI:UID:1851635221 NAME:coding的zhs'''
print(f'[red]{star}[/red]')
chat('请输入最小范围：')
a = int(input('请输入最小范围：'))
chat('请输入最大范围：')
b = int(input('请输入最大范围：'))

while True:
    num = 随机数(a, b)
    time0 = 0
    player = None
    chat('你的数字是什么：')
    player = int(input('你的数字是什么：'))
    print('🤔🤔🤔')
    等待(0.3)
    if player != num:
        time0 += 1
        if player < num:
            print('小了')
            chat('小了')
        else:
            print('大了')
            chat('小了')
    else:
        time0 += 1
        print(f'恭喜你答对了，就是{player}!!!')
        chat(f'恭喜你答对了，就是{player}!!!')
        print(f'你用了{time0}次才答对的哦...........')
        time_list.append(time0)
        input('回车键继续')
        times += 1
        user_input = ''
        while not user_input:
            user_input = input('enter[1] try again, enter[2] exit:')
            if not user_input:
                print('输入不能为空，请重新输入')
        user_input = int(user_input)
        if user_input == 2:
            output()
            break
