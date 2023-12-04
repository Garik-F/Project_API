s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

t = s.split(":")
result = {t[int(i)*2 + 1]: t[i*2] for i in t}

print(result)
