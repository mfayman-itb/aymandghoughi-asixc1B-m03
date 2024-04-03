def print_menu(options):
    print("Menú:")
    for i, option in enumerate(options, start=1):
        print(f"{i} - {option}")

def print_sub_menu(options):
    print("Submenú:")
    for i, option in enumerate(options, start=1):
        print(f"{i} - {option}")

def get_input(prompt):
    return input(prompt)
