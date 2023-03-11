import os
import pathlib
from pathlib import Path


def go_to_path_return_directory(path=""):
    try:
        if path == "":
            path = input("What is the path of your file?: ")
        os.chdir(path)
        print(os.getcwd())
        os_walk_list = [x for x in os.listdir(os.getcwd())]
        dir_list = []
        print("Items in", path)
        for i in range(len(os_walk_list)):
            dir_list.append([i, os_walk_list[i]])
            print(dir_list[i])
        print()
        return dir_list
    except Exception as e:
        print("")
        print(e, "\nPath not found. Try again.")
        os_walk_list = go_to_path_return_directory()
        return os_walk_list


def main():
    path_dir_list = go_to_path_return_directory()

    location = 0
    found_index = False
    print("Is there a sub directory you'd like to access?\n")
    while location != -2 or not found_index:
        print("Current Directory:", os.getcwd())
        try:
            location = int(input("Type in the index number to access it.\n"
                                 "Type -1 to navigate / change absolute path.\n"
                                 "Type -2 to continue in this current directory.\n"
                                 "Where do you want to go?: "))
            if location == -1:
                path_dir_list = go_to_path_return_directory()
            elif location == -2:
                continue
            elif location < -2:
                print("Number invalid. Try again")
            else:
                for i in range(len(path_dir_list)):
                    if path_dir_list[i][0] == location:
                        os.chdir(path_dir_list[i][1])
                        found_index = True
                if not found_index:
                    print("Index not found. Try again.")

        except ValueError as e:
            print("Enter an integer. Try again.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
