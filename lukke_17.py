# tallet A = a1a2...a(n-1)6
# tallet B = 6a1...a(n-1)
# B = 4A

counter = 1
while True:
    a = 10*counter + 6
    counter += 1
    b = 4*a
    if str(b)[0] == '6' and int(str(a)[:-1]) == int(str(b)[1:]):
        print(a)
        break



