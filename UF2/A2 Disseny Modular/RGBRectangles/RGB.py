import systemColors as sc

def rectangle_colors(color, lenght, width)
    color_dict = {
        'RED' : sc.CRED,
        'WHITE' : sc.CWHITE,
        'YELLOW' : sc.CYELLOW,
        'GREEN' : sc.CGREEN

    }

def get_rectangles():
    rectangles = []
    while rectangles != ';Q':
        rectangle_input = input().upper()
        rectangles.append(rectangle_input.split())
    return rectangles

def draw_rectangle(color, height, width):
    color_code = SystemColors[color.upper()]
    for i in range(height):
        for j in range(width):
            print(f'\x1b[6;30;{color_code}m' + 'X' + '\x1b[0m', end="")
        print()

rectangles = get_rectangles()
