# bit_length()

num, num1 = 10, 50
print(num.bit_length())
print(num1.bit_length())

# to_bytes(length, byteorder, *, signed-False)
print(num.to_bytes(2, byteorder='big'))
print(num.to_bytes(10, byteorder='big'))

# from_bytes(bytes, byteorder, *, signed-False)
print(int.from_bytes(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\n', byteorder='big'))
