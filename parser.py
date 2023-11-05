from myclass import Transition, PDA, String

def parseFilePDA(filedir):
    with open(f"{filedir}", "r", encoding="utf-8") as file:

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

            transition = content[i].split()
            iState = transition[0]
            read = transition[1]
            pop = transition[2]
            fState = transition[3]
            push = transition[4]

            transition = Transition(iState, read, pop, fState, push)
            transitions.append(transition)
        
        if pdaType == "F": # PDA by Accepted State
            return PDA(states, alphabet, stackSymbol, transitions, startState, startStack, acceptedStates)
        else: # PDA by Empty Stack
            return PDA(states, alphabet, stackSymbol, transitions, startState, startStack)


def parseFileHTML(filedir):
    with open(f"{filedir}", "r", encoding="utf-8") as file:

        content = file.readlines()
        content = [line.rstrip('\n') for line in content]

        string = ""
        for row in content:
            for char in row:
                if char != " ":
                    string += char.lower()
        
        return String(string)

if __name__ == "__main__":

    # contoh parsing file PDA by Empty Stack
    print("PDA by Empty Stack")
    P = parseFilePDA("txt/pda_empty.txt")

    print(P)
    for t in P.transitions:
        print(t)

    print()

    # contoh parsing file PDA by Accepted States
    print("PDA by Accepted States")
    P = parseFilePDA("txt/pda_acceptedstates.txt")

    print(P)
    for t in P.transitions:
        print(t)
    
    print()

    # contoh parsing file HTML
    print("String")
    String = parseFileHTML("txt/html.txt")
    print(String)