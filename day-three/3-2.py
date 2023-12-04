import re

used_indexes = {}
# fill input matrix
m = []
with open("input.txt") as f:
        for l in f:
                line_list = list(l)
                line_list.pop()
                m.append(line_list)

rows = len(m)
cols = len(m[0])
def valid(r,c):
        if (r < 0 or r >= rows) or (c < 0 or c >= cols): return False
        return True

print(rows, cols) 
#print(m)

#exit()
def digit_at(m, r, c):
        return (valid(r, c) and m[r][c].isnumeric())
#        if not valid(r, c): return False
#        if m[r][c].isnumeric(): 
#                print(f"is digit @ {r} {c} ({m[r][c]})")
#                return True
# SM implementation ?
def extract_num(m, r, c):

#        if r, c range in used_dic --> return 0;

        # ROW does not change, num should be on the same line
        start_idx = c 
        end_idx = c 

#        print(f"starting search with {r} {c}")
        # check L
        loc_c = c - 1 # go L
#        while valid(r, loc_c) and m[r][loc_c] != '.':
        while digit_at(m,r,loc_c):
#                print(f"loc_c is {loc_c}")
                start_idx = loc_c
                loc_c -= 1 
        # check R
        loc_c = c # return to start pos
        loc_c = c + 1  # go R
        # check if is number and valid
#        while valid(r, loc_c) and m[r][loc_c] != '.':
        while digit_at(m,r,loc_c):
#               print(f"loc_c is {loc_c}")
                end_idx = loc_c
                loc_c += 1 

        if r in used_indexes.keys() and [start_idx, end_idx] in used_indexes[r]: 
#                print("A")
                return -1
        else:
#                print("B")
                if r not in used_indexes.keys():
                        used_indexes[r] = []
                used_indexes[r].append([start_idx, end_idx])
#        print(f"Will get num from {start_idx} to {end_idx} on line {r}")
        # get in dic
        return form_num(r, start_idx, end_idx)        

# don't like
def form_num(r, start_idx, end_idx):
        iters = (end_idx - start_idx) + 1 
        num = 0
        tmp = 0
        for it in range(iters):
                i = it
                tmp = int(m[r][start_idx + i])
                while i < (iters-1) :
                        tmp *= 10
                        i += 1
                num += tmp

#        print(f"NUM FORMED {num}")
        return num

def find_num(m, r, c, max_r, max_c):
        gear_ratio = 1
        tmp = 0
        adj_count = 0
        # going clock-wise
        # L UP diag
        cr = r - 1; cc = c - 1
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1
        # L UP
        cr = r - 1; cc = c
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1
        # R UP diag
        cr = r - 1; cc = c + 1
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1
        # R
        cr = r; cc = c + 1
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1
        # R DOWN diag
        cr = r + 1; cc = c + 1
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1
        # R DOWN
        cr = r + 1; cc = c
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1
        # L DOWN diag
        cr = r + 1; cc = c - 1
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1
        # L
        cr = r; cc = c - 1
        if digit_at(m, cr, cc):
                tmp = extract_num(m, cr, cc)
                if (tmp != -1):
                        gear_ratio *= tmp
                        adj_count += 1

#        print(m[r][c], adj_count, gear_ratio)
        if adj_count == 2:
                return gear_ratio
        else:
                return 0

#        return ( adj_count == 2 : gear_ratio ? 0)

# traverse input matrix and find special characters
s = 0
for r in range(rows):
        for c in range(cols):
                current_char = m[r][c]
#                if current_char != '\n' and not current_char.isnumeric() and current_char != ".":
                if current_char == '*':
                        # search for number
#                        print(f"Found gear {current_char} at  {r} {c}")
                        s += find_num(m, r,c, rows, cols)

print("sum is: " + str(s))
'''
        if [start_idx, end_idx] in used_indexes[r]:
                return 0 
        else:
                used_indexes[r].append([start_idx, end_idx])
'''
