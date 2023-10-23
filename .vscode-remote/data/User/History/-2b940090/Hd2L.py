def main():
    n = get_pos_number()
    meow(n)
def get_pos_number():
    while True:
        try:
            n = int(input("n: "))
            if n <= 0:
                raise ValueError
            return n
        except ValueError
        print("n is notpositive number")
def meow(n)
    for i in range(n):
        print("meow")