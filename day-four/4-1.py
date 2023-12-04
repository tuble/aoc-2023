import re
pat = r':\s*(.*?)\s*\|\s*(.*)'

#def get_lists(winning, scratched):
with open("input.txt") as data:
        s = 0
        for line in data:
                mul = 0
                ex = re.search(pat ,line)
                if ex:       
                        winning_str = ex.group(1).strip()
                        scratched_str = ex.group(2).strip()

                        winning = list(map(int, winning_str.split()))
                        scratched = list(map(int, scratched_str.split()))
#                        print(f"W {winning}")
#                        print(f"S {scratched}")
                        for num in scratched:
#                                print(f"list is {winning}, num is {num}")
                                if num in winning:
                                        # >:(
                                        if mul == 0: mul = 1
                                        else: mul *= 2

                        s += mul
                        print(f"Card is worth {mul} pts.. total pts = {s}")

print(f"total PTS: {s}")
