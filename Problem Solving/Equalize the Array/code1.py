def equalizeArray(arr):
    l1 = [arr.count(i) for i in set(arr)]
	s1 = len(arr) - max(l1)
	return s1
	
