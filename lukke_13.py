goods = []

with open('loot.txt', 'r', encoding="utf-8") as file:
    data = file.readlines()
    for line in data:
        goods.append(int(line.split()[1]))

goods = sorted(goods,reverse=True)

thue_morse_seq = '0110100110010110100101100110100110010110011010010110100110010110'
while len(thue_morse_seq) < len(goods):
    for ch in thue_morse_seq:
        if ch == '0':
            thue_morse_seq += '1'
        else:
            thue_morse_seq += '0'

bob_takes = 0
for i in range(len(goods)):
    if thue_morse_seq[i] == '1':
        bob_takes += goods[i]
print(bob_takes)

