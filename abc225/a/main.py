S = list(input())
st = set()

st.add(S[0] + S[1] + S[2])
st.add(S[0] + S[2] + S[1])
st.add(S[1] + S[2] + S[0])
st.add(S[1] + S[0] + S[2])
st.add(S[2] + S[1] + S[0])
st.add(S[2] + S[0] + S[1])

print(len(st))
