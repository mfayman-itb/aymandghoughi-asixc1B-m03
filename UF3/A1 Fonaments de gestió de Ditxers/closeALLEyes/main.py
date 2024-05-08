"""
Description: Llegir tots els fitxers  *.in i crear el fitxer de sortida, amb el mateix mon acabat en "Closed" *Closed.out amb el mateix contingut.
Però els ulls del drac que al fitxer d'entrada estan oberts 0   0 , i al de sortida hauran d'estar tancats -    - o també per uns '👁' '👁'

Usage:
Input --> Directory (File.txt)
"""

import os

inputDir = os.path.join('.', 'pictures')
outputDir = os.path.join('.', 'picturesClosed')

def replace_eyes(content):
    content = content.replace('0 = 0', '👁=👁')
    content = content.replace('0 \ 0', '👁 \ 👁')
    return content


def process_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.in'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                modified_content = replace_eyes(content)
                write_processed_files(modified_content, directory, file)

def write_processed_files(modified_content, directory, file):
    output_filename = file.replace('.in', 'Closed.out')
    with open(os.path.join(directory, output_filename), 'w', encoding='utf-8') as f:
        f.write(modified_content)

def main():
    if not os.path.exists(outputDir):
        os.mkdir(os.path.join('.', 'picturesClosed'))
    process_files(inputDir)

if __name__ == "__main__":
    main()
