#region variables i constants
CMD = ('touch', 'grep', 'cat', 'fdisk', 'cmp', 'dmesg', 'man', 'top', 'htop', 'halt')
OPTIONS = ('-v', '--version', '-h, --help')
LACABRA = bash_commands_help = (('v1.2', 'touch: Create an empty file.'), ('v2.5', 'grep: Search for patterns in files.'), ('v3.1', 'cat: Concatenate and display file contents.'), ('v1.8', 'fdisk: Manipulate disk partition tables.'), ('v2.3', 'cmp: Compare two files byte by byte.'), ('v1.6', 'dmesg: Display system message buffer.'), ('v2.0', 'man: Display manual pages for commands.'), ('v1.4', 'top: Display and update sorted information about processes.'), ('v3.2', 'htop: Interactive process viewer.'), ('v1.9', 'halt: Stop the system.'))
def cmd_input(CMD):
    comand = input().split()
    if comand == 'halt':
        return comand
    elif len(comand) != 1:
        if comand[0] in CMD and comand[1] in OPTIONS:
            return comand
        else:
            print(f'{comand} command not found.')
    else:
        print(f'need options')
def cmd_exe(comand):
