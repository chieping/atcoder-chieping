h1, h2, h3, W1, W2, W3 = map(int, input().split())
H = [h1, h2, h3]
W = [W1, W2, W3]
ans = 0

match = []
for r in range(3):
    match.append([])
    for i0 in range(1, 29):
        if i0 + 2 > H[r]: break
        for i1 in range(1, 29):
            if H[r] - i0 - i1 > 0:
                match[r].append((i0, i1, H[r] - i0 - i1))
            else:
                break

ans = 0
for w0, w1, w2 in match[0]:
    for j in match[1]:
        if w0 + j[0] > W1:
            break
        if w1 + j[1] > W2 or w2 + j[2] > W3:
            continue
        
        for k in match[2]:
            if W1 - w0 - j[0] == k[0] and W2 - w1 - j[1] == k[1] and W3 - w2 - j[2] == k[2]:
                ans += 1

print(ans)