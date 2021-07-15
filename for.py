# -*- coding: utf-8 -*-



# 単純な繰り返し
words = ["cat","window","dog","だよ"]
for w in words:
    print(w)
    print(w,len(w))


# range
# 5回繰り返し
for i in range(5):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
# for b in range(a):
#     print(b)
# ↑エラーになる
# rangeはintしか受け取らない

for i in range(len(a)):
    print(i,a[i])

# enumerate 繰り返し。indexも同時に取り出し。
for i, v in enumerate(['tic', 'tac', 'toe']):
     print(i, v)

# dict型のループ
array ={"a":"apple","b":"banana"}
for k,v in array.items():
    print(k,v)
