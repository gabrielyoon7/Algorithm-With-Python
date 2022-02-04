#단어 공부
word=input().upper()
character=[0]*26
for i in word:
    character[ord(i)-65]+=1
# print(character)
max=0
answer=""
for i in range(len(character)):
    if character[i]>max:
        max=character[i]
        answer=chr(i+65)
    elif character[i]==max:
        answer="?"
print(answer)