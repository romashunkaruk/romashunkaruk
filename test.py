#! /usr/bin/env python3 
# -*- coding: utf-8 -*-

#import sys

print('Введіть фразу : ')
phrase = str(input())
x = len(phrase)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if phrase[x - i] == phrase[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("Ця фраза не є паліндромом")
else:
  print("Ця фраза  є паліндромом")


