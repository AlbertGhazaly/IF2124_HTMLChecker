class pda:
    def __init__(self, states, symbols, stacksymbol, start_state, transition_rules):
        self.states = states
        self.symbols = symbols
        self.stacksymbol = stacksymbol
        self.start_state = start_state
        self.transition_rules = transition_rules

def read_pda(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()

        states = content[0].split()
        symbols = content[1].split()
        stacksymbol = content[2].split()
        startstate = content[3]
        transition_rules = []

        for i in range(4, len(content)):
            transition_rule = content[i].split()
            transition_rule = {(transition_rule[0], transition_rule[1], transition_rule[2]): (transition_rule[3], transition_rule[4], transition_rule[5])}
            transition_rules.append(transition_rule)

        return pda(states, symbols, stacksymbol, startstate, transition_rules)



filepath = "pda/pda.txt"
pda = read_pda(filepath)

tr = pda.transition_rules
for element in tr:
    print(element)