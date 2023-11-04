class Transition:

    def __init__(self, iState, read, pop, fState, push):
        self.iState = iState
        self.read = read
        self.pop = pop
        self.fState = fState
        self.push = push

    def __str__(self):
        return f"δ({self.iState}, {self.read}, {self.pop}) = ({self.fState}, {self.push})"

class PDA:

    def __init__(self, states, alphabet, stackSymbol, transitions, startState, startStack, acceptedStates = None):

        self.states = states
        self.alphabet = alphabet
        self.stackSymbol = stackSymbol
        self.transitions = transitions
        self.startState = startState
        self.startStack = startStack
        self.acceptedStates = acceptedStates

    def __str__(self):

        states = f"{{{', '.join(self.states)}}}"
        alphabet = f"{{{', '.join(self.alphabet)}}}"
        stackSymbol = f"{{{', '.join(self.stackSymbol)}}}"
        transitions = "δ"
        startState = self.startState
        startStack = self.startStack

        if self.acceptedStates != None: # PDA by Accepted States
            acceptedStates = f"{{{', '.join(self.acceptedStates)}}}"
            return f"P({states}, {alphabet}, {stackSymbol}, {transitions}, {startState}, {startStack}, {acceptedStates})"
        else: # PDA by Empty Stack
            return f"P({states}, {alphabet}, {stackSymbol}, {transitions}, {startState}, {startStack})"


if __name__ == "__main__":
    # contoh transition
    t1 = Transition("q", "0", "X", "q2", "XX")
    # print(t1)

    # contoh empty stack pda
    pda1 = PDA(["q0","q1","q2"], ["0","1"], ["X"], [t1], "q0", "#")
    print(pda1)

    # contoh accepted state pda
    pda2 = PDA(["q0","q1","q2"], ["0","1"], ["X"], [t1], "q0", "#", ["q2"])
    print(pda2)

    # contoh transition pada pda, (transition disimpan dalam list)
    print(pda2.transitions[0])
