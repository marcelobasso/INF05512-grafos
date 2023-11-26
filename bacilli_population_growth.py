population_at_k = [0, 1]
positions = []

# reads number of instances
N_inst = int(input())

# reads all desired K's
for i in range(N_inst):
    n_inp = input()
    pos = int(n_inp[-12:len(n_inp)]) % 1500
    positions.append(pos)

# calculate ellements till the biggest
for x in range(2, 1500):
    pn = (population_at_k[x - 1] + population_at_k[x - 2]) % 1000
    population_at_k.append(pn)

# print the number in order
for i in range(N_inst):
    print(f"{population_at_k[positions[i]]:03d}")