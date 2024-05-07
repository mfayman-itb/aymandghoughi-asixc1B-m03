import os

def replace_eyes(content):
    content = content.replace('0 = 0', '👁=👁')
    content = content.replace('0 \ 0', '👁 \ 👁')
    return content


def process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.in'):
            with open(os.path.join(directory, filename), 'r') as file:
                content = file.read()
            modified_content = replace_eyes(content)
            output_filename = filename.replace('.in', 'Closed.out')
            with open(os.path.join(directory, output_filename), 'w') as file:
                file.write(modified_content)

def main():
    process_files('pictures')

if __name__ == "__main__":
    main()
