Stuart = list('bcdfghjklmnpqrstvwxyz'.upper())
Kevin = list('aeiou'.upper())
def minion_game(string):
    # your code goes here
    sub_string = ""
    count_1 = 0
    count_2 = 0
    for i in range(len(string)):
        if string[i] in Stuart:
            count_1 = count_1 + len(range(i, len(string)))
        elif string[i] in Kevin:
            count_2 = count_2 + len(range(i, len(string)))

    if count_1 > count_2:
        print(f"Stuart {count_1}")
    elif count_1 == count_2:
        print("Draw")
    else:
        print(f"Kevin {count_2}")

if __name__ == '__main__':
    s = input()
    minion_game(s)