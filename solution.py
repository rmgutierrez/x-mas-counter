import sys
WORD = "XMAS"

def count_xmas(grid):
    # Solution for Part 1

    R, C = len(grid), len(grid[0]) if grid else 0
    target = WORD
    L = len(target)
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    total = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] != target[0]:
                continue
            for dr, dc in dirs:
                rr, cc = r, c
                ok = True
                for k in range(1, L):
                    rr += dr
                    cc += dc
                    if not (0 <= rr < R and 0 <= cc < C) or grid[rr][cc] != target[k]:
                        ok = False
                        break
                if ok:
                    total += 1

    return total

def count_x_mas(grid):
    # Solution for part 2
    
    R, C = len(grid), len(grid[0]) if grid else 0
    def is_mas(a,b,c):
        # a-A-c must be M-A-S in either direction
        return (a=='M' and b=='A' and c=='S') or (a=='S' and b=='A' and c=='M')
    total = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            if grid[r][c] != 'A':
                continue
            d1 = is_mas(grid[r-1][c-1], grid[r][c], grid[r+1][c+1])
            d2 = is_mas(grid[r-1][c+1], grid[r][c], grid[r+1][c-1])
            if d1 and d2:
                total += 1
    return total

def read_grid_from_stream(stream):
    data = [line.rstrip("\n") for line in stream if line.strip("\n") != ""]
    return data

def main(argv):
    with open(argv[1], "r") as f:
        grid = read_grid_from_stream(f)
    print(count_xmas(grid))

if __name__ == "__main__":
    main(sys.argv)
