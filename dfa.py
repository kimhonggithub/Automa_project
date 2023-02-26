class FA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transition(self, state, symbol):
        return self.transition_function[state][symbol]
    #De
    def is_deterministic(self):
        for state in self.states:
            for symbol in self.alphabet:
                if len(self.transition_function[state][symbol])>1:
                    return False
        return True

    def is_accepted(self, string):
        current_state = self.start_state
        for symbol in string:
            current_state = self.transition(current_state, symbol)
        return current_state in self.accept_states

