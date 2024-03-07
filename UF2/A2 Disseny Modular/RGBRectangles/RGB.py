from syscolors.sysColors import SystemColors

def get_rectangles():
    rectangles = []
    while True:
        rectangle_input = input().upper()
        if ';Q' in rectangle_input:
            break
        rectangles.append(rectangle_input.split())
    return rectangles

def draw_rectangle(color, height, width):
    color_code = SystemColors[color.upper()]
    for i in range(height):
        for j in range(width):
            print(f'\x1b[6;30;{color_code}m' + 'X' + '\x1b[0m', end="")
        print()

rectangles = get_rectangles()
