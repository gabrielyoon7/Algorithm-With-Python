#크로아티아 알파벳
croatianAlphabet=['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
for i in croatianAlphabet:
    word=word.replace(i,'a')
print(len(word))