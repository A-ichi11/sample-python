# タプル型 tuple型
# 後からデータを追加出来ないので、読み込み専用のように使いたい時に利用する
t = (1,2,3,4,5,1)
print(t)
# 値の代入は出来ない
# t[0] = 100
# print(t)

# 一つだけ出力できる
print(t[0])

# 何番目にあるか
print(t.index(1))

# 何個あるか
print(t.count(1))

# タプル内にリストを入れることはできる
t = ([1,2,3],[4,5,6])
print(t)
print(type(t))

# タプルの中のlistのデータは変更できる
t[0][0] = 100
print(t)

# これでもタプル型になる。カンマが入っているとタプル型になる。
n = 1,2,3
print(type(n))


# タプルのアンパッキング。数字の入れ替え
a = 100
b = 200
print(a,b)
a,b = b,a
print(a,b)