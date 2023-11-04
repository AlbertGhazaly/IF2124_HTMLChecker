from myClass import Transition, PDA

def parseFile(filedir):
    with open(f"{filedir}", "r") as file:

        content = file.readlines()
        content = [line.rstrip('\n') for line in content]

        pdaType =  content[0].rstrip(" ")
        states = [element for element in content[1] if element != " "]
        alphabet = [element for element in content[2] if element != " "]
        stackSymbol = [element for element in content[3] if element != " "]
        startState = content[4].rstrip(" ")
        startStack = content[5].rstrip(" ")

        if pdaType == "F": # PDA by Accepted State
            acceptedStates = [element for element in content[6] if element != " "]
            startIdx = 7
        else: # PDA by Empty Stack
            startIdx = 6

        transitions = []

        for i in range(startIdx, len(content)):

            iState = content[i][0].rstrip(" ")
            read = content[i][2].rstrip(" ")
            pop = content[i][4].rstrip(" ")
            fState = content[i][6].rstrip(" ")
            push = content[i][8:].rstrip(" ")

            transition = Transition(iState, read, pop, fState, push)
            transitions.append(transition)
        
        if pdaType == "F": # PDA by Accepted State
            return PDA(states, alphabet, stackSymbol, transitions, startState, startStack, acceptedStates)
        else: # PDA by Empty Stack
            return PDA(states, alphabet, stackSymbol, transitions, startState, startStack)

# contoh parsing PDA by Empty Stack
print("PDA by Empty Stack")
P = parseFile("txt/pda_empty.txt")

print(P)
for t in P.transitions:
    print(t)

print()

# contoh parsing PDA by Accepted State
print("PDA by Accepted State")
P = parseFile("txt/pda_acceptedstates.txt")

print(P)
for t in P.transitions:
    print(t)