users = []
users.append(1)
users.append(2)
users.append(3)
users.append(4)

i = 0

for a in range(10):
    if i < len(users):
        print(users[i])
    else:
        i = 0
        print(users[i])
    i += 1