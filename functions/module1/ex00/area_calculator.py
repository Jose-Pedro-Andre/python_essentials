#!/usr/bin/python3 
# execute the code as script


"""
    Write a function area_rectangle(width, height) that returns the area of a rectangle. Then write a
    second function area_circle(radius) that returns the area of a circle. Both must include a docstring
    explaining what they do
"""
import sys

def area_rectangule(width, heigth):
    """
    This function calcule the area of the retangule. it receive two date(width and height) and return a integer as result
    """
    area = width * heigth
    return area
def area_circle(radius):
    """
    This function calcule the area of the circle. it receive two date(width and height) and return a integer as result
    """
    area = 3.14 * (radius * radius)
    return area