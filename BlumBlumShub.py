def generate_random_number(p, q, x):
    while True:
        n = p * q
        x = x**2 % n
        print(x)

generate_random_number(17,31,1248)