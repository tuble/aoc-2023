import re

nums = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
digs = ("1", "2", "3", "4", "5", "6", "7", "8", "9") 
 
num_to_dig = {"one" : 1,
                 "two": 2,
                 "three": 3,
                 "four": 4,
                 "five": 5,
                 "six" : 6,
                 "seven" : 7,
                 "eight" : 8,
                 "nine": 9,
                "1": 1,
                 "2": 2, "3" : 3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9": 9 }

num_digs = nums + digs

def get_dic_map(l):
        dmap = {}
        for num in num_digs:
                oc = [l.start() for l in re.finditer(num, l)]
                if oc: # kkddrrtskfive75pcmhhxcxzfourthree8 in cases where both the digit and the word is present 
                        print(num + " ============== " + str(oc))
                        if num_to_dig[num] in dmap.keys():
                                dmap[num_to_dig[num]] += oc;
                        else: dmap[num_to_dig[num]] = oc;
        return dmap 
                        

example = ("two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen", "kkddrrtskfive75pcmhhxcxzfourthree8")
'''
for l in example:
        print(l)
        get_dic_map(l)
'''
def min_max(inpu):
        s = 0
        for l in inpu:
                line_dic = get_dic_map(l)
                print("------ " + l + " ---- " , line_dic)
                # dict full k -> digit ; v -> index; find smallest and largest index and assign to value(key)
                min_idx = 256 
                max_idx = -1 
                max_num = min_num = -1
                for num in line_dic:
                        print("digit turned " + str(num)) # digit i need
                        print("digit found at index " + str(line_dic[num])) # list
                        for elem in line_dic[num]:
                                if elem > max_idx:
                                        max_num = num
                                        max_idx = elem
                                if elem < min_idx:
                                        min_num = num
                                        min_idx = elem
                                print("indexes stored " + str(elem))
                print(f"for {l} found max {max_num} ; min {min_num}; num to sum: {min_num}{max_num}")
                if max_num == -1 or min_num == -1: continue
                s += (min_num * 10 + max_num)

                print(f"sum is {s}")
        return s

with open("input.txt") as input_file:
        print("sum is: " + str(min_max(input_file)))
#print("sum is: " + str(min_max(example)))
