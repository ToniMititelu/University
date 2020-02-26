'''
Convert NFA to DFA
The NFA is given as:
- no of states
- states
- no of symbols
- symbols
- initial state
- no of final states
- final states
- transitions

'''

import queue

file = open("input.txt", "r")

nfa_num_states = int(file.readline())

line = file.readline().split(" ")
nfa_states = []
for i in line:
	if i != '\n':
		nfa_states.append(int(i))

nfa_num_symbols = int(file.readline())

line = file.readline().split(" ")
nfa_symbols = []
for i in line:
	if i != '\n':
		nfa_symbols.append(i)

nfa_first_state = int(file.readline())
nfa_num_finals = int(file.readline())

line = file.readline().split(" ")
nfa_finals = []
for i in line:
	if i != '\n':
		nfa_finals.append(int(i))

nfa_transitions = {}
nfa_num_transitions = int(file.readline())
for i in range(nfa_num_transitions):
	line = file.readline().split(" ")
	state_a = int(line[0])
	symbol = line[1]
	state_b = int(line[2])
	if (state_a, symbol) in nfa_transitions:
		nfa_transitions[(state_a, symbol)].append(state_b)
	else:
		nfa_transitions[(state_a, symbol)] = [state_b]

file.close()

X = [nfa_first_state]
q = queue.Queue(maxsize=0)
q.put(X)
viz = []
dfa_tranz = []
dfa_states = []
dfa_final_states = []

print(nfa_symbols)

while q.empty() != True:
	elem = q.get()
	viz.append(elem)
	for symbol in nfa_symbols:
		T = []
		for state in elem:
			if (state, symbol) in nfa_transitions:
				for i in nfa_transitions[(state, symbol)]:
					if i not in T:
						T.append(i)
		transition_function = (elem, symbol, T)
		sorted_transition1 = transition_function[0]
		sorted_transition1.sort()
		sorted_transition2 = transition_function[2]
		sorted_transition1.sort()
		new_transition_function = (sorted_transition1, symbol, sorted_transition2)
		if sorted_transition1 and sorted_transition2 and new_transition_function not in dfa_tranz:	
			dfa_tranz.append(new_transition_function)
		T.sort()
		if T not in viz:
			q.put(T)

k = 1
redenumire = {}
for multime in viz:
	redenumire[tuple(multime)] = k
	k += 1

for item in redenumire:
	print(redenumire[item])

for transition in dfa_tranz:
	sorted_transition1 = transition[0]
	sorted_transition1.sort()
	if sorted_transition1 not in dfa_states:
		dfa_states.append(sorted_transition1)
	sorted_transition2 = transition[2]
	sorted_transition2.sort()
	if sorted_transition2 not in dfa_states:
		dfa_states.append(sorted_transition2)
	for state in nfa_finals:
		if state in sorted_transition1 and sorted_transition1 not in dfa_final_states:
			dfa_final_states.append(sorted_transition1)
		if state in sorted_transition2 and sorted_transition2 not in dfa_final_states:
			dfa_final_states.append(sorted_transition2)

dfa_first_state = [nfa_first_state]
dfa_num_states = len(dfa_states)
dfa_num_finals = len(dfa_final_states)
dfa_num_transitions = len(dfa_tranz)

file_out = open("output.txt", "w")
file_out.write(str(dfa_num_states) + "\n")
for state in dfa_states:
	file_out.write(str(redenumire[tuple(state)]) + " ")
file_out.write("\n" + str(nfa_num_symbols) + "\n")
for symbol in nfa_symbols:
	file_out.write(str(symbol) + " ")
file_out.write("\n" + str(redenumire[tuple(dfa_first_state)]))
file_out.write("\n" + str(dfa_num_finals) + "\n")
for state in dfa_final_states:
	file_out.write(str(redenumire[tuple(state)]) + " ")
file_out.write("\n" + str(dfa_num_transitions) + "\n")
for transition in dfa_tranz:
	file_out.write(str(redenumire[tuple(transition[0])]) + " " + transition[1] + " " + str(redenumire[tuple(transition[2])]) + "\n")
file_out.close()

