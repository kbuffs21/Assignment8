import math
import operator
import re
import string


def main():
	alpha_count_num = dict.fromkeys(string.ascii_lowercase, float(1.0))
	alpha_count_denom = dict.fromkeys(string.ascii_lowercase, float(26.0))
	alpha_count_prob = dict.fromkeys(string.ascii_lowercase, float(0.0))
	lines = []
	
	with open('typos20.data') as f:
		lines = f.read().splitlines()
	
	# find & set observations & states
	for i in range(0,len(lines)):
		if re.search('[a-z]',lines[i]):
			alpha_count_denom[lines[i][0]] +=1 
			if lines[i][0] == lines[i][2]:
				alpha_count_num[lines[i][2]] +=1
	
	#calc individual probs
	for iterate in alpha_count_prob:
		alpha_count_prob[iterate] = alpha_count_num[iterate] / alpha_count_denom[iterate]
	
	
	for key, val in alpha_count_prob.iteritems():
		print key, val
	

if __name__ == "__main__":
    main()
	
