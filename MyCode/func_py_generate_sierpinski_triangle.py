# func_py_generate_sierpinski_triangle.py
import turtle

def func_py_generate_sierpinski_triangle(length, depth):
    if depth == 0:
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        func_py_generate_sierpinski_triangle(length/2, depth-1)
        turtle.forward(length/2)
        func_py_generate_sierpinski_triangle(length/2, depth-1)
        turtle.backward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        func_py_generate_sierpinski_triangle(length/2, depth-1)
        turtle.left(60)
        turtle.backward(length/2)
        turtle.right(60)

turtle.speed("fastest")
func_py_generate_sierpinski_triangle(200, 4)
turtle.done()
