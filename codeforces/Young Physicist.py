class Matrix:
    def __init__(self, n):
        self.n = n
        self.matrix = []
        
    def set_matrix(self):
        for i in range (0, self.n):
            x, y, z = map(int, input().split())
            self.matrix.append([x, y, z])
            
    def get_matrix(self):
        return self.matrix
        
    def solve(self):
        saver_x = 0
        saver_y = 0
        saver_z = 0
        for m in self.matrix:
            saver_x = saver_x + m[0]
            saver_y = saver_y + m[1]
            saver_z = saver_z + m[2]
        
        if saver_x == 0 and saver_y == 0 and saver_z == 0:
            return True
        else:
            return False


n = int(input())
M1 = Matrix(n)
M1.set_matrix()
resault = M1.solve()
if(resault == True):
    print("YES")
else:
    print("NO")
