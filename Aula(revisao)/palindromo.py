s = input()
 
s = s.replace(" ","")
s2 = s[::-1]
flag = True

for i in range(len(s)):
    if s[i] != s2[i]:
        print("Não é palindromo")
        flag = False
        break

if flag:
    print("É palindromo")