for i in range(3):
    spaces = ' ' * (2 * i)
    bits = 7 - 4 * i
    pattern = ''
    for j in range(bits):
        pattern += '1' if j % 2 == 0 else '0'
    print(spaces + pattern)