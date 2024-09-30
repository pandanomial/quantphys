# https://www.programiz.com/python-programming/online-compiler/
# use this online compiler, copy my code then run it
# Quantum Physics - Statistical Mechanics - Maxwell–Boltzmann distribution
# Author: Stephanie Zhang
# https://github.com/pandanomial


'''
Physics 4D
Statistical Mechanics
PS4-2
1. Six identical but distinguishable particles share seven units of energy.
Each particle can have energy only in integral amounts.
Create a table that lists all possible macrostates and for each macrostate
compute its multiplicity.
'''


# You can update NUM_OF_PARTICLES and NUM_OF_ENERGY as needed, eg
NUM_OF_ENERGY = 7
NUM_OF_PARTICLES = 6


# DO NOT change any code below

# total macrostates
macrostates = 0
# total microstates
microstates = 0
# temp holding each macrostate detailed info
macrostate_dict = {}
# holds all macrostates detailed info
total_macrostates_dict = {}




# for students who don't know python or don't know how to install
# any libraries. I wrote this factorial function for students' convince
def factorial(n):
    fact = 1
    for i in range(1, n+1):
      fact = fact * i
    return fact






# If the object is a dictionary, create a new dictionary and recursively copy its contents
def deep_copy(obj):
    #if isinstance(obj, dict):
    new_dict = {}
    for key, value in obj.items():
        new_dict[key] = value
    return new_dict






# Maxwell–Boltzmann distribution in visual presentation:
# each star * represents each particle
def format_distribution(macrostate_dict):

  rows = []

  for n in range(NUM_OF_ENERGY, -1, -1):
    e_level = f"\033[92m{n}|\033[0m"
    row = [str(e_level)]
    #row.append('\033[94mThis is blue text\033[0m')

    stars = macrostate_dict[n]
    for i in range(NUM_OF_PARTICLES):
      if i < stars:
        # ANSI escape code for colored text
        # print("\033[91mThis is red text\033[0m")
        row.append('\033[91m*\033[0m')
      else:
        # ANSI escape code for colored text
        # print("\033[92mThis is green text\033[0m")
        row.append('\033[92m-\033[0m')

    row.append(f"\033[92m|\033[0m Energy level = \033[92m{n}\033[0m")
    row.append(f", Particles at this level = \033[91m{stars}\033[0m")
    rows.append(' '.join(row))
  return '\n'.join(rows)





# total macrostates saved in variable macrostates
def solve_macrostates(index, energy_sum, particle_sum):
    global macrostates

    if index == NUM_OF_ENERGY + 1:

        # for print out microstates of each macrostate
        str_microstate = ''
        for i in range(NUM_OF_ENERGY + 1):
          if i < NUM_OF_ENERGY:
              str_microstate = str_microstate + str(macrostate_dict[i]) + '! * '
          else:
              str_microstate = str_microstate + str(macrostate_dict[i]) + '!'

        # for calculating actuarial microstates of each macrostate
        int_microstate = factorial(NUM_OF_PARTICLES)
        for i in range(NUM_OF_ENERGY + 1):
            int_microstate = int(int_microstate / factorial(macrostate_dict[i]))

        # Recursive: Base case to check if the current configuration meets the conditions
        if energy_sum == NUM_OF_ENERGY and particle_sum == NUM_OF_PARTICLES:
            macrostates += 1
            print('\n\n\n\n\n\n')
            print(f"Macrostate # {macrostates}")
            print(format_distribution(macrostate_dict))
            print("\033[1;35m")
            print(f"                             {NUM_OF_PARTICLES}!")
            print("Microstates = --------------------------------------------")
            print('                ' + str_microstate)
            print(f"Microstates = {int_microstate}\033[0m")
            print()
            total_macrostates_dict[macrostates] = deep_copy(macrostate_dict)

        return

    # Try all possible values for macrostate_dict[index]
    for value in range(NUM_OF_ENERGY):
        macrostate_dict[index] = value
        # Recursively solve for the next index
        solve_macrostates(index + 1, energy_sum + macrostate_dict[index] * index,
                          particle_sum + macrostate_dict[index])







# total microstates saved in microstates
def total_microstates():
    global microstates
    microstates = factorial(NUM_OF_ENERGY + NUM_OF_PARTICLES - 1)/factorial(NUM_OF_ENERGY)/factorial(NUM_OF_PARTICLES - 1)

    print("\033[1;35m                         (NUM_OF_ENERGY + NUM_OF_PARTICLES - 1)!")
    print("Total Microstates = -------------------------------------------------")
    print("                         (NUM_OF_ENERGY!) * (NUM_OF_PARTICLES - 1)!")
    print()
    print(f"Total Microstates = {int(microstates)}\033[0m")





# print out again
def print_total_macrostates_dict(total_macrostates_dict):
    for key, value in total_macrostates_dict.items():
        print(key, value)




# print out tables
def display_probabilities():
    print("You can update \033[1mNUM_OF_PARTICLES\033[0m and \033[1mNUM_OF_ENERGY\033[0m as needed, eg")
    print()
    print("\033[1mSix\033[0m identical but distinguishable particles share \033[1mseven\033[0m units of energy.")
    print("Each particle can have energy only in integral amounts.")
    print()
    print("Create a table that lists all possible macrostates and for each macrostate")
    print("compute its multiplicity.")
    print()
    print(f"\033[0;32mNUM_OF_PARTICLES = {NUM_OF_PARTICLES}")
    print(f"NUM_OF_ENERGY =  {NUM_OF_ENERGY}\033[0m")
    print()
    total_microstates()
    solve_macrostates(0, 0, 0)
    print("\033[91mAgain, print out all the macrostates in a different format:\033[0m")
    print_total_macrostates_dict(total_macrostates_dict)

display_probabilities()
