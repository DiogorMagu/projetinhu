import os

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
        
def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data

def main():
    folder_name = 'example'
    create_folder(folder_name)
    file_name = 'example.txt'
    file_path = os.path.join(folder_name, file_name)
    write_file(file_path, 'example data')
    data = read_file(file_path)
    print(data)

if __name__ == '__main__':
    main()
