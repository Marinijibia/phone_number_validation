import re

def is_valid_mobile_number(number):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, number) is not None

def main():
    N = int(input())
    for _ in range(N):
        number = input().strip()
        if is_valid_mobile_number(number):
            print("YES")
        else:
            print("NO")
    
    return 0

if __name__ == '__main__':
    main()
