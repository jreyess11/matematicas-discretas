import hashlib


def generate_random_number(seed):
    while True:
        seed = hashlib.sha256(seed).digest()
        print(int.from_bytes(seed,'little')%45)


generate_random_number(bytes(12))

