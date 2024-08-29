import os
import time
from dan import dan
os.system('cls')
print('Welcome, I am Dan, your personal valorant trainer\npick a color\n 0:purple')
color = input()
try:
    color=int(color)
except:
    raise(Exception('pick a number retard'))

os.system('cls')
print('Nice! Now whats ur resolution seperated by spaces (ex. 1920 1080)?')
resolution = input()
try:
    resolution=map(int,resolution.split())
except:
    raise(Exception('bro you really dont know how to do this do you'))

os.system('cls')
print('what should the activation key be. enter nothing for control')
activation_key=input()
if(activation_key==''):
    activation_key='ctrl'

os.system('cls')
print('what should the fov be')
fov=input()
try:
    fov=int(float(fov))
except:
    raise(Exception('ur fucking retarded'))

os.system('cls')
print('what is your mouse dpi ex 0.8 would mean your mouse is 0.8 times as slow')
mouse_dpi=input()
try:
    mouse_dpi=int(float(mouse_dpi))
except:
    raise(Exception('ur fucking retarded'))

os.system('cls')
print('what is your valorant sensitivity')
valorant_dpi=input()
try:
    valorant_dpi=int(float(valorant_dpi))
except:
    raise(Exception('ur fucking retarded'))

os.system('cls')
print('Finally, now we can get started\n')
time.sleep(1)
print('Finding process..')
time.sleep(0.75)
print('Updating resources...')
time.sleep(1)
print('Injecting cheat...')
time.sleep(2)
print('Attempting vanguard bypass...')
time.sleep(5)
print('\nlol just kidding it uses color. starting...')
time.sleep(1)


bot = dan(resolution=resolution,fov=fov,activation_key=activation_key,color=color,use_arduino=True,vdpi=valorant_dpi)
while True:
    bot.task()