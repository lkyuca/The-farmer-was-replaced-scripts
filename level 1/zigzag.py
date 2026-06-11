#test file for harvesting bushes in a zigzag pattern
for i in range(get_world_size()):
	harvest()
	move(North)
	if can_harvest():
		move(East)