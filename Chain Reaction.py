import numpy as np
import pygame


#display initial grid

#modify grid with user input
    #modify array
    #display modified array
#create next grid
    #modify array with next array subroutine
    #display array

 #loop the previous steps

def updatecells(cell_data):
    #get next array from input array

    #get input array as input
        #get array dimensions
        #return error is size is one by one
    #copy input array as output array
    #for each element of input array
        #explode cell if at critical mass
            #check what edges surround cell and count
                #initial array of boundary points like [[-1,1],[-1,1]]
                #what coordinates are bounds of the range of the coordinate
                #for each coordinate out of bounds, remove from list, add to edge counter
            #critical mass is 4-edge
            #if cell>= critmass
                #reduce cell by critmass in output
                #increase cells in boundary array by one
            #else do nothing


    #get array dimensions
    inputdim=cell_data.shape

    #return error is size is one by one
    if inputdim == (1,1):
        raise Exception("Array should be greater than 1x1")

    #copy input array as output array
    outarr=cell_data.copy()
    #for each element of input array
    for x in range(0,inputdim[0]):
        for y in range(0,inputdim[1]):

            coordinates=np.array((x,y))
            #explode cell if at critical mass
            #check what edges surround cell and count
            #initial array of boundary points like b=[[-1,1],[-1,1]]
            # b[0],b[1] correspond to available displacements in x and y
            # direction directions respectively

            availedges=np.array(((-1,1),(-1,1)))
            #what coordinates are bounds of the range of the coordinate
            for coordinate in range(0,2) :
                if coordinates[coordinate]==0:
                    availedges[coordinate,0]=0

                if coordinates[coordinate]==inputdim[coordinate]-1:
                    availedges[coordinate,1]=0

            #number of edges
            numavailedges=np.sum(np.absolute(availedges))
            #critical mass is 4-edge
            crit_mass=numavailedges
            #if cell>= critmass
            if cell_data[x, y]>=crit_mass:
                #reduce cell by critmass in output
                outarr[x,y]=outarr[x,y]-crit_mass

                #increase cells in boundary array by one
                for coordinate in range(2):
                    for direction in range(2):

                        #amount to move coordinate
                        displacecoord=availedges[coordinate,direction]

                        if displacecoord != 0:
                            if coordinate==0:
                                outarr[x+displacecoord,y]+=1
                            if coordinate==1:
                                outarr[x,y+displacecoord]+=1


    return outarr

def display_cells(cell_data, cellsize, gridsize, screen,color=(255, 0, 255)):


    for i in range(gridsize[0]):
        for j in range(gridsize[1]):

            rect_size = cellsize / 2

            if cell_data[i,j]==1:

                position=( cellsize[0]*(i+1/4) , cellsize[1]*(j+1/4) )
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)

            elif cell_data[i, j]==2:

                position = (cellsize[0] * i, cellsize[1] * (j+1/4))
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)

                position = (cellsize[0] * (i+1/2), cellsize[1] * (j+1/4))
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)


            elif cell_data[i, j]==3:

                position = (cellsize[0] * i, cellsize[1] * (j+1/2))
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)


                position = (cellsize[0] * (i+1/2), cellsize[1] * (j+1/2))
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)


                position = (cellsize[0] * (i+1/4), cellsize[1] * j)
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)

            elif cell_data[i, j]>=4:

                position = (cellsize[0] * i, cellsize[1] * (j+1/2))
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)


                position = (cellsize[0] * (i+1/2), cellsize[1] * (j+1/2))
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)


                position = (cellsize[0] * (i), cellsize[1] * j)
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)

                position = (cellsize[0] * (i+1/2), cellsize[1] * j)
                ellipse_rect = pygame.Rect(position, rect_size)
                pygame.draw.ellipse(screen, color, ellipse_rect)

            else:
                Exception("encountered nvalid Cell data whilst draw ")

#draw window
windowsize = np.array ( (1000 ,  1000) )
screen = pygame.display.set_mode(windowsize)


#initialise grid
gridsize=np.array((49,49))
#cell_data=np.random.randint(1,4,gridsize)
cell_data=np.zeros(gridsize)
cell_data[24,24]=10000

cellsize=windowsize/gridsize

# draw vertical lines
for i in range(gridsize[0]):
    pygame.draw.line(screen, "red", (cellsize[0] * (i + 1), 0), (cellsize[0] * (i + 1), windowsize[1]))

# draw horizontal lines
for i in range(gridsize[1]):
    pygame.draw.line(screen, "red", (0, cellsize[1] * (i + 1)), (windowsize[0], cellsize[1] * (i + 1)))

#draw grid
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = np.array(pygame.mouse.get_pos())
            #which cell is click in
            #integer division mouse pos by cellsize
            cell_pos=np.floor_divide(pos,cellsize)
            print(cell_pos)
            #increase cell by one
            cell_data[int(cell_pos[0]),int(cell_pos[1])]+=1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cell_data=updatecells(cell_data)

    screen.fill((0, 0, 0))
    # draw vertical lines
    for i in range(gridsize[0]):
        pygame.draw.line(screen, "red", (cellsize[0] * (i + 1), 0), (cellsize[0] * (i + 1), windowsize[1]))

    # draw horizontal lines
    for i in range(gridsize[1]):
        pygame.draw.line(screen, "red", (0, cellsize[1] * (i + 1)), (windowsize[0], cellsize[1] * (i + 1)))

    cell_data=updatecells(cell_data)
    display_cells(cell_data,cellsize,gridsize,screen)


    pygame.display.update()
    pygame.time.delay(10)

