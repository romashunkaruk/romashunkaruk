#! /usr/bin/env python3

import sys 

weight = input("Введіть Ваш вагу (кг.): ")
height = input("Введіть Ваш зріст (м.): ")

weight = float(weight)
height = float(height)

BMI = weight / height**2
print('Ваш індекс маси тіла', + BMI)
