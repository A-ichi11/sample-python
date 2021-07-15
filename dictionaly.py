# -*- coding: utf-8 -*-

# dictionary型 辞書型 mapと同じ?

d = {"x":1, "y":2}
print(type(d))
print(d)
# これでkeyがxのvalを出力
print(d["x"])

# 値の上書き
d["x"] = 100
print(d)

# 値の追加
d["z"] = 1000
print(d)

# このような作り方も出来る
c =dict(a=1,b=2)
print(c)

# タプルを中に入れる事も可能
t = dict([("a",1),("b",2)])
print(t)

# メソッド
# keyだけ取り出し
print(d.keys())
# valuesだけ取り出し
print(d.values())

# 上書き
m = {"x": 1000, "j":11}
d.update(m)
print(d)

# get
print(d["x"])
print(d.get("x"))

# 中に何が入っているか確認
print("x" in d)
print("a" in d)


# 参照渡しのため、コピーは注意する
x = {"a":1}
y = x
y["a"] =1000
# どっちも1000に書き変わる
print(x)
print(y)

# 避けるためにはcopyを使う
x = {"a":1}
y = x.copy()
y["a"] =1000
print(x)
print(y)


def menu(**w):
    print(w)
    for k,v in w.items():
        print(k,v)
        # ドキュメント

menu(entree="beef",drink="coffee")
