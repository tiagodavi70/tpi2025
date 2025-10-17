# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 1 x 10 = 10

for i in range(1, 11):
    print("Tabuada de " + str(i))
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()
