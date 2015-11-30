import math
import operator
import re
import string

def print_dict(acd, alpha_transition2, alpha_emissions):
	print 'Transitional Probabilities'
	print ''
	for letter in acd:
		for given in acd:
			print 'probability next letter is: ' + given + ', given current letter is: ' +letter + ' = ' + str(alpha_transition2[letter][given])
	
	
	print ''
	print '-----------------------------------'
	print ''
	print 'Emission Probabilites'
	print 'E[t] | X[t]'
	print ''  		
	#for key, val in alpha_count_prob.iteritems():
	#	print key, val	
	for letter in acd:
		for given in acd:
			print 'probability output is: ' + given + ', given state is: ' +letter + ' = ' + str(alpha_emissions[letter][given])

def viterbi_algo(acd, alpha_transition2, alpha_emissions, lines_test):
	original_state = ''
	state = ''
	vx = {}
	vpxp = {}
	pie = {}
	for let1 in acd:
		vx[let1] = float(0.0)
		pie[let1] = acd[let1] / len(lines_test)
	
	#initial
	for let1 in acd:	
		vx[let1] = math.log(alpha_emissions[let1][lines_test[1][2]]) + math.log(pie[let1]) 
	state = max(vx.iteritems(), key=operator.itemgetter(1))[0]
	original_state += state
	vpxp = dict(vx)
	
	#algo
	for letter in range(2,len(lines_test)):
		for let1 in acd:
			vx[let1] = math.log(alpha_emissions[let1][lines_test[letter][2]]) + .74 * math.log(alpha_transition2[state][let1]) + vpxp[state]
		state = max(vx.iteritems(), key=operator.itemgetter(1))[0]
		original_state += state				
		#vpxp = {key: vx[key] + vpxp.get(key, 0) for key in vx.keys()}
		vpxp = dict(vx)
		
	return original_state

		
def main():
	
	
	#create dicts and lists
	alphat = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alpha_emissions = {}
	alpha_transition2 = {}
	acd = {}
	err_rate_original = 0.0
	err_rate_after_algo = 0.0
	after = ''
	
	for let1 in alphat:
		acd[let1] = float(28.0)
	
	for let1 in alphat:
		alpha_transition2[let1] = {}
		alpha_emissions[let1] = {}
		for let2 in alphat:
			alpha_transition2[let1][let2] = float(1.0)
			alpha_emissions[let1][let2] = float(1.0)
	
	#read in files: typos into lines and typos-test into lines_test
	lines = []
	with open('typos20.data') as f:
		lines = f.read().splitlines()
		
	lines_test = []
	with open('typos20Test.data') as t:
		lines_test = t.read().splitlines()
		
	# find & set observations & states
	for i in range(0,len(lines)):
		if re.search('[a-z_]',lines[i][0]): 
			acd[lines[i][0]] +=1
			
		
	#calc transitional and emission probs
	for letter in range(0,len(lines)-1):
		if re.search('[a-z_]',lines[letter][0]) and re.search('[a-z_]',lines[letter+1][0]):
			alpha_transition2[(lines[letter][0])][(lines[letter+1][0])] +=1
			alpha_emissions[(lines[letter][0])][(lines[letter][2])] +=1
	
	#normalize transitional and emission probabilities		
	for letter in alphat:
		for given in alphat:
			alpha_transition2[letter][given] = alpha_transition2[letter][given] / acd[letter]  
			alpha_emissions[letter][given] = alpha_emissions[letter][given] / acd[letter]
			
	after = viterbi_algo(acd, alpha_transition2, alpha_emissions, lines_test)
	
	#print_dict(acd, alpha_transition2, alpha_emissions)
	
	#calc and print error rates
	for i in range(1,len(lines_test)):
		if lines_test[i][0] == lines_test[i][2]:
			err_rate_original += 1
		if lines_test[i][0] == after[i-1]:
			err_rate_after_algo += 1
	err_rate_after_algo = err_rate_after_algo/len(after)
	err_rate_original = err_rate_original/len(after)
	err_rate_after_algo = 1 - err_rate_after_algo
	err_rate_original = 1 - err_rate_original
	print 'State sequence: '
	print after
	print 'error before algo: ', err_rate_original
	print 'error after algo : ', err_rate_after_algo
	
	
if __name__ == "__main__":
    main()
	
