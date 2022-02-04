#단어 공부
from numpy import character

word=input().lower()
character=[0]*26
for i in word:
    character[ord(i)-97]+=1
print(character)
max=0
maxIndex=-1
index=-1
isDuplicated=False
for i in character:
    index+=1
    if i == max:
        isDuplicated=True
    if i>max:
        max=i
        maxIndex=index
        isDuplicated = False
if isDuplicated:
    print("?")
else:
    print(chr(maxIndex+65))