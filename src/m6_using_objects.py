"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and James (Bo) Geyer.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    two_circles()
    circle_and_rectangle()
    lines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():

    window = rg.RoseWindow(500,500)
    point1 = rg.Point(150,150)
    circle1 = rg.Circle(point1,100)
    circle1.fill_color = 'red'
    point2 = rg.Point(300,300)
    circle2 = rg.Circle(point2,70)

    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()



    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    window = rg.RoseWindow()
    point1 = rg.Point(100,100)
    point2 = rg.Point(250,150)
    point3 = rg.Point(300,250)
    circle1 = rg.Circle(point1,80)
    circle1.fill_color='blue'
    rectangle1 = rg.Rectangle(point2,point3)

    point4 = rectangle1._upper_right_corner
    point5 = rectangle1._upper_left_corner
    point6 = rectangle1._lower_right_corner
    a = (point4.x - point5.x) / 2
    b = (point6.y - point4.y) / 2

    center = rg.Point(a,b)



    print('',circle1.outline_thickness,'\n',circle1.fill_color,'\n',circle1.center,'\n',point1.x,'\n',point1.y)
    print('',rectangle1.outline_thickness,'\n',rectangle1.fill_color,'\n',center,'\n',a,'\n',b,'\n')

    circle1.attach_to(window)
    rectangle1.attach_to(window)



    window.render()

    window.close_on_mouse_click()

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    window = rg.RoseWindow()
    point1 = rg.Point(50,50)
    point2 = rg.Point(100,100)
    point3 = rg.Point(150, 150)
    point4 = rg.Point(200, 200)

    line1 = rg.Line(point1, point2)
    line2 = rg.Line(point3, point4)
    line2.thickness = 5
    point5 = line2.get_midpoint()

    print('',line2.get_midpoint(),'\n',point5.x,'\n',point5.y)

    line1.attach_to(window)
    line2.attach_to(window)

    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
