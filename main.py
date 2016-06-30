print ("hello")

main = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]

f = [
[-1,-1,-1],
[-1,8,-1],
[-1,-1,-1],
]

main_row = len(main)
main_line=len(main[1])

arr = [[0 for i in range(main_line)] for j in range(main_row)]
tmp = 0

for r in range(main_row):
    for l in range(main_line):
        if main[r][l] == 1:
            arr[r-1][l-1] = arr[r-1][l-1] + f[0][0]
            arr[r-1][l] = arr[r-1][l] + f[0][1]
            arr[r-1][l+1] = arr[r-1][l+1] + f[0][2]
            arr[r][l-1] = arr[r][l-1] + f[1][0]
            arr[r][l] = arr[r][l] + f[1][1]
            arr[r][l+1] = arr[r][l+1] + f[1][2]
            arr[r+1][l-1] = arr[r+1][l-1] + f[2][0]
            arr[r+1][l] = arr[r+1][l] + f[2][1]
            arr[r+1][l+1] = arr[r+1][l+1] + f[2][2]

for a in range(main_row):
    for b in range(main_line):
        if arr[a][b] >= 1:
            arr[a][b] = 1
        else:
            arr[a][b] = 0

for t in range(main_row):
    print(arr[t])
