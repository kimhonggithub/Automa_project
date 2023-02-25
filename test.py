from demo import FA

# 5-tuple collection
states = []
alphabets = []
start_state = ""
accept_states = []
transition = {}

# Input which the DFA will accept/reject
input_string = ""



# The states and input alphabest will be represented as a list of strings
print("Enter the automaton states separated by space: ", end="")
states = input().split()

print("Enter the automaton alphabets separated by space: ", end="")
alphabets = input().split()

# Start and accepted states
print("Enter the start state of the automaton: ", end="")
start_state = input()

print("Enter the accepting states of the automaton separated by space: ", end="")
accept_states = input().split()

# Transition function is a dictionary where
#   key = (current_state, input)
#   value = next_state  (None for rejected states)
print("Enter the next states for the following (enter . for dead/reject state)")
for state in states:
    for alpha in alphabets:
        print(f"\t  {alpha}")
        print(f"{state}\t---->\t", end="")
        dest = input()
        
        # Rejected states are represented as None in the dictionary
        if dest == ".":
            transition[(state, alpha)] = None
        else:
            transition[(state, alpha)] = dest


print("Enter the input string to run the automaton: ", end="")
input_string = input()

# Start parsing the input string with the current state as start state
current_state = start_state

dfa = FA(states,alphabets,transition,current_state,accept_states)

print(dfa.is_accepted(input_string))
   
