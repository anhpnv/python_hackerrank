''''
print(*values, sep=' ', end='\n', file=sys.stdout)
print(value1, value2, value3, sep=' ', end='\n', file=sys.stdout)

Here, values is an array and *values means array is unpacked, you can add values separated by a comma too. The arguments sep, end, and file are optional, but they can prove helpful in formatting output without taking help from a string module.

The argument definitions are below:
sep defines the delimiter between the values.
end defines what to print after the values.
file defines the output stream.
'''
if __name__ == '__main__':
    n = int(input())
    list_integers = list(range(1,n+1))
    print(*list_integers,sep='',end='\n')