from Stack import Stack

def solveMaze(maze, startX, startY):
	stack = Stack()
	directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
	stack.push([startX, startY])
	step = 1

	while not stack.isEmpty():

		x, y = stack.peek()

		if maze[x][y] == 'G':
			return True

		if maze[x][y] == ' ':
			maze[x][y] = step
			step += 1
		
		moved = False
		for dx, dy in directions:
			newX, newY = x + dx, y + dy
			if maze[newX][newY] in [' ', 'G']:
				stack.push([newX, newY])
				moved = True
				break

		if not moved:
			stack.pop()
			
		
	return False