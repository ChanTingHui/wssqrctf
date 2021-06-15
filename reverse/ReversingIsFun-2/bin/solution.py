import string

INT_BITS = 8

def leftRotate(n, d):
    result = bin(n << d)
    if len(result) - 2 > 8:
        result = result[-8:-1 * (len(result) - 2 - 8)] + result[2:-8]

    return int(result, 2)

rotated_left_3 = [187, 155, 155, 139, 147, 27, 0, 0, 0, 0, 129, 163, 250, 51]
rotated_left_4 = [119, 55, 55, 23, 39, 54, 71, 102, 183, 118, 0, 0, 0, 0]

flag = ''
for i in range(14):
    for char in string.ascii_letters + string.digits + '-_{}':
        if leftRotate(ord(char), 3) == rotated_left_3[i] or leftRotate(ord(char), 4) == rotated_left_4[i]:
            flag += char
    i += 1
print(flag)
assert len(flag) == 14

r_values = [76, 64, 103, 95, 66, 121, 95, 82, 51, 118, 51, 114, 36, 105]
flag += ''.join([chr(x) for x in r_values])

print(flag)
assert len(flag) == 28

flag += 'ng_th3_wh0L3_$'
print(flag)
assert len(flag) == 42

flag += 'ructur3_the_r1'
print(flag)
assert len(flag) == 56

fragment = ''
results = [1187410, 616666, 989235, 1068505, 600812, 949600, 1100213, 600812, 1131921, 600812, 1068505, 949600, 997162]
for result in results:
    for char in string.ascii_letters + string.digits + '-_{}':
        output = ord(char) * 7927 - 0x49
        if int(bin(output)[-16:], 2) == int(bin(result)[-16:], 2):
            fragment += char
            break

flag += 'd'
flag += fragment[::-1]
print(flag)