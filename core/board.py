from core.oj import oj

# users_probs data structure:
#   tuple(users, probs)
#   users:
#     dict(user1_name: {oj1: oj1_uid, ...}, ...)
#   probs:
#     [(prob1_judge, prob1_namestr), (prob2_judge, prob2_namestr), ...]
# return data structure:
#   dict(user1_name: [prob1_status_str, prob2_status_str, ...], ...)
def fetch(users_probs):
	users, probs = users_probs
	for i,p in enumerate(probs):
		probs[i] = (p[0], oj.decode_probname(p[0],p[1]))
	judges = set()
	for p in probs:
		judges.add(p[0])
	result = {}
	for user, accts in users.items():
		raw_result = {}
		for judge in judges:
			if judge in accts:
				raw_result[judge] = oj.fetch_user(judge,accts[judge])
			else:
				raw_result[judge] = set()
		status = []
		for p in probs:
			judge, prob = p
			if p in raw_result[judge]:
				status.append("AC")
			else:
				status.append("NO")
		result[user] = status
	return result
