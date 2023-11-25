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
keys = pda.transition_rules.keys()

while check:

    print(stack)
    print(html)

    currState = stack.state

    currChar = html[0]

    if len(html) == 1:
        check = False
    else:
        html = html[1:]

    currTop = stack.top

    key = (currState, currChar, currTop)
    keyAny = (currState, "any", currTop)

    if key in keys:
        stack.do_procedure(key)
    elif keyAny in keys:
        stack.do_procedure(keyAny)
    else:
        check = False

if stack.isEmpty and len(html) == 0:
    print("Accepted")
else:
    print("Not Accepted")

