def write_file(data):
    with open ('file.csv', 'a') as file:
        return file.writelines(data)

def read_file():
    with open ('file.csv', 'r') as file:
        return file.readlines()