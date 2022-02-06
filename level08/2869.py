#달팽이는 올라가고 싶다
import math
A,B,V= map(int, input().split())
velocity=A-B
height=V-B
print(math.ceil(height/velocity))