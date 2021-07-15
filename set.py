# 集合

a = {1,2,2,3,3,4,4,5,5,5,6}
# 同じ値は削除される
print(type(a),a)

b = { 2,3,4,7}
# aのsetから2.3.4を取り除いた値を出力
print(a-b)

# aにもbにもある値を出力
print(a & b)

# aとbにある全ての値を出力
print( a | b)

# aとbで重複していないものを出力
print( a ^ b)

# 集合にはindexがない
# これをするとエラーになる
# print(a[0])

# 追加は出来る
a.add(7)
print(a)

# 削除
a.remove(7)
print(a)