import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 6),
    (5, 1),
    (5, 4),
    (5, 6),
    (7, 3),
    (7, 4),
    (7, 6),
)

surfaces = (
    (0, 1, 2, 3),
    (0, 1, 5, 4),
    (4, 5, 6, 7),
    (7, 6, 2, 3),
    (0, 4, 7, 3),
    (1, 5, 6, 2)
)
colors = (
    (.3, .4, 0),
    (0, 1, 1),
    (0, 1, 0),
    (0, 1, 0),
    (1, .2, .4),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0)
)

# Cube thing.
def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x=0
        for vertex in surface:
            glColor3fv(colors[x])
            x += 1
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


# Main game block/loop
def main():
    pygame.init()
    display = (500, 350)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), .01, 50.0)
    glTranslatef(0.0, 0.0, -12)
    glRotatef(0, 0, 0, 0)

    camera_hit = False

    while not camera_hit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, .5, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -.5, 0)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         glTranslatef(0, 0, 1.0)
            #     if event.button == 5:
            #         glTranslatef(0, 0, -1.0)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glTranslatef(0, 0, .1)
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        # print(str(x))
        camera_z = x[3][2]
        if camera_z < -1:
            camera_hit = True
            print(camera_z)
            print("again")

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

for x in range(10):
    main()

# pygame.quit()
# quit()
