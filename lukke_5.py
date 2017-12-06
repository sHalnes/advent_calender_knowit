'''Vi beskriver en tallrekke på følgende måte:

Rekken inneholder positive heltall.
Neste tall i rekken er alltid større enn eller likt det foregående tallet, det minker aldri.
Verdien til tallet på n-te posisjon er antallet ganger n vil forekomme i rekken.
Rekken starter med a(1) = 1.
a(2) = 2
Sammen med de fem neste tallene i rekken får vi da: 1, 2, 2, 3, 3, 4 ...

Finn summen av de 1000000 (1 million) første tallene i rekken.'''


# not the best brute force solution 

N_array = [0 for x in range(1000001)]
N_array[1] = 1
N_array[2] = 2

counter = 2
pointer = 2
while counter < 1000001:
    value = N_array[counter]
    for x in range(value):
        if pointer  < len(N_array):
            N_array[pointer] = counter
            pointer += 1
    counter += 1
print(sum(N_array))
