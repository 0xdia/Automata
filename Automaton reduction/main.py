from Automaton import *

if __name__ == '__main__':
  with open('sample_input.txt') as f:
    input_data = f.read().strip().split('\n')
    X = [x for x in input_data[0].split()[1:]]
    S = int(input_data[1].split()[-1])
    S0 = int(input_data[2].split()[-1])
    F = [int(f) for f in input_data[3].split()[1:]]

    I = [i.split(',') for i in input_data[4].split()[1:]]
    I = [(int(i[0]), i[1], int(i[2])) for i in I]

    automaton = Automaton(X, S, S0, F, I)
    automaton.print_parameters()
    print(40 * '-')
#automaton.test()
    equivalent_automaton = automaton.reduce()
    equivalent_automaton.print_parameters()

