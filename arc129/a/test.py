N = 5

print('{0:08b}'.format(N))
for i in range(1, N*2+1):
    xor = N ^ i
    print("i:", i, ", cnt:", xor < N , ",\t bin:", '{0:08b}'.format(i), ", XOR:", '{0:08b}'.format(xor))

