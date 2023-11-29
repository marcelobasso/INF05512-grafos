import functools
fib = [0, 1]

# reads number of instances
N_inst = int(input())

# calculates fibonacci series till the 1500th term
for x in range(2, 1500):
    pn = (fib[x - 1] + fib[x - 2]) % 1000
    fib.append(pn)

# calculates position of every desired term
for i in range(N_inst):
    n_inp = input()
    len_ = len(n_inp)
    # truncates the input number to only it's 5 first digits
    crop_n = n_inp[-5:len(n_inp)]
    pos = int(crop_n)

    # if the size of the input number is bigger than 4
    if (len_ > 4):
        # sums all the digits of the number but the last 3 digits
        sum_ = functools.reduce(lambda a, b: int(a) + int(b), n_inp[0: -4])

        # if the sum mod 3 is different than the truncated number sum mod 3
        if (sum_ % 3 != (int(crop_n[0]) + int(crop_n[1])) % 3):
            # updates position fixing offset
            pos += (sum_ % 3) * 1000

    print(f"{fib[pos % 1500]:03d}")
