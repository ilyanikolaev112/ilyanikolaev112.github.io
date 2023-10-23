def main():
    x = get_int()
    print(f"x = {x}")
def get_int():
    while True:
        try:
            n = int(input("Enter n: "))
            return n
        except ValueError:
            print("n is not number")
            
