x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
     's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_rangoli(n):
    k =  x[0:n]

    # k = ['e', 'd', 'c', 'b', 'a', 'b', 'c', 'd', 'e']
    k =  sorted(k, reverse=True)[0:n-1] + sorted(k)
    len_string = len('-'.join(k))
    count = 0
    #above function
    if len(k) != 1:
        print('-' * (len(k) - 1) + 

                '-'.join(k[0:1]) + 

                '-'.join(k[len(k):len(k)]) +

                '-' * (len(k) - 1)
                )
    for i in range(1,len(k)//2):
        print('-' * (len(k)- i * 2 - 1)    + 

            '-'.join(k[0: i + 1]) +  '-' +

            '-'.join(k[len(k)-i:len(k)]) +

            '-' * (len(k) - i * 2 - 1)
            )
    # Below fucntion
    while True:
        if len(k) > 1:
            # print(len(k))
            print('-' * count * 2 +  '-'.join(k) + '-' * count * 2)
            del k[len(k)//2]
            del k[len(k)//2]
            count = count + 1
        else:
            print('-' * count * 2 +  '-'.join(k) + '-' * count * 2)
            break
#     # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


