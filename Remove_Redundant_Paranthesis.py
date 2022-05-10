def isOperator(ch):
    if ch == "+" or ch == "-" or ch == "*" or ch == "/":
        return True
    return False

def rmv_rdnt_pnths(s):
    st = []
    d = dict()
    for i in range(len(s)):
        if isOperator(s[i]):
            st.append([s[i],i])
        elif s[i] == "(":
            st.append([s[i],i])
        elif s[i] == ")":
            if st[-1][0] == "(":
                d[st[-1][1]] = 1
                d[i] = 1
            while isOperator(st[-1][0]):
                st.pop()
            st.pop()

    res = ""
    for i in range(len(s)):
        if i not in d.keys():
            res += s[i]
    if res[0] == "(" and res[-1]==")":
        res = res[1:len(res)-1]
    print(res)
    

s = input()
rmv_rdnt_pnths(s)
