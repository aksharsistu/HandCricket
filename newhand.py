from random import randint
from PIL import Image

re = Image.open("hand.jpg")
xy=open("Hand Cricket.py")
xy.read()
i1 = Image.open("1.png", "r")
i2 = Image.open("2.png", "r")
i3 = Image.open("3.png", "r")
i4 = Image.open("4.png", "r")
i5 = Image.open("5.png", "r")
i6 = Image.open("6.png", "r")
i7 = Image.open("7.png", "r")
i8 = Image.open("8.png", "r")
i9 = Image.open("9.png", "r")
i0 = Image.open("10.png", "r")

print("odd or even?")
a = str(input(":"))
print("enter your number:")
b = int(input())
c = randint(1, 10)
print(c)
d = b + c
x = "odd"
y = "even"
e = randint(1, 2)

o = int
p = int
q = int
r = int

if d % 2 == 0:
    print("it's even")
    if a == x:
        print("you loose the toss")

        if e == 1:
            print("i choose to bat")
        if e == 2:
            print("i choose to bowl")

    if a == y:
        print("you win the toss")
        f = str(input("you choose to:"))

if d % 2 != 0:
    print("it's odd")
    if a == x:
        print("you win the toss")
        f = str(input("you choose to:"))
    if a == y:
        print("you loose the toss")

        if e == 1:
            print("i choose to bat")
        if e == 2:
            print("i choose to bowl")
print("Let's start the game")
if e == 1:
    for i in range(1000):
        h = int(input("your no.:"))
        g = randint(1, 10)
        print(g)
        if g == 1:
            i1.show()
            i1.close()
        if g == 2:
            i2.show()
            i2.close()
        if g == 3:
            i3.show()
            i3.close()
        if g == 4:
            i4.show()
            i4.close()
        if g == 5:
            i5.show()
            i5.close()
        if g == 6:
            i6.show()
            i6.close()
        if g == 7:
            i7.show()
            i7.close()
        if g == 8:
            i8.show()
            i8.close()
        if g == 9:
            i9.show()
            i9.close()
        if g == 10:
            i0.show()
            i0.close()
        o = g
        if g == h:
            print("i am out")
            o = o + g
            print("score:", o)
        o = o + g
        i = i + 1
        break
if e == 2:
    for i in range(1000):
        m = int(input("your no.:"))
        p = m
        n = randint(1, 10)
        print(n)
        if n == 1:
            i1.show()
            i1.close()
        if n == 2:
            i2.show()
            i2.close()
        if n == 3:
            i3.show()
            i3.close()
        if n == 4:
            i4.show()
            i4.close()
        if n == 5:
            i5.show()
            i5.close()
        if n == 6:
            i6.show()
            i6.close()
        if n == 7:
            i7.show()
            i7.close()
        if n == 8:
            i8.show()
            i8.close()
        if n == 9:
            i9.show()
            i9.close()
        if n == 10:
            i0.show()
            i0.close()
        if n == m:
            print("you are out")
            p = p + m
            print("score:", p)
        p = p + m
        i = i + 1
        break

print("its your turn")
if e == 1:

    for j in range(o):
        j = int(input("your no.:"))
        k = randint(1, 10)
        print(k)
        if k == 1:
            i1.show()
            i1.close()
        if k == 2:
            i2.show()
            i2.close()
        if k == 3:
            i3.show()
            i3.close()
        if k == 4:
            i4.show()
            i4.close()
        if k == 5:
            i5.show()
            i5.close()
        if k == 6:
            i6.show()
            i6.close()
        if k == 7:
            i7.show()
            i7.close()
        if k == 8:
            i8.show()
            i8.close()
        if k == 9:
            i9.show()
            i9.close()
        if k == 10:
            i0.show()
            i0.close()
        q = k

        if k == j:
            print("you are out")
            q = q + k
            print("score:", q)
        q = q + k
        break
if e == 2:
    for k in range(p):
        k = int(input("your no.:"))
        j = randint(1, 10)
        print(j)
        if j == 1:
            i1.show()
            i1.close()
        if j == 2:
            i2.show()
            i2.close()
        if j == 3:
            i3.show()
            i3.close()
        if j == 4:
            i4.show()
            i4.close()
        if j == 5:
            i5.show()
            i5.close()
        if j == 6:
            i6.show()
            i6.close()
        if j == 7:
            i7.show()
            i7.close()
        if j == 8:
            i8.show()
            i8.close()
        if j == 9:
            i9.show()
            i9.close()
        if j == 10:
            i0.show()
            i0.close()
        r = k
        if j == k:
            print("i am out")
            r = r + k
            print("score:", r)
        r = r + k
        break

try:
    if q > o:
        print("You loose")
    if r > p:
        print("you win")

except:
    "Thank you!"


finally:
    print("game over")
    s = input("do you want to play again? y/n")
    if s == "y":
        xy.read()
    if s == "n":
        quit()
