import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (2, 1, 0),
    (-2, 1, 0),
    (0, 1, 4),
    (2, -1, 0),
    (-2, -1, 0),
    (0, -1, 4)
)

edges = (
    (0, 1),
    (1, 2),
    (0, 2),
    (3, 4),
    (3, 5),
    (4, 5),
    (0, 3),
    (1, 4),
    (2, 5)
)

surfaces = (
    (0, 1, 2),
    (3, 4, 5),
    (0, 1, 3, 4),
    (0, 3, 2, 5),
    (1, 4, 2, 5)
)


def prism():
    glBegin(GL_QUADS)
    for surface in surfaces:
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,0))
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (500, 350)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        prism()
        pygame.display.flip()
        pygame.time.wait(10)


main()

# def main():
#     pygame.init()
#     display = (400, 450)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
#     glTranslatef(0.0, 0.0, -4)
#     glRotatef(0, 0, 0, 0)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         prism()

#     pygame.display.flip()
#     pygame.time.wait(10)


# main()
