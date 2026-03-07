#Напишите функцию draw_triangle(), которая выводит звёздный прямоугольный треугольник с катетами, равными 10

def draw_triangle():
    for i in range(1, n + 1):
        print('*' * i)

n = 10
draw_triangle()