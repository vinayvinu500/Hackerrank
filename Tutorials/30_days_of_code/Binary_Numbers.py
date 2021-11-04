import re
# https://www.hackerrank.com/challenges/30-binary-numbers/problem?h_r=internal-search

if __name__ == '__main__':
    # method 1
    """
    N = 6
    binary_string = bin(N).replace('0b','')
    # print(binary_string)
    pattern = r'1+'
    matches = re.findall(pattern, binary_string)
    # print(matches)
    # span = matches.span()
    # ones = binary_string[span[0]:span[1]]
    ones = max(matches)
    # print(ones)
    print(len(ones))
    # print(ones)
    # print(len(ones))
    """
    # method 2
    N = 13

    def binary(n):
        count = 0
        while n != 0:
            # n = bin(n).replace('0b','')
            print("binary: ",bin(n).replace('0b',''))
            print('bitwise left: ', bin(n << 1).replace('0b',''))
            print("bitwise and: ",bin(n & (n << 1)).replace('0b',''))
            print("")
            n = n & (n << 1)
            count += 1
        return count

    print(binary(N))
