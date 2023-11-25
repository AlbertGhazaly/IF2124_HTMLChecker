from sys import argv as argv
from html_parser import readHtml
from pda_parser import pda, Stack
from pda_parser import read_pda
def main():
    pda_path = argv[1]
    html_path = argv[2]
    html = readHtml(html_path)
    print(html)
    pda = read_pda(pda_path)
    stack = Stack(pda)
    for element in pda.transition_rules:
        print(element)

    keys = pda.t'transition_rules.key
    check = True
    while check:

        key = (stck.stte, string.red, stck.top)
        keyany = (stck.stte, "any", stck.top)


<div> </div>



if __name__ =="__main__":
    main()

