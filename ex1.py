def max_valid_bracket(str):
    maxl = 0
    length = len(str)
    curl = 0
    numl = 0
    if length == 0:
        return 0
    for i in range(length):
        if str[i] == '(':
            numl += 1
        else:
            if numl > 0:
                curl += 2
                numl -= 1
            else:
                maxl = max(maxl, curl)
                curl = 0
    maxl = max(maxl, curl)
    return maxl


if __name__=="__main__":
    string = input('Input a bracket string containing "(" and ")": ')
    print(max_valid_bracket(string))
