if __name__ == '__main__':
    N = int(input())
    list_number = []
    for _ in range(N):
        command = input().split()
        if command[0] == 'insert':
            list_number.insert(int(command[1]), int(command[2]))
        elif command[0] == 'remove':
            list_number.remove(int(command[1]))
        elif command[0] == 'append':
            list_number.append(int(command[1]))
        elif command[0] == 'pop':
            list_number.pop()
        elif command[0] == 'sort':
            list_number = sorted(list_number)
        elif command[0] == 'reverse':
            list_number.reverse()
        elif command[0] == 'print':
            print(list_number)