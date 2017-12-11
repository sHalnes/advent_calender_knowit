#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:56:36 2017

@author: s_halnes


Velkommen til Knowit sitt julebord!

På julebordet er vi 1500 mennesker som sitter rundt et stort bord. Vi er nummerert fra 1 til 1500 langs bordet. Vi har fått tak i en flaske med meget sterk (men god!) akevitt.

Den første personen tar flasken og serverer person nummer to en dram. Akevitten er så sterk at denne personen går rett i bakken. Person nummer en sender så flaska videre til den tredje personen som serverer den fjerde en dram. Han går også rett i bakken og flasken sendes videre til femtemann. Dette fortsetter rundt slik at person nummer 1499 serverer person 1500 en dram (hvorpå han dundrer i gulvet) og gir flaska tilbake den første.

Nå serverer den første personen den tredje (som deiser av stolen) og gir flaska videre til den femte...

Dette fortsetter til det bare er en person igjen. Hvilken person sitter igjen ved julebordets slutt?

Svaret skal være i form av nummeret på personen som sitter igjen, eksempelvis 1337
"""

survived = [x for x in range(1500) if x%2>0]

survived = [x for x in range(1,1501)]
counter = 0
while counter < len(survived):
    if (counter + 1)%2 > 0:
        survived.append(survived[counter])
    counter += 1
print(survived[counter - 1])