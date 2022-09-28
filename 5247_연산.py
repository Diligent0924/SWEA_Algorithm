# 똑같은 방식이여도 재귀는 Error가 뜬다. 왜이럴까요?
# 해당 재귀는 DFS로 문제를 풀었고 BFS는 가까운 순서대로 문제를 풀기 때문에 가장 빠르면 그냥 끝내버리면 된다.
# def solution(N, count, previous):
#     global min_count
#     if count >= min_count or N > 1000000:
#         return
#
#     if N == M:
#         min_count = count
#     else:
#         if N < M:
#             solution(N*2, count+1, 2)
#             if previous != -1:
#                 solution(N+1, count+1, 1)
#         if previous != 1:
#             solution(N-1, count+1, -1)
#         solution(N-10, count+1, 10)
#
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     min_count = abs(M - N)
#     if M > N:
#         solution(N, count=0, previous=0)
#     elif M < N:
#         solution(M, count=0, previous=0)
#     else: # 만약 M == N일 경우에
#         print(f"#{test_case} 0")
#     print(f"#{test_case} {min_count}")
#

from collections import deque
def bfs():
    queue = deque([(S, 0)])
    visited = set()
    visited.add(S)
    while queue:
        N, count = queue.popleft()
        if N == E:
            print(f"#{test_case} {count}")
            return
        for x in ((N*2, N+1, N-1, N-10)):
            if 0 < x <= 1000000 and x not in visited:
                visited.add(x)
                queue.append((x, count+1))

T = int(input())
for test_case in range(1, T+1):
    S, E = map(int, input().split())
    bfs()