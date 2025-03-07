def constrain(value, min_value=0, max_value=1):
	return max(min(value, max_value), min_value)