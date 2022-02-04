#상수
a,b = input().split()
new_a=""
new_b=""
for i in a:
    new_a=i+new_a
for i in b:
    new_b=i+new_b
print(max(int(new_a),int(new_b)))