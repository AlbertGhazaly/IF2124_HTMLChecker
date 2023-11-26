from sys import argv as argv
from html_parser import readHtml, readHtmlList
from pda_parser import PDA, STACK
from pda_parser import read_pda

pda_path = "pda/pda.txt"

pda = read_pda(pda_path)
stack = STACK(pda)

states = set()
counter = 1

f = open("listRules.txt", "w", encoding="utf-8")

keys = pda.transition_rules.keys()
for key in keys:
    val = f"{counter}. {key[0]} {key[1]} {key[2]} <=> {pda.transition_rules[key][0]} {pda.transition_rules[key][1]} {pda.transition_rules[key][2][::-1]}\n"
    states.add(key[0])
    counter += 1
    print(counter)
    f.write(val)
f.close()


# print(len(keys))
# print(states)
print(len(states))


# while True:
#     state = input("state: ")

#     for key in keys:
#         if key[0] == state:
#             print(key, pda.transition_rules[key])