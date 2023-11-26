class PDA:
    def __init__(self, states, symbols, stacksymbols, startstack, startstate, transition_rules):
        self.states = states
        self.symbols = symbols
        self.stacksymbols = stacksymbols
        self.startstate = startstate
        self.startstack = startstack
        self.transition_rules = transition_rules

class STACK:

    def __init__(self, pda):
        self.stack = pda.startstack
        self.state = pda.startstate
        self.top = pda.startstack

    def __str__(self):
        return self.stack

    def isEmpty(self):
        # print(f"stack : |{self}|")
        # print(self.stack == "")
        return self.stack == ""
    
    def stackpush(self,x):
            if x != "ε":
                self.stack += x
                self.top = x[-1]

    def stackpop(self):

        if self.isEmpty():
            self.top = None
            self.stack = ""
        else: 
            if len(self.stack) == 1:
                self.top = ""
                self.stack = ""
            else:
                self.top = self.stack[-2]
                self.stack = self.stack[:-1]

    def do_procedure(self, transition):

        fstate = transition[0]
        pop = transition[1]
        push = transition[2]

        self.state = fstate
        if pop != 'ε':
            self.stackpop()
        self.stackpush(push)


def read_pda(filepath):
    with open(filepath, 'r', encoding="utf-8") as file:
        content = [e.rstrip("\n") for e in file.readlines() if e != "\n" and e[0] != "-"]
        # for row in content:
        #     print(row)
        
        states = content[0].split()
        symbols = content[1].split()
        stacksymbol = content[2].split()
        startstate = content[3]
        startstack = content[4]
        transition_rules = {}

        for i in range(5, len(content)):
            # print(content[i])
            transition_rule = content[i].split()
            # print(transition_rule)
            key = (transition_rule[0], transition_rule[1], transition_rule[2])
            value = (transition_rule[3], transition_rule[4], transition_rule[5][::-1])
            transition_rules[key] = value

        return PDA(states, symbols, stacksymbol, startstate, startstack, transition_rules)