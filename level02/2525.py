#	오븐 시계
hour, minute = map(int, input().split())
timer = int(input())
time = hour*60+minute
time += timer
hour=time//60
minute=time%60
if hour>=24:
    hour-=24
print(hour,minute)

