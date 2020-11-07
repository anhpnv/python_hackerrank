def print_formatted(number):
    # your code goes here
    for n in range(1,number+1):
        # print(n)
        print("%{0}s %{0}s %{0}s %{0}s".format(len(bin(number)[2:])) %(n, oct(n)[2:], hex(n)[2:].title(), bin(n)[2:]))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)