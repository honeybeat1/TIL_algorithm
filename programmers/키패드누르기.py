# 중간  저장
import numpy as np

def solution(numbers, hand):
    map = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    
    # 2차원 배열 index 구하는 함수
    def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
        
    # 각 위치별로 거리 값이 담긴 2차원 배열 생성
    def distance(start):
        dist = np.zeros((4,3))
        start_xy = index_2d(map, start)
        for i in range(4):
            for j in range(3):
                dist[i][j] = abs(i-start_xy[0]) + abs(j-start_xy[1])
        return dist
    L = 10 # *
    R = 12 # #
    for i in numbers:
        if i in [1,4,7]:
            L = i
        elif i in [3,6,9]:
            R = i
        else:
            L_distance = distance(L)
            
    answer = ''
    return answer
