#다이얼
alphabet = ('ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ')
word=input()
second=0
for character in word:
    for i in alphabet:
        if character in i:
            second+=alphabet.index(i)+3
print(second)