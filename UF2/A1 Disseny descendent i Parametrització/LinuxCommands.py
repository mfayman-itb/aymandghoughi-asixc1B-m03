#my own version

#region variables
import random
CMD = ('touch', 'grep', 'cat', 'fdisk', 'cmp', 'dmesg', 'man', 'top', 'htop', 'halt')
OPTIONS = ['-v', '-h', '--version', '--help']
LACABRA = (('v1.2', 'touch: Create an empty file.'), ('v2.5', 'grep: Search for patterns in files.'), ('v3.1', 'cat: Concatenate and display file contents.'), ('v1.8', 'fdisk: Manipulate disk partition tables.'), ('v2.3', 'cmp: Compare two files byte by byte.'), ('v1.6', 'dmesg: Display system message buffer.'), ('v2.0', 'man: Display manual pages for commands.'), ('v1.4', 'top: Display and update sorted information about processes.'), ('v3.2', 'htop: Interactive process viewer.'), ('v1.9', 'halt: Stop the system.'))
#endregion

#region functions
def get_random_greeting():
    greetings = [
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        "Bienvenido al nuevo sistema operativo en desarrollo.",
        "¿Cómo puedo servirte?",
        "¡Saludos! ¿Qué necesitas hacer?"
    ]
    return random.choice(greetings)
def cmd_input(CMD, OPTIONS):
    try:
        print(get_random_greeting())
        running = True
        while running:
            comand = input().split()
            if len(comand) >= 1:
                if comand[0] in CMD:
                    if len(comand) == 1:
                        if comand[0] == 'halt':
                            print('Halting the system...')
                            running = False  # Se detiene el bucle
                        else:
                            print(f'{comand[0]} needs one parameter. For instance -v or -h')
                            continue
                    else:
                        option = comand[1]
                        if option in OPTIONS:
                            if option == '--version':
                                option = '-v'
                            elif option == '--help':
                                option = '-h'
                            elif option == '-v' or option == '-h':
                                pass
                            else:
                                print(f'Invalid option: {option}')
                                continue
                        else:
                            print(f'Invalid option: {option}')
                            continue
                        comand[1] = option
                        cmd_exe(comand)
                else:
                    print(f'{comand[0]} command not found.')
            else:
                print(f'Need command')
    except Exception as e:
        print(e)
def cmd_exe(comand):
    fnc = CMD.index(comand[0])
    opt = OPTIONS.index(comand[1])
    print(LACABRA[fnc][opt])
#endregion

#region main
cmd_input(CMD, OPTIONS)
#endregion

#version2

