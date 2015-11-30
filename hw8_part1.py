import math
import operator
import re
import string

def print_dict(dictionary, ident = '', braces=1):
	
	for key, hAsh in dictionary.iteritems():
		if isinstance(hAsh, dict):
			print '%s%s%s%s' %(ident,braces*'[',key,braces*']') 
			print_dict(hAsh, ident+'  ', braces+1)
		else:
			print ident+'%s = %s' %(key, hAsh)

def main():
	alpha_count_num = dict.fromkeys(string.ascii_lowercase, float(1.0))
	alpha_count_denom = dict.fromkeys(string.ascii_lowercase, float(26.0))
	alpha_count_prob = dict.fromkeys(string.ascii_lowercase, float(0.0))
	#alpha_transition = dict.fromkeys(string.ascii_lowercase, dict.fromkeys(string.ascii_lowercase, float(1.0)))
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alpha_transition2 = {}
	for let1 in alpha:
		alpha_transition2[let1] = {}
		for let2 in alpha:
			alpha_transition2[let1][let2] = float(1.0)
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
	for letter in alpha_count_prob:
		alpha_count_prob[letter] = alpha_count_num[letter] / alpha_count_denom[letter]
	
	#calc transitional probs
	for letter in range(0,len(lines)-1):
		if re.search('[a-z]',lines[letter][0]) and re.search('[a-z]',lines[letter+1][0]):
			alpha_transition2[(lines[letter][0])][(lines[letter+1][0])] +=1 
	#normalize transitional probabilities		
	for letter in alpha_count_prob:
		for given in alpha_count_prob:
			alpha_transition2[letter][given] = alpha_transition2[letter][given] / alpha_count_denom[letter]  
	
			
			
	print 'Transitional Probabilities'
	print ''
	#print_dict(alpha_transition2)
	for letter in alpha_count_prob:
		for given in alpha_count_prob:
			print 'probability next letter is: ' + given + ', given this letter is: ' +letter + ' = ' + str(alpha_transition2[letter][given])
	
	
	print ''
	print '-----------------------------------'
	print ''
	print 'Emission Probabilites'
	print 'E[t] | X[t]'
	print ''  		
	for key, val in alpha_count_prob.iteritems():
		print key, val	

if __name__ == "__main__":
    main()
	
