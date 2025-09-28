
#456
cdu = int(input("Entra com o número: "))

c = cdu // 100
d = c * 10 - (cdu // 10)
u = cdu - (cdu // 10)

udc = u * 100 + d * 10 + c

print(udc)