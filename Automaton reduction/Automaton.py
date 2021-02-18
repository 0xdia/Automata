#!/usr/bin/env python3

class Automaton:
  """
    Defintion de la structure d'un automate d'états finis, simple et déterministe
  """

  def __init__(self, X, S, S0, F, I):
    self.X  = X   # L'alphabet
    self.S  = S   # Le nombre d'états
    self.S0 = S0  # L'état initial
    self.I  = I
    self.F = F

    self.final_states = [False for _ in range(S)]
    for f in F:
      self.final_states[f] = True

    self.transitions_table = [[] for _ in range(S)]
    for instruction in I:
      self.transitions_table[instruction[0]].append((instruction[1], instruction[2]))

  def print_parameters(self):
    print(f'X = {self.X}')
    print(f'|S| = {self.S}')
    print(f'S0  = {self.S0}')
    print(f'F = {self.F}')
    print('Set of instructions:')
    for i in self.I:
      print(i)
    
    self.print_transitions_table()

  def print_transitions_table(self):
    print("Transitions table:")
    print(end='    ')
    for x in self.X:
      print(end=f'  {x}')
    print()
    
    for i in range(self.S):
      if i == self.S0:
        print(end='s: ')
      else:
        print(end='   ')

      print(i, end='')
      for x in self.X:
        Found = False
        for t in self.transitions_table[i]:
          if t[0] == x:
            print(end=f'  {t[1]}')
            Found = True
            break
        if not Found:
          print(end='  -')
      print()
    print()

  def is_accessible(self, state):
    """ Vérifie si un état est accessible """
    if state == self.S0:
      return True

    current_states = [self.S0]
    for _ in range(self.S):
      next_states = []
      for current_state in current_states:
        for next_state in self.transitions_table[current_state]:
          if state == next_state[1]:
            return True

          if not (next_state[1] in next_states):
            next_states.append(next_state[1])

      current_states = next_states

    return False
       
  def is_co_accessible(self, state):
    """ Vérifie si un état est accessible """
    if self.final_states[state]:
      return True

    current_states = [state]
    for _ in range(self.S):
      next_states = []
      for current_state in current_states:
        for next_state in self.transitions_table[current_state]:
          if self.final_states[next_state[1]]:
            return True
          
          if not (next_state[1] in next_states):
            next_states.append(next_state)
      current_states = next_states

    return False


  def reduce(self):
    """ Donne un automate équivalent et réduit """
    accessible_states    = [False for _ in range(self.S)]
    co_accessible_states = [False for _ in range(self.S)]

    for stt in range(self.S):
      accessible_states[stt]     = self.is_accessible(stt)
      co_accessible_states[stt]  = self.is_co_accessible(stt)

    assert(accessible_states[self.S0] and co_accessible_states[self.S0]), print("L'automate est invalide")

    F, I = [], []
    S = 0

    for f in range(self.S):
      if self.final_states[f] and accessible_states[f] and co_accessible_states[f]:
        F.append(f)
    
    for s in range(self.S):
      if accessible_states[s] and co_accessible_states[s]:
        S += 1

    for i in self.I:
      if not (accessible_states[i[0]] and co_accessible_states[i[0]]):
        continue
      if not (accessible_states[i[2]] and co_accessible_states[i[2]]):
        continue

      I.append(i)

    return Automaton(self.X, S, self.S0, F, I) 
    


