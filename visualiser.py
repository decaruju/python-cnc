import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_lines(lines):
    glBegin(GL_LINES)
    last_x = 0
    last_y = 0
    last_z = 0
    for start, end in zip(lines[:-1], lines[1:]):
        glVertex3fv((start.get('x', last_x), start.get('y', last_y), start.get('z', last_z)))
        glVertex3fv((end.get('x', last_x), end.get('y', last_y), end.get('z', last_z)))
        if 'x' in end:
            last_x = end['x']
        if 'y' in end:
            last_x = end['y']
        if 'z' in end:
            last_x = end['z']
    glEnd()

def parse_line(line):
    if 'G1' in line:
        out = {}
        for coord in line.split(' '):
            if 'X' in coord:
                out['x'] = float(coord[1:])
            if 'Y' in coord:
                out['y'] = float(coord[1:])
            if 'Z' in coord:
                out['z'] = float(coord[1:])
        return out


def main():
    with open('out.nc', 'r') as f:
        code = f.readlines()
    vertices = [coord for line in code if (coord := parse_line(line))]
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)

    glTranslatef(0.0,0.0, -50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_lines(vertices)
        pygame.display.flip()
        pygame.time.wait(10)


main()
