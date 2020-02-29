
given = 5

def soft_sum(cards):
	if 1 in cards:
		if sum(cards) <= 11:
			return sum(cards)+10
	return sum(cards)

def prob(cards,p):
	if len(cards) == 1:
		return 1.0
	if 10 == cards[-1]:
		return p*prob(cards[:-1],p)
	else:
		return ((1-p)/9.0)*prob(cards[:-1],p)

# sum will be in the range 17-27
probs = [0]*7		# 21,20,19,18,17,black_jack,22+, 
def compute_dealer_probabilities(p,cards):
	global probs
	sum_ = soft_sum(cards)
	if sum_ < 17:
		for i in range(1,11):
			a = cards+[i]
			compute_dealer_probabilities(p,a)
	else:
		if sum_ > 21:
			probs[-1] = probs[-1]+prob(cards,p)
		else:
			if cards == [1,10]:
				probs[4] += prob(cards,p)
			elif cards == [10,1]:
				probs[4] += prob(cards,p)
			else:
				probs[21-sum_] += prob(cards,p)

probabilities = []
for i in range(1,11):
	compute_dealer_probabilities(given,[i])
	probabilities.append(probs)
	probs = [0]*7

