# file_copier.py
def copy_file(src, dst):
    with open(src, 'rb') as source_file:
        with open(dst, 'wb') as dest_file:
            dest_file.write(source_file.read())

if __name__ == "__main__":
    src = input("Enter the source file path: ")
    dst = input("Enter the destination file path: ")
    copy_file(src, dst)
    print(f"Copied content from {src} to {dst}")
