population_at_k = [0, 1]
positions = []
biggest_pos = 0

# reads number of instances
N_inst = int(input())

# reads all desired K's
for i in range(N_inst):
    n_inp = input()
    pos = int(n_inp[-12:len(n_inp)]) % 1500
    positions.append(pos)

    if pos > biggest_pos:
        biggest_pos = pos

# calculate ellements of fibonacci series till the biggest requested
for x in range(2, biggest_pos + 1):
    pn = (population_at_k[x - 1] + population_at_k[x - 2]) % 1000
    population_at_k.append(pn)

# print the requested numbers in order
for i in range(N_inst):
    print(f"{population_at_k[positions[i]]:03d}")