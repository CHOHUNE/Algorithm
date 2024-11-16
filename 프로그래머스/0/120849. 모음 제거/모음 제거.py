def solution(my_string) :
	s =''
	for char in (my_string) :
		if char not in 'aeiou':
			s+=char
	return s