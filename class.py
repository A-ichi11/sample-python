# -*- coding: utf-8 -*-


class Complex:
    # __init__特別なメソッド。インスタンスが生成されると自動で呼び出し
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

# インスタンス生成
x = Complex(3.0, -4.5)
print(x.r, x.i)
