    # Size: 7 x 21 
    # ---------.|.---------
    # ------.|..|..|.------
    # ---.|..|..|..|..|.---
    # -------WELCOME-------
    # ---.|..|..|..|..|.---
    # ------.|..|..|.------
    # ---------.|.---------

matrix_len = input().split()
row = int(matrix_len[1])
col = int(matrix_len[0])

for i in range(col//2):
    left = '-' * 3 * (col//2 - i)
    center_1 = '.|.' * (i + 1)
    center_2 = '.|.' * i
    print(left + center_1 + center_2 + left)

print('-' * ((row - len('WELCOME'))//2) + 'WELCOME' +  
      '-' * ((row - len('WELCOME'))//2))

for i in range(col//2):
    left = '-' * 3 * (i + 1)
    center_1 = '.|.' * (col//2 - i)
    center_2 = '.|.' * (col//2 - i - 1)
    print(left + center_1 + center_2 + left)