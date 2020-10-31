if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr)
    sort_array = sort(list(set(arr)))
    print(sort_array[-2])