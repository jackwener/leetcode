def common(str1,str2) -> str:
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                i += 1
                continue
            else:
                return str1[:i]
        return str1[:i]

a = common("1234","1234")
print(a)