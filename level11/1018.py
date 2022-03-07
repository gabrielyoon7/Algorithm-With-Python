#체스판 다시 칠하기 (실패)
N, M = map(int, input().split())
chess_map=""
w_first=['W','B']
b_first=['B','W']
w_first_count=0
b_first_count=0
for i in range(M):
    chess_map+=input()
# print(chess_map)
for i in range(len(chess_map)):
    if (i//N)%2 == 0 and w_first[(i%M)%2]!=chess_map[i]:
        w_first_count+=1
        print(i,i//N,i%M,chess_map[i])
    elif (i//N)%2 == 1 and b_first[(i%M)%2]!=chess_map[i]:
        w_first_count+=1
        print(i,i//N,i%M,chess_map[i])
print(w_first_count)

for i in range(len(chess_map)):
    if (i//N)%2 == 0 and b_first[(i%M)%2]!=chess_map[i]:
        b_first_count+=1
        print(i,i//N,i%M,chess_map[i])
    elif (i//N)%2 == 1 and w_first[(i%M)%2]!=chess_map[i]:
        b_first_count+=1
        print(i,i//N,i%M,chess_map[i])
print(b_first_count)
print(min(w_first_count,b_first_count))
