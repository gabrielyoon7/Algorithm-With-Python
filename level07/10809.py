#알파벳 찾기
word = input()
alphabet = [-1,]*26
for i in range(len(word)):
    code=ord(word[i])-97
    if alphabet[code]==-1:
        alphabet[code]=i
for i in alphabet:
    print(i, end=" ")
