P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]

def apply_permutation(x, p):
  res = []
  for i in p:
    res.append(x[i-1])
  return res

def left_shift(x, places = 1):
  places %= len(x)
  return x[places:] + x[:places]

# key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
key = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0]

key_p10 = apply_permutation(key, P10)
print(f'Key after P10 permutation: {key_p10}')

l = key_p10[:5]
r = key_p10[5:]
print(f'Left half: {l}, Right half: {r}')

l_ls1 = left_shift(l)
r_ls1 = left_shift(r)
print('Applying left shift')
print(f'Left half: {l_ls1}, Right half: {r_ls1}')

key_ls1 = l_ls1 + r_ls1
k1 = apply_permutation(key_ls1, P8)
print(f'Key-1 after applying P8 permutation: {k1}')

l_ls2 = left_shift(l_ls1, 2)
r_ls2 = left_shift(r_ls1, 2)
print('Applying double left shift')
print(f'Left half: {l_ls2}, Right half: {r_ls2}')


key_ls2 = l_ls2 + r_ls2
k2 = apply_permutation(key_ls2, P8)
print(f'Key-2 after applying P8 permutation: {k2}')

print('Final keys obtained')
print(f'Key-1: {k1}')
print(f'Key-2: {k2}')

IP = [2, 6, 3, 1, 4, 8, 5, 7]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]

def apply_xor(x, y):
  res = []
  for i in range(len(x)):
    res.append(x[i] ^ y[i])
  return res

S0 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]

S1=  [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,0],
      [2,1,0,3]]

def apply_s_box(x, s):
  r = int(f'{x[0]}{x[3]}', 2)
  c = int(f'{x[1]}{x[2]}', 2)
  val = s[r][c]

  if val == 0: return [0, 0]
  elif val == 1: return [0, 1]
  elif val == 2: return [1, 0]
  else: return [1, 1]

def split_halves(x):
  n = len(x) // 2
  return x[:n], x[n:]

def perform_round(text, key, swap):
  l, r = split_halves(text)
  r_new = apply_permutation(r, EP)
  r_new = apply_xor(r_new, key)
  rl, rr = split_halves(r_new)
  r_new = apply_s_box(rl, S0) + apply_s_box(rr, S1)
  r_new = apply_permutation(r_new, P4)
  r_new = apply_xor(l, r_new)
  return r + r_new if swap else r_new + r

plain_text = [0, 0, 1, 0, 1, 0, 0, 0]
# plain_text = [1, 0, 0, 1, 0, 1, 1, 1]

text = apply_permutation(plain_text, IP)
print(text)
text = perform_round(text, k1, True)
print(text)
text = perform_round(text, k2, False)
print(text)
cipher_text = apply_permutation(text, IP_inv)

cipher_text