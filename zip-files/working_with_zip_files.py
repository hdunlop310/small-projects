from zipfile import ZipFile
import os


def main():
    choice = input("What would you like to do: zip or unzip? ")
    if choice == "zip":
        zip()
    elif choice == "unzip":
        unzip()


def find_file():
    filename = input("Please enter the filename: ")
    return filename


def find_directory():
    directory = input("Please enter folder/directory name: ")
    return directory


def get_files(directory):
    paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            paths.append(path)
    return paths


def zip():
    directory_name = find_directory()
    files = get_files("./" + directory_name)
    print("The following files will be zipped: ")
    for file in files:
        print(file)

    with ZipFile(directory_name + ".zip", 'w') as f:
        print("Zipping file now...")
        for file in files:
            f.write(file)

    print("Done!")


def unzip():
    filename = find_file()
    with ZipFile(filename + ".zip", 'r') as f:
        print("Unzipping file now...")
        f.printdir()
        f.extractall()
    print("Done!")


if __name__ == "__main__":
    main()
