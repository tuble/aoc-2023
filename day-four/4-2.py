import re
pat = r':\s*(.*?)\s*\|\s*(.*)'

class Card:
        def __init__(__self__, copies):
                __self__.copies = copies
         
        def __string__(self):
                return __self__.copies

# int, card
card_cpys = {}

s = 0
with open("input.txt") as data:
        current_card = 1
        for line in data:
#                print(f"LINE: CURRENT_CARD IS {current_card}")
                next_cards_won = 0
                ex = re.search(pat ,line)

                if ex:       
                        winning_str = ex.group(1).strip()
                        scratched_str = ex.group(2).strip()

                        winning = list(map(int, winning_str.split()))
                        scratched = list(map(int, scratched_str.split()))

                        if current_card not in card_cpys.keys():
                                card_cpys[current_card] = 1 
                                times_won = 1
                        else:
                                times_won = card_cpys[current_card]

                        # findall or similar ... 
                        for num in scratched:
                                if num in winning:
#                                        print(f"{num} is in {winning}!")
                                        next_cards_won += 1

                        # go next_cards_won ahead and win them times_won times
                        for i in range(1, (next_cards_won+1)):
                                next_card = ( current_card + i )
                                if next_card in card_cpys.keys():
                                        card_cpys[next_card] += times_won
                                else:
                                        card_cpys[next_card] = ( 1 + times_won ) # 1 initial  + times_won

                        current_card += 1

# ------ -
total_cards = 0
for card_id, card_copies in card_cpys.items():
        total_cards += card_copies
#        print(f"card with ID {card_id} with copies {card_copies}")

print(f"total PTS: {total_cards}")
