import re

with open("input.txt") as data:
        prod = 0
        for line in data:
                game_id = re.search(r"Game (\d+):", line)
                game_id = int(game_id.group(1))
#                print(f"current game: {game_id}")
                print(f"current input {line}")
                deal = line.split(':')[1]
                colors_max_needed = {"red": 0, "green": 0, "blue": 0}
                for m in re.finditer(r"(\d+) (\w+)", deal):
                        current_val, current_col  = m.groups()
                        current_val = int(current_val)
                        print(current_val, str(current_col))
                        if colors_max_needed[current_col] < int(current_val):
                                print(f"game {game_id} {colors_max_needed[current_col]} was < {current_val} :: REPLACED")
                                colors_max_needed[current_col] = int(current_val)

                print(colors_max_needed)
                p = 1
                # one-liner ? : ( 
                for key in  colors_max_needed:
                        p *= colors_max_needed[key]
                print(f"PROD of maxes: {p}")

                prod += p

        print(f"SUM of all Prods: {prod}")
