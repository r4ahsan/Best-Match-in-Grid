from sess1q3subgrid import *
from grids import *

## mismatch_count(grid_1, grid_2) counts the number of mismatches in the
## two grids grid_1 and grid_2
## mismatch_count: Grid Grid -> Nat
## Requires: Grid_1 and Grid_2 must be non-empyt and
##           both grids must be of same dimension

def mismatch_count(grid_1, grid_2):
    num_row = grid_1.rows
    num_col = grid_1.cols
    count = 0
    for i in range(num_row):
        for j in range(num_col):
            if grid_1.access(i,j) != grid_2.access(i,j):
                count += 1
    return count


## best_match(pattern, target) finds the subgrid of target which has the same
## dimension as pattern and has the minimum number of mismatches and returns a
## list of size 2 containing the row and column numbers of the top left corner
## of the location of the subgrid
## best_match: Grid Grid -> (listof Int)
## Requires : Numbers of rows and columns of the pattern is smaller than or 
##            that of the target
def best_match(pattern, target):
    p_row = pattern.rows
    p_col = pattern.cols
    num_mismatch = p_row * p_col
    position = [0,0]
    r = 0
    while r <= target.rows - p_row:
        c = 0
        while c <= target.cols - p_col:
            sub_grid = subgrid(target, r, r + p_row-1, c, c + p_col-1)
            p = mismatch_count(pattern, sub_grid)
           
            if num_mismatch >= p:
                position = [r,c]
                num_mismatch = p
            c += 1
        r += 1
    return position

