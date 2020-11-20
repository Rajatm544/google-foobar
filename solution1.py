def solution(s):
    count = 0
    stemp = s[0:len(s)]
    st = ""
    arr = []
    for i in range(len(s)):
        st += s[i]
        arr = s.split(st)
        len_count = 0
        for ele in arr:
            if not len(ele):
                len_count += 1
        if(len_count == len(arr)):
            break
    print(len(s)//len(st))


def main():
    str = input()
    solution(str)


if __name__ == '__main__':
    main()
