import os

def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        print(prefix + path)


if __name__ == "__main__":
    root_dir = 'C:\\Users\\alal3\\OneDrive\\바탕 화면\\test'
    print_files_in_dir(root_dir, "")
