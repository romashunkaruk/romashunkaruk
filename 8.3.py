#! /usr/bin/env python3

def _average_value_(av):
	i=0
	j=0
	while i < len(av):
		j = j + int(av[i])
		i = i + 1
	j = j / len(av)
	return(j)

def _mediana_(med):
	length = len(med)
	if length % 2 == 0:
		t = int(med[length//2]) + int(med[length//2 - 1])
		return(t)
	if length // 2 != 0:
		return(int(med[int(length//2)]))


a = list(input('Задайте знач через кому : ').split(","))
print('\nСереднє значення списку : ', _average_value_(a),'\nМедіана : ', _mediana_(a))
