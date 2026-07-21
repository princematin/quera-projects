n, m = map(int, input().split())

board = []

for x in range(n):
    board.append([])
    for y in range(m):
        board[x].append(0)

bombs = int(input())

pos = [-1, 0, 1]

for i in range(bombs):
    b_n, b_m = map(int, input().split())

    b_n -= 1
    b_m -= 1

    board[b_n][b_m] = '*'

    for j in pos:
        for h in pos:
            if j == 0 and h == 0 :
                continue
            new_x = b_n + j
            new_y = b_m + h
            if 0 <= new_x < n and 0 <= new_y < m: 
                    if board[new_x][new_y] != '*':
                        board[new_x][new_y] += 1

for i in board:
    for j in i:
        print(j , end=' ')
    print('')
