from sys import argv as argv
from html_parser import readHtml, readHtmlList
from pda_parser import PDA, STACK
from pda_parser import read_pda

pda_path = argv[1]
html_path = argv[2]

html = readHtml(html_path)
html_List = readHtmlList(html_path)

pda = read_pda(pda_path)
stack = STACK(pda)

check = ((len(html) > 0))
invalid = False

keys = pda.transition_rules.keys()

counterCol = -1
counterRow = 0

newLine = False

while check:

    currState = stack.state
    currChar = html[0]

    if currChar == "$":
        counterRow += 1
        counterCol = -1
    counterCol += 1

    print(f"stack: {stack}")
    print(f"str: {html}")
    print()
    
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
    # print(html_List)
    print()
    print(f"  file \"{html_path}\", line {counterRow+1}")
    print(html_List[counterRow], end="")
    if counterRow+1 == len(html_List):
        print()
    for i in range(counterCol-1):
        print(" ", end="")
    print("^")
    print(f"SyntaxError: kode kamu jelek (detected at line {counterRow+1})")