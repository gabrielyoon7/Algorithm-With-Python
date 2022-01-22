hour, minute = map(int, input().split())
time = hour*60+minute
time -= 45
hour=time//60
minute=time%60
if hour<0:
    hour+=24
print(str(hour)+" "+str(minute))

