#region variables i constants
CMD = ('touch', 'grep', 'cat', 'fdisk', 'cmp', 'dmesg', 'man', 'top', 'htop', 'halt')
OPTIONS = ['-v', '-h', '--version', '--help']
LACABRA = (('v1.2', 'touch: Create an empty file.'), ('v2.5', 'grep: Search for patterns in files.'), ('v3.1', 'cat: Concatenate and display file contents.'), ('v1.8', 'fdisk: Manipulate disk partition tables.'), ('v2.3', 'cmp: Compare two files byte by byte.'), ('v1.6', 'dmesg: Display system message buffer.'), ('v2.0', 'man: Display manual pages for commands.'), ('v1.4', 'top: Display and update sorted information about processes.'), ('v3.2', 'htop: Interactive process viewer.'), ('v1.9', 'halt: Stop the system.'))
#endregion

#region functions
def cmd_input(CMD, OPTIONS):
    try:
        comand = [0]
        while comand[0] != 'halt':
            comand = input().split()
            if len(comand) != 1:
                if comand[0] in CMD and comand[1] in OPTIONS:
                    if comand[1] == '--version':
                        comand.pop(-1)
                        comand.append('-v')
                    else:
                        comand.pop(-1)
                        comand.append('-h')
                    OPTIONS.pop(-1)
                    OPTIONS.pop(-1)
                    cmd_exe(comand)
                elif comand[0] in CMD and comand[1] not in OPTIONS:
                    print(f'Value {comand[1]} is not valid option')
                else:
                    print(f'{comand} command not found.')
            elif comand[0] != 'halt' and comand[0] in CMD:
                print(f'{comand[0]} needs one paramater. For instance -v or -h')
            else:
                print(f'need options')
    except Exception as e:
        print(e)
def cmd_exe(comand):
    fnc = CMD.index(comand[0])
    opt = OPTIONS.index(comand[1])
    print(LACABRA[fnc][opt])

#region main
cmd_input(CMD, OPTIONS)
#endregion