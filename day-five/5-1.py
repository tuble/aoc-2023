import re
import sys 

seeds_pat = r"seeds:\s*(\d+(?:\s+\d+)*)"
map_range_pat = r"(\d+)\s+(\d+)\s+(\d+)" 
maps = {}
map_idx = 0
with open("input.txt") as data:
        first_line = data.readline()
        # Extract numbers
        match = re.search(seeds_pat, first_line)
        if match:
                seeds =  list(map(int, match.group(1).split()))
        
        mode = 0
        # map SRC - DEST
        # INPUT DEST - SRC
        for l in data:
                if mode and not (l == "\n"):
                        print(l)
                        match = re.match(map_range_pat, l)
                        if match:
                                if map_idx not in maps.keys():
                                        maps[map_idx] = {}

                                dst_range_start, src_range_start,\
                                        range_len = map(int, match.groups())

                                # Add entry for start and end (calculate end number (start+range-1))
                                # Check if number in start <= num <= end 
                                for i in range(range_len):
                                        maps[map_idx][(src_range_start + i)] = (dst_range_start + i)

#                                print(f"Dict for {map_idx} --   {maps[map_idx]}")

                        print(f"dst_range_start {dst_range_start} src_range_start {src_range_start} range_len {range_len}")


                # count times we ve encountered "map" to use it as an index
                if "map" in l: # go to fill map mode
                        mode = 1
                        map_idx += 1
#                        print(f"for map {map_idx}::")
                        continue
                # once l == "\n" exit fill map mode
                if l == "\n": 
                        mode = 0
                        continue

print(f"Seeds: {seeds}")

#for k in maps[1].keys():
#        print(f"{k} - - - {maps[1][k]}")

lowest_location = sys.maxsize
for s in seeds:
        NUM = s
        print(f"SEED IS {NUM}")
        for i in range(0, map_idx): 
                if NUM in maps[i+1].keys():
                        print(f"i: {i+1} for {NUM} --> {maps[i+1][NUM]}")
                        NUM = maps[i+1][NUM]
                else:
                        print(f"i: {i+1} for {NUM} --> {NUM}")
                        NUM = NUM

        if NUM < lowest_location:
                lowest_location = NUM

print(f"Lowest location is {lowest_location}")
