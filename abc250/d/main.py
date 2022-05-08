N = int(input())

is_prime = [True] * (10**6+1)
is_prime[0] = is_prime[1] = False
prime_cnt = [0] * (10**6+1)
for i in range(2, 10**6+1):
    if is_prime[i]:
        prime_cnt[i] = 1
        for j in range(i*i, 10**6+1, i):
            is_prime[j] = False

for i in range(2, 10**6+1):
    prime_cnt[i] += prime_cnt[i-1]

ans = 0
for q in range(2, 10**6+1):
    if not is_prime[q]:
        continue
    pUpperBound = N // q**3
    ans += prime_cnt[min(pUpperBound, q-1)]

print(ans)