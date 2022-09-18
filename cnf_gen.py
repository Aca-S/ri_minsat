import sys
import json
import random
from cnfgen import RandomKCNF
from math import comb


def gen_n_dimacs(num_of_formulas, num_of_vars, num_of_clauses):
	# max_clauses = comb(num_of_vars, 3) * 2**3
	return [RandomKCNF(3, num_of_vars, num_of_clauses).dimacs(export_header=False) for _ in range(num_of_formulas)]


def main():
	if len(sys.argv) != 5:
		print('Usage: python cnf_gen.py file_name num_of_formulas num_of_vars num_of_clauses')
		exit(1)
	
	try:
		num_of_formulas = int(sys.argv[2])
		num_of_vars = int(sys.argv[3])
		num_of_clauses = int(sys.argv[4])
	except ValueError:
		print('num_of_formulas, num_of_vars and num_of_clauses arguments have to be integers')
		exit(1)
	
	try:
		with open(sys.argv[1], 'w') as f:
			f.write(json.dumps(gen_n_dimacs(num_of_formulas, num_of_vars, num_of_clauses)))
	except IOError:
		print(f'Error opening file {sys.argv[1]}')
		exit(1)


if __name__ == '__main__':
	main()
