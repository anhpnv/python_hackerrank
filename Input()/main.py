input_number = input().split()
polynomial = input()

x = int(input_number[0])
k = int(input_number[1])
if eval(polynomial) == k:
    print(True)
else:
    print(False)