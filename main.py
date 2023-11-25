from sys import argv as argv
from html_parser import readHtml
from pda_parser import PDA, STACK
from pda_parser import read_pda

pda_path = argv[1]
html_path = argv[2]

html = readHtml(html_path)

pda = read_pda(pda_path)
stack = STACK(pda)

check = ((len(html) > 0))
invalid = False

keys = pda.transition_rules.keys()

while check:

    currState = stack.state
    currChar = html[0]

    # print(f"stack: {stack}")
    # print(f"str: {html}")
    # print()
    
    if len(html) == 1:
        check = False
        html = ""
    else:
        html = html[1:]

    currTop = stack.top

    key = (currState, currChar, currTop)
    keyAny = (currState, "any", currTop)

    if key in keys:
        stack.do_procedure(pda.transition_rules[key])
        # print(f"rules: {pda.transition_rules[key]}")
        # print(" ")

    elif keyAny in keys:
        stack.do_procedure(pda.transition_rules[keyAny])
    else:
        check = False
        invalid = True
    
    # print(f"\nstack: {stack}")
    # print(f"str: {html}")
    # print(f"read: {currChar}")
    # print(f"state: {stack.state}")

currState = stack.state
key = (currState, "any", "#")
if key in keys:
        stack.do_procedure(pda.transition_rules[key])

print(f"\nstack: {stack}")
print(f"str: {html}")
print(f"read: {currChar}")
print(f"state: {stack.state}")
# print(pda.transition_rules[key])

if stack.top == "#" and len(html) == 0 and not(invalid):
    print("\nAccepted!\n")
else:
    print("\nNot Accepted :(\n")

