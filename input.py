from dfa import FA
from variable import*


print("Enter the automaton states separated by space: ", end="")
states = input().split()

print("Enter the automaton alphabets separated by space: ", end="")
alphabets = input().split()

print("Enter the start state of the automaton: ", end="")
start_state = input()

print("Enter the accepting states of the automaton separated by space: ", end="")
accept_states = input().split()
 

print("Enter the next states for the following (enter . for dead/reject state)")
for state in states:

    transition_function[state] = {}
    
    for alpha in alphabets:  
        print(f"\t  {alpha}")
        print(f"{state}\t---->\t", end="")
        dest = input()
    
        # Rejected states are represented as None in the dictionary
        if dest == ".":
            transition_function[state][alpha] = None
        else:
            transition_function[state][alpha] = dest


print("Enter the input string to run the automaton: ", end="")
input_string = input()


dfa = FA(states,alphabets,transition_function,start_state,accept_states)

if(dfa.is_accepted(input_string)):
    print("Accept")
else:
    print("Reject")

# print(dfa.is_deterministic)

# print("The transition function is:")
# for state in transition_function:
#     print("q{}: {}".format(state, transition_function[state]))

   
