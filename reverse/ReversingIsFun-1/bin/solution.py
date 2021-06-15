first_part = '}yy{xi~lqr:'

second_part = "sd'mU]6'<Uh"

for char in first_part:
    print(chr(ord(char) ^ 10), end='')

result = ''

for char in second_part:
    result += chr(ord(char) + 10)

print(result[::-1])
