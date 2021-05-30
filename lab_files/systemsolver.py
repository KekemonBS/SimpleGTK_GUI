# -*- encoding: utf-8 -*-

name = "Gauss method of sequential exclusion of coeficients"
req = {'Coefficient matrix\n[[a11,a12,...],[a21,a22,...]...]': None,'Free members column\n[b1,b2,...]': None,}
res = {}
result = "resulting vector"

import time 
import matplotlib.pyplot as plt
import numpy as np

def system(coeff_matr,free_coeff_vector):
	coeff_matr = [coeff_matr[i]+[free_coeff_vector[i]] for i in range(len(coeff_matr))]
	m = len(coeff_matr) 					# рядків
	n = min([len(s) for s in coeff_matr])	# стовпців
	if m+1 != n : return 'Матриця коефіцієнтів не квадратна'
	for i in range(0,m-1): 					# Прямий хід
		for j in range(i+1,m):
			M = coeff_matr[j][i]/coeff_matr[i][i]
			new_row = [(coeff_matr[j][k] - coeff_matr[i][k]*M) for k in range(n)]
			coeff_matr.pop(j)
			coeff_matr.insert(j,new_row)
	free_coeff_vector = [i[-1] for i in coeff_matr] 
	coeff_matr = [i[0:-1] for i in coeff_matr]
	result = [1]*m
	print("\n")
	for i in range(1,m+1): 					# Зворотний хід
		x = (free_coeff_vector[-i]-sum([coeff_matr[-i][j]*result[j] for j in range(n-1) if j!=m-i]))/coeff_matr[-i][-i]
		result[-i] = x
	return result
	
def main():
	coeff_matr = res.get('Coefficient matrix\n[[a11,a12,...],[a21,a22,...]...]').split('],')
	coeff_matr = list(map(lambda x : x.strip('[').strip(']').split(','), coeff_matr))
	coeff_matr = [[float(j) for j in i] for i in coeff_matr]
	free_coeff_vector = res.get('Free members column\n[b1,b2,...]')
	free_coeff_vector = list(map(lambda x : float(x.strip('[').strip(']')),free_coeff_vector.split(',')))
	
	solution = system(coeff_matr,free_coeff_vector)
	solution = sum([[solution.index(i)+1,i] for i in solution],[])
	form = 'x{} = {}\n'*len(coeff_matr)
	return form.format(*solution)
