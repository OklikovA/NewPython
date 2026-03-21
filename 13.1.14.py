#Напишите функцию draw_triangle(), которая выводит звёздный прямоугольный треугольник с катетами, равными 10
#Переписать функцию draw_triangle(), которая выводит звёздный равносторонний треугольник с катетами


def draw_triangle(n, simvol):
    for i in range(1, (n + 1) // 2 + 1):
        print(simvol * i)
    for i in range((n + 1) // 2 - 1, 0, -1):
        print(simvol * i)

n = 13
simvol = '#'

draw_triangle(n, simvol)