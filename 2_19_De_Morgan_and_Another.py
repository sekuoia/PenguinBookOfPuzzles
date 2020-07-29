# for x in range(1,100):
#     if 1700 < x**2 < 1900:
#         print(x, x**2)
#         print("Year of birth is" , ((x**2) - x))

for a in range(1,10):
    for b in range(1,10):
        if 1800 < a**4 + b**4 < 2000:
            print(a, b, a**2 + b**2, a**4 + b**4)

print('_________________')

for m in range(1, 35):
    print(m, 2*m, 2*(m**2))

print('_________________')

for n in range(1,25):
    print(n, 3 * n, 3 * (n **4))