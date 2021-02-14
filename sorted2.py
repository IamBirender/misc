matrix = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17,18,19,20]]
print("original matrix")
for m in matrix:
    print(m)

borders_list = list()

def get_border(matrix):
    if len(matrix) == 0:
        return 
    R, C = len(matrix), len(matrix[0])
    result = list()
    for i in range(R):
        for j in range(C):
            if i == 0 or i == R-1 or j == 0 or j == C-1:
                result.append(matrix[i][j])
    borders_list.append(result)
    new_matrix = [m[1:-1] for m in matrix[1:-1]]
    get_border(new_matrix)
    
get_border(matrix)
borders_list = [sorted(l) for l in borders_list]
new_mat = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

def get_new_matrix(new_mat, x, y, borders_list):
    if x == len(borders_list):
        return new_mat
    
    for j in range(y, len(new_mat[0])-y):
        new_mat[x][j] = borders_list[x].pop(0)
    
    for i in range(x+1, len(new_mat)-x-1):
        new_mat[i][len(new_mat[0])-y-1] = borders_list[x].pop(0)
    
    for j in range(len(new_mat[0])-y-1, y-1, -1):
        new_mat[len(new_mat)-x-1][j] = borders_list[x].pop(0)
    
    for i in range(len(new_mat)-x-2, x, -1):
        new_mat[i][y] = borders_list[x].pop(0)
        
    
    get_new_matrix(new_mat, x+1, y+1, borders_list)
    return 

get_new_matrix(new_mat, 0, 0, borders_list)
print("after matrix")
for m in new_mat:
    print(m)
