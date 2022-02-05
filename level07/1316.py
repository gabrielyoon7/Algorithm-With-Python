#그룹 단어 체커
N = int(input())
count=0
for i in range(N):
    word=input()
    temp=''
    alphabet=[False]*26
    isGroup=True
    for character in word:
        if alphabet[ord(character)-97]:
            if temp!=character:
                isGroup=False
                break
        else:
            alphabet[ord(character)-97]=True
            temp = character
    if isGroup:
        count+=1

print(count)
