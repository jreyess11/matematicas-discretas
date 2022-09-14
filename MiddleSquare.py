def generate_random_number(seed):
    while seed!=0:
        seed = seed * seed
        seed = take_middle_digits(seed)
        print(seed%100)

def take_middle_digits(num):
    num_str = str(num)
    while len(num_str)!=12:
        num_str="0"+num_str
    length = len(num_str)
    return int(num_str[length//2-2:length//2+3])

generate_random_number(675248)