# -*- coding: utf-8 -*-

y = [1,2,3]
x = 1

# yの中にxが入っているか
if x in y:
    print("in")
else:
    print("not")

# yの中に100が入っているか
if 100 not in y :
    print("not in")


a = 1
b = 2

# aとbが等しくない
if not a == b :
    print("Not Equal")
# 上と一緒の意味
if a != b:
    print("Not Equal")


if not c :
    print("not")

c = True
# これではエラーになる
# if !c :
print(c)