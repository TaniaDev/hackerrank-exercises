if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(list(set(arr)), reverse=True)
    print(arr[1])