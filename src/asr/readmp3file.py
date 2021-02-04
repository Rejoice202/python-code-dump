import os, sys
import base64

file = "01_-_That_Time_I_Got_Reincarnated_as_a_Slime.mp3"
#file = "KOE.mp3"
f = open(file, mode='rb')
print(type(f))
data = base64.b64encode(f.read())
print(type(data))
print(len(data))
