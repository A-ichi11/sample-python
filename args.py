# -*- coding: utf-8 -*-

def say(word):
    print(word)

say("Hi")

# argsの中引数をまとめられる。タプルに入る
def saysay(*args):
    for a in args:
        print(a)

saysay("Hi","Mike","Nancy")