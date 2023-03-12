import os
import time
from typing import Any, List


def go_to_path_return_directory(path=""):
    path_active = False
    try:
        if path == "":
            print()
            path = input("What is the path of your file?: ")
            path_active = True
        os.chdir(path)
        print(os.getcwd())
        os_walk_list = [x for x in os.listdir(os.getcwd())]
        dir_list = []
        print("Items in", path)
        for i in range(len(os_walk_list)):
            dir_list.append([i+1, os_walk_list[i]])
            print(dir_list[i])
        print()
        return dir_list
    except Exception as e:
        print("")
        print(e, "\nPath not found. Try again.")
        if path_active:
            dir_list = go_to_path_return_directory()
            return dir_list
        else:
            return



def main(recur=False):
    path_dir_list = go_to_path_return_directory()

    location = 0
    print("Is there a sub directory you'd like to access?")
    while location != -1:
        print("\nCurrent Directory:", os.getcwd())
        try:
            location = int(input("Type in the index number to access it.\n"
                                 "Type 0 to navigate / change path.\n"
                                 "Type -1 to continue in this current directory.\n"
                                 "Where do you want to go?: "))
            print(location)
            if location == 0:
                path_dir_list = go_to_path_return_directory()
            elif location == -1:
                continue
            elif location < -1 or location > len(path_dir_list):
                print("Number out of range. Try again")
            else:
                for i in range(len(path_dir_list)):
                    if path_dir_list[i][0] == location:
                        print("Found file:", path_dir_list[i][1])
                        path_dir_list = go_to_path_return_directory(os.getcwd() + "\\" + path_dir_list[i][1])
                        break
        except ValueError:
            print("Enter an integer. Try again.")
        except TypeError:
            print("Not a directory. Try again.")

    print("Chosen Directory: ", os.getcwd())
    time.sleep(1)

    choice = 0
    while choice != -1:
        try:
            print("      Directory Contents      ")
            print("==============================")
            for i in range(len(path_dir_list)):
                print("> ", path_dir_list[i][1])
            choice = int(input("Choose action.\n"
                               "Type 1 to pick the first item in the list to sort things by.\n"
                               "Type 0 to navigate / change path.\n"
                               "Type -1 to do nothing and end software.\n"
                               "What do you want to?: "))
            if choice == -1:
                if not recur:
                    print("Closing script.")
                continue
            elif len(path_dir_list) > choice > 0:
                temp_str_list: List[Any] = path_dir_list[0][1].split(" ")
                for j in range(len(temp_str_list)):
                    temp_str_list[j] = [j + 1, temp_str_list[j]]
                    print(temp_str_list[j])
                print("What range of strings do you want to move into a subdirectory?")
                str_range_one = 1
                str_range_two = 0

                if str_range_one > str_range_two:
                    while str_range_one > str_range_two:
                        str_range_one = int(input("For the first string, type its number here: ")) - 1
                        str_range_two = int(input("For the second string, type its number here."
                                                  "To keep it at only one string, write the same number here: "))
                        if str_range_one > str_range_two:
                            print("The first number cannot be greater than the second. Try again.")
                        elif str_range_one < 1 or str_range_two < 1:
                            print("One or both numbers out of range (Less than 1). Try again.")
                        elif str_range_one > len(temp_str_list) or str_range_two > len(temp_str_list):
                            print("One or both numbers out of range (Greater than "+str(len(temp_str_list))+"). Try again.")

                regex_string = ""
                for j in range(str_range_one, str_range_two):
                    if j != (str_range_two - 1):
                        regex_string += temp_str_list[j][1] + " "
                    else:
                        regex_string += temp_str_list[j][1]

                print(regex_string)

                for j in range(len(path_dir_list)):
                    pass
            elif choice == 0:
                main(True)
                if not recur:
                    print("Closing script.")
                return
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
