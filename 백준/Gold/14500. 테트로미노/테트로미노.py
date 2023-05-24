import sys


def match(matrix, sr, sc):
    tetromino = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                 [(0, 0), (1, 0), (2, 0), (3, 0)],
                 [(0, 0), (1, 0), (0, 1), (1, 1)],
                 [(0, 0), (1, 0), (2, 0), (2, 1)],
                 [(0, 1), (1, 1), (2, 1), (2, 0)],
                 [(0, 0), (0, 1), (1, 1), (2, 1)],
                 [(0, 0), (0, 1), (1, 0), (2, 0)],
                 [(0, 0), (1, 0), (1, 1), (1, 2)],
                 [(0, 2), (1, 1), (1, 2), (1, 0)],
                 [(0, 0), (0, 1), (0, 2), (1, 2)],
                 [(0, 0), (1, 0), (0, 1), (0, 2)],
                 [(0, 0), (1, 0), (1, 1), (2, 1)],
                 [(0, 1), (1, 1), (1, 0), (2, 0)],
                 [(1, 0), (1, 1), (0, 1), (0, 2)],
                 [(0, 0), (0, 1), (1, 1), (1, 2)],
                 [(0, 1), (1, 0), (1, 1), (1, 2)],
                 [(0, 0), (0, 1), (0, 2), (1, 1)],
                 [(0, 0), (1, 0), (1, 1), (2, 0)],
                 [(0, 1), (1, 1), (1, 0), (2, 1)]]
    max_val = 0
    for tet in tetromino:
        elem = []
        for t in tet:
            elem.append(tuple(map(sum, zip((sr, sc), t))))
        sum_val = 0
        for er, ec in elem:
            if not (0 <= er < N and 0 <= ec < M):
                break
            sum_val += matrix[er][ec]
        max_val = max(max_val, sum_val)
    return max_val


def find_max(matrix):
    max_val = -1
    for i in range(N):
        for j in range(M):
            max_val = max(max_val, match(matrix, i, j))
    return max_val


N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(find_max(matrix))
