'''ROT-13 er et substitusjonschiffer hvor hver bokstav byttes ut med bokstaven som kommer 13 plasser etter den. A blir N, B blir O, C blir P osv. Når man teller forbi siste bokstav i alfabetet (vi ser her bort i fra ÆØÅ) fortsetter man fra starten igjen, W blir for eksempel J.

Andre verdier enn 13 kan selvsagt brukes. I den følgende meldingen har hver enkelt bokstav blitt kryptert med en egen verdi, nemlig summen av ascii-verdien til bokstaven og posisjonen til bokstaven i alfabetet.

OTUJNMQTYOQOVVNEOXQVAOXJEYA

Hva er den dekrypterte meldingen?

Eksempel: Dekrypterer vi PWVAYOBB får vi JULEMANN'''

from string import ascii_letters

letters = ascii_letters[26:]
encrypted_letters = ''
for ch in range(len(letters)):
    ltr = int(bin(int.from_bytes(letters[ch].encode(), 'big')), 2)
    new_pos = (ltr + ch + 1)%(-26)
    encrypted_letters += letters[new_pos+ch]

dictionary = dict()
for i in range(len(letters)):
    dictionary[encrypted_letters[i]] = letters[i]

to_decript = 'OTUJNMQTYOQOVVNEOXQVAOXJEYA'
decrypted = ''

for ch in to_decript:
    decrypted += dictionary[ch]

print(decrypted)



