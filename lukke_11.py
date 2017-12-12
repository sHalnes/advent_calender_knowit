'''Et MIRPTALL er et primtall som fortsatt er primtall når sifrene reverseres, uten at de er palindromer.
(Et palindrom er et ord eller tall som gir samme resultat enten det leses fra høyre eller venstre).

Eksempel 1: Primtallet 13 er et MIRPTALL, fordi reversen, 31, også er et primtall.

Eksempel 2: Primtallet 23 er ikke et MIRPTALL da reversen ikke er et primtall.

Eksempel 3: Primtallene 5 og 101 er ikke MIRPTALL da reversen er palindromer.

Hvor mange positive heltall under 1000 er MIRPTALL?

NB! Alle MIRPTALL skal telles, dvs. tell både 13 og 31.'''

def is_palindrome(tall):
    if int(str(tall)[::-1]) == tall:
        return True
    return False

def is_prime(tall):
    for i in range(2, tall):
        if tall % i == 0:
            return False
    return True

mirptall = []

for x in range(12, 1000): # before 12 all primes are palindromes
    if x not in mirptall:
        # check if palindrome
        if not is_palindrome(x):
            # check if prime
            if is_prime(x):
                # check reverse
                rev = int(str(x)[::-1])
                if is_prime(rev):
                    mirptall += [x, rev]
print(len(mirptall))
