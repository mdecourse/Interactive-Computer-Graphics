# !/usr/bin/env python

#	Assignment 5.4 - Affine Transformation - Reflection
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions

# defining some colors
backGroundColor = (0, 0, 0) # background color as black
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 512
originX = int (scrWidth / 2)
originY = int (scrHeight / 2)

# draw polygon
def drawPolygon (vertexX, vertexY, numVertex, color) :
	for i in range (numVertex) :
		pygame.draw.line (display_box, color, [vertexX[i % numVertex], vertexY[i % numVertex]], [vertexX[(i + 1) % numVertex], vertexY[(i + 1) % numVertex]], 1)
	pygame.display.update ()

# reflection along x-axis
def drawReflectionX (vertexX, vertexY, numVertex, color) :
	for i in range (numVertex) :
		pygame.draw.line (display_box, color, [vertexX[i % numVertex], 2 * originY - vertexY[i % numVertex]], [vertexX[(i + 1) % numVertex], 2 * originY - vertexY[(i + 1) % numVertex]], 1)
	pygame.display.update ()

# reflection along y-axis
def drawReflectionY (vertexX, vertexY, numVertex, color) :
	for i in range (numVertex) :
		pygame.draw.line (display_box, color, [2 * originX - vertexX[i % numVertex], vertexY[i%numVertex]], [2 * originX - vertexX[(i + 1) % numVertex], vertexY[(i + 1) % numVertex]], 1)
	pygame.display.update ()

# start here
if __name__ == '__main__' :
		# get input from command line
		numVertex = int (input ('Enter the number of vertices for your polygon : ').strip ())
		print ('The vertices will be modified into', originX, 'x', originY, 'quadrant')
		vertexX = list ()
		vertexY = list ()
		for i in range (numVertex) :
			print ("Vertex", i)
			temp = int (input ('X coordinate : ').strip ())
			vertexX.append (temp % originX + originX)
			temp = int (input ('Y coordinate : ').strip ())
			vertexY.append (originY - temp % originY)

		# initialize the display box (window)
		display_box = pygame.display.set_mode (screenSize) # set size of screen
		display_box.fill (backGroundColor) # set background color of the screen
		pygame.display.update ()

		# draw axes
		pygame.draw.line (display_box, white, [originX, 0], [originX, scrHeight], 1)
		pygame.draw.line (display_box, white, [0, originY], [scrWidth, originY], 1)
		pygame.display.update ()

		# draw the polygon
		drawPolygon (vertexX, vertexY, numVertex, blue)
		# draw the polygon reflection w.r.t x-axis
		drawReflectionX (vertexX, vertexY, numVertex, red)
		# draw the polygon reflection w.r.t y-axis
		drawReflectionY (vertexX, vertexY, numVertex, green)

		# update display
		pygame.display.update ()

		# wait for user exit
		while 1 :
				for event in pygame.event.get () :
						if event.type == pygame.QUIT :
								sys.exit ()
