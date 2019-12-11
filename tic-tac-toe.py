print("""guide for input-elow give no. to fill the boxes-e.g- 00 for first box that is the box at the upper left corner.
similarly 01 is for tha upper middle box. """)

for i in range(3):
    for j in range(3):
        if j != 2:
            print(i, j, "|", end=" ")
        else:
            print(i, j)
            if i != 2:
                print("----------------")
m = -1
n = -1
l = []
for i in range(3):
    a = []
    for j in range(3):
        a.append(" ")
    l.append(a)
print("Starting condition:: ", l)


def re_enter():
    x = int(input("re-enter the place u want to place where blank is available:"))
    n = x % 10
    m = int(x / 10)
    print("M:: ", m, "  N:: ", n)
    in1(m, n)


def in1(m,n):
    for i in range(3):
        for j in range(3):
            if i == m and j == n:
                if l[i][j] == " ":
                    l[i][j] = '*'
                elif l[i][j] == "*" or l[i][j] == "0":
                    re_enter()


def in2(m, n):
    for i in range(3):
        for j in range(3):
            if i == m and j == n:
                if l[i][j] == " ":
                    l[i][j] = '0'
                elif l[i][j] == "*" or l[i][j] == "0":
                    re_enter()


def display():
    for i in range(3):
        for j in range(3):
            print(l[i][j], end=" ")
        print()




def check(g):
    for i in range(3):
        if l[i][0] == l[i][1] == l[i][2] != " ":
            print("game over")
            g = 0
        if l[0][i] == l[1][i] == l[2][i] != " ":
            print("game over")
            g = 0

    if g != 0:
        if l[0][0] == l[1][1] == l[2][2] != " " or l[0][2] == l[1][1] == l[2][0] != " ":
            print("game over:")
    return g

print("player 1 your sign is \"*\"")

print("player 2 your sign is \"0\"")

for i in range(9):
    g = 1
    if i % 2 == 0:
        print("player 1 turn:")
        x = int(input("enter the place u want to place:"))
        n = x % 10
        m = int(x / 10)
        print("M:: ", m, "  N:: ", n)
        in1(m, n)
        print("Present:: ", l)
        display()
        g = check(g)
        if g == 0:
            print("player 1 won")
            break
    else:
        print("player 2 turn:")
        x = int(input("enter the place u want to place:"))
        n = x % 10
        m = int(x / 10)
        in2(m, n)
        print("Present:: ", l)
        display()
        g = check(g)
        if g == 0:
            print("player 1 won")
            break
    if i == 8:
        print("it is a tie")


