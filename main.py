from sys import argv as argv
from html_parser import readHtml
from pda_parser import pda, Stack
from pda_parser import read_pda

pda_path = argv[1]
html_path = argv[2]

html = readHtml(html_path)
print(html)

pda = read_pda(pda_path)
stack = STACK(pda)

check = True
keys = pda.transition_rules.keys()

while check:

    currState = stack.state

    currChar = html[0]
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

if stack.isEmpty:
    print("Accepted")
else:
    print("Not Accepted")

