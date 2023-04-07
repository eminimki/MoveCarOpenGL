#! /usr/bin/env python
'''
23 Bahar Dönemi Bilgisayar Grafikleri Dersi Vize Projesi
Muhammed Emin Ay 20120205038 07.04.2023 @eminimki
Ders notlarından alıntılar yapılmıştır.
'''
import math

from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0
deltax = 0.0
deltay = 0.0
cam_boyasi = [0.1, 1, 1]
kapi_boyasi = [1,0,0]


# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):  # We call this right after our OpenGL window is created.
    glClearColor(1.0, 1.0, 1.0, 1.0)  # This Will Clear The Background Color To Black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)



# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(5.0, -5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)


# The main drawing function.
def DrawGLScene():
    #global deltax
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset The View

    # Gunes
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_POLYGON)
    for vertex in range(0, 720):
        angle = float(vertex) * 1 * math.pi / 360
        glVertex3f(4.0 + math.cos(angle) * 0.5, 4.0 + math.sin(angle) * 0.5, 0.0)
    glEnd()

    # Agac govdesi
    glColor3f(0.75, 0.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-3.6, -0.7)
    glVertex2f(-3.6, 1.5)
    glVertex2f(-4.1, 1.5)
    glVertex2f(-4.1, -0.7)
    glEnd()

    # Agac Yapraklari
    glColor3f(0.01, 0.5, 0.32)
    glBegin(GL_POLYGON)  # Start drawing a polygon
    glVertex3f(-3.85, 3.0, 0.0)  # Top
    glVertex3f(-4.6, 1.5, 0.0)  # Bottom Right
    glVertex3f(-3.1, 1.5, 0.0)  # Bottom Left
    glEnd()  # We are done with the polygon




    # Yol
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(5.0, -0.7)
    glVertex2f(-5.0, -0.7)
    glEnd()

    # Yolun altindai cim alan
    glColor3f(0.5, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(5.0, -0.7)
    glVertex2f(-5.0, -0.7)
    glVertex2f(-5.0, -5.0)
    glVertex2f(5.0, -5.0)
    glEnd()



    glTranslatef(deltax, deltay, 0.0)


    # Kapi Boyasi
    r = kapi_boyasi[0]
    g = kapi_boyasi[1]
    b = kapi_boyasi[2]
    glColor3f(r, g, b)

    glBegin(GL_POLYGON)
    glVertex2f(0.5, 0)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 0)
    glVertex2f(-0.5, 0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 0)
    glEnd()

    r = cam_boyasi[0]
    g = cam_boyasi[1]
    b = cam_boyasi[2]
    glColor3f(r, g, b)

    glBegin(GL_POLYGON)
    glVertex2f(-0.25, 0)
    glVertex2f(-0.25, 0.5)
    glVertex2f(0.25, 0.5)
    glVertex2f(0.25, 0)
    glEnd()

    # Arka Kapi Cerceve
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5, 0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 0)
    glEnd()

    # On Kapi Cerceve
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.5, 0)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 0)
    glEnd()

    # Cam Cerceve
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.25, 0)
    glVertex2f(-0.25, 0.5)
    glVertex2f(0.25, 0.5)
    glVertex2f(0.25, 0)
    glEnd()

    # Arka Teker
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertex in range(0, 720):
        angle = float(vertex) * 1 * math.pi / 360
        glVertex3f(-0.35 + math.cos(angle) * 0.1, -0.6 + math.sin(angle) * 0.1, 0.0)
    glEnd()

    # On Teker
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertex in range(0, 720):
        angle = float(vertex) * 1 * math.pi / 360
        glVertex3f(0.35 + math.cos(angle) * 0.1, -0.6 + math.sin(angle) * 0.1, 0.0)
    glEnd()
    glFlush()


    glutSwapBuffers()


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    global deltax
    global deltay
    # If escape is pressed, kill everything.
    if args[0]  == b"a" :
        if deltax <4:
            deltax+=1
    elif args[0]  == b"d" :
        if deltax > -3:
            deltax-=1
    glutPostRedisplay()


def on_click( button, state, x, y):
    global deltax
    global deltay
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            if deltax <4:
                deltax+=1
    elif button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            if deltax > -3:
                deltax-=1
    else:
        print("Algılanamayan mouse aktivitesi")



def main():
    global window
    glutInit(sys.argv)

    # Select type of Display mode:
    #  Double buffer
    #  RGBA color
    # Alpha components supported
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE )

    # get a 640 x 480 window
    glutInitWindowSize(640, 480)

    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

    # Okay, like the C version we retain the window id to use when closing, but for those of you new
    # to Python (like myself), remember this assignment would make the variable local and not global
    # if it weren't for the global declaration at the start of main.
    window = glutCreateWindow(b"Muhammed Emin Ay 20120205038 - @eminimki")

    # Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
    # set the function pointer and invoke a function to actually register the callback, otherwise it
    # would be very much like the C version of the code.
    glutDisplayFunc(DrawGLScene)

    # Uncomment this line to get full screen.
    # glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    #mouse aktivitesini okur
    glutMouseFunc(on_click)
    # Initialize our window.
    InitGL(640, 480)

    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()