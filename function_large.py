# number size

def number_size():
    x = [4, 6, 8, 24, 12, 2]
    b = 0
    x_length = len(x)
    for i in range(x_length):
        if x[i] > b:
            b = x[i]
    print(b)


number_size()
