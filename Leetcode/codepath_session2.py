"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

def transpose(matrix):
    output = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            output[i][j] = matrix[j][i]

    print(output)
    return

transpose(matrix)
