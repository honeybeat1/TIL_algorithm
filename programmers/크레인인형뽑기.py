def solution(board, moves):
    lst = []
    answer = 0
    for i in moves:
        n = len(lst)
        if n >= 2:
            if lst[n-2] == lst[n-1]:
                lst = lst[:-2]
                answer += 2
        for j in range(len(board)):
            if board[j][i-1] != 0:
                lst.append(board[j][i-1])
                board[j][i-1] = 0
                break # break하면 if문 탈출해서 for문을 돈다는 것 염두
    return answer