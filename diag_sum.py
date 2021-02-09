mat = [[1,2,3],
      [4,5,6],
      [7,8,9]
       ]

rows = len(mat)
diag_sum = 0
right = rows - 1
for i in range(0, rows):
    # print(mat[i][i])
    # print(mat[i][right])
    diag_sum += (mat[i][i] + mat[i][right])
    right -= 1
if rows % 2 == 1:
    middle = int((rows - 1) / 2)
    diag_sum -= mat[middle][middle]
print(diag_sum)

