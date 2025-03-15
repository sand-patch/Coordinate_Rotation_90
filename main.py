import stdarray, stdio

grid_len = 10
your_grid = stdarray.create2D(grid_len,grid_len,"0")

def populate_grid(grid):
    for row in range(0,grid_len):
        for col in range(0,grid_len):
            grid[row][col] = f"({row+1},{col+1})  "

def print_grid(grid):
    buffer = ""
    for row in range(0,grid_len):
        for col in range(0,grid_len):
            buffer +=  grid[row][col]
        stdio.writeln(buffer)
        buffer = ""
    print("\n")

def rotate_grid(grid):
    buffer_grid = stdarray.create2D(grid_len,grid_len,"0")

    for row in range(0,grid_len):
        for col in range(0,grid_len):
            buffer_grid[col][(grid_len-1) - row] = grid[row][col]

    return buffer_grid

def rotate_n_times(n, grid):
    for i in range(0,n):
        grid = rotate_grid(grid)
    
    return grid

populate_grid(your_grid)
print("Main grid:\n")
print_grid(your_grid)


print("Rotated n Grid:\n")
print_grid(rotate_n_times(2,your_grid))

