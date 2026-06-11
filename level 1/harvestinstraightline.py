#harvest in straight line
while True:
	move(North)
	if can_harvest():
		harvest()