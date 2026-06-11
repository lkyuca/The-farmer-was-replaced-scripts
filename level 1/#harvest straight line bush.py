#harvest straight line bush
while True:
	move(North)
	plant(Entities.Bush)
	if can_harvest():
		harvest()