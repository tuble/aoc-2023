import re

cubes = {"red": 12, "green": 13, "blue": 14}

with open("input.txt") as data:
        s = 0
        for line in data:
                game_id = re.search(r"Game (\d+):", line)
                game_id = int(game_id.group(1))
#                print(f"current game: {game_id}")
                print(f"current input {line}")
                deal = line.split(':')[1]
                deal_dic = {}
                for m in re.finditer(r"(\d+) (\w+)", deal):
                        current_val, current_col  = m.groups()
                        print(current_val, str(current_col))
                        if int(current_val) > int(cubes[current_col]):
#                                print(f"yes {current_val} IS GREATER THAN > {cubes[current_col]} for color: {current_col}")
                                s += game_id
                                print(f"game {game_id} is NOT possible!")
                                break

#                        print(f"{current_val} >? {cubes[current_col]} for color: {current_col}")
#                       if current_col in deal_dic.keys():
#                                deal_dic[str(current_col)] += int(current_val)
#                        else: deal_dic[str(current_col)] = int(current_val)
                # After deal_dic full in deal
#                for c in cubes:
#                        if deal_dic[c] > cubes[c]:
#                                s += game_id
#                                print(f"game {game_id} is NOT possible!")
#                                break
        print(f"sum of YES possible games: {5050 - s}")
'''
                        if int(current_val) > int(cubes[current_col]):
#                                print(f"yes {current_val} IS GREATER THAN > {cubes[current_col]} for color: {current_col}")
                                s += game_id
                                print(f"game {game_id} is NOT possible!")
                                break
'''


#                combs = line.split(':')[1]
#                combs = combs.split(';')
#                print(combs)
