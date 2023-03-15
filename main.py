import os
import time
import shutil
from typing import Any, List


def go_to_path_return_directory(path=""):
    path_active = False
    try:
        if path == "":
            print()
            path = input("What is the path of your file?: ")
            path_active = True
        os.chdir(path)
        os_walk_list = [x for x in os.listdir(os.getcwd())]
        dir_list = []
        for i in range(len(os_walk_list)):
            dir_list.append([i + 1, os_walk_list[i]])
        return dir_list
    except Exception as e:
        print("")
        print(e, "\nPath not found. Try again.")
        if path_active:
            dir_list = go_to_path_return_directory()
            return dir_list
        else:
            return


def parentheses_check(regex_string):
    if any(x in ["(", ")", "[", "]"] for x in regex_string):
        answer = ""
        while not any(x in ["y", "n"] for x in answer):
            answer = input("This string has parentheses or brackets. "
                           "Do you want them removed in the new sub directory (y/n)?: ")
            if not any(x in ["y", "n"] for x in answer):
                print("That is not a 'y' or an 'n'. Try again.")
        if answer == "y":
            return os.getcwd() + "\\" + regex_string.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
        else:
            return os.getcwd() + "\\" + regex_string
    else:
        return os.getcwd() + "\\" + regex_string


def print_path_dir_list(path_dir_list):
    print("Items in", os.getcwd())
    for i in range(len(path_dir_list)):
        print(path_dir_list[i])


def yes_no_question(question):
    answer = ""
    while not any(x in ["y", "n"] for x in answer):
        answer = input(question)
        if not any(x in ["y", "n"] for x in answer):
            print("That is not a 'y' or an 'n'. Try again.")
    if answer == "y":
        return True
    else:
        return False

def main(recur=False):
    path_dir_list = go_to_path_return_directory()
    print_path_dir_list(path_dir_list)

    location = 0
    print("Is there a directory you'd like to access?")
    while location != -1:
        print("\nCurrent Directory:", os.getcwd())
        try:
            location = int(input("Type in the index number to access it.\n"
                                 "Type 0 to navigate / change path.\n"
                                 "Type -1 to continue in this current directory.\n"
                                 "Where do you want to go?: "))

            if location == 0:
                path_dir_list = go_to_path_return_directory()
                print_path_dir_list(path_dir_list)
            elif location == -1:
                continue
            elif len(path_dir_list) > location > 0:
                for i in range(len(path_dir_list)):
                    if path_dir_list[i][0] == location:
                        if os.path.isdir(os.getcwd() + "\\" + path_dir_list[i][1]):
                            print("\nFound directory:", path_dir_list[i][1])
                            path_dir_list = go_to_path_return_directory(path=os.getcwd() + "\\" + path_dir_list[i][1])
                            break
                        else:
                            print("\nNot a directory. Try again.")
                            break
                print_path_dir_list(path_dir_list)
            else:
                print("Number out of range. Try again")
        except ValueError:
            print("Enter an integer. Try again.")
        except TypeError:
            print("Not a directory. Try again.")

    choice = 0
    for i in range(len(path_dir_list)):
        path_dir_list[i]: List[Any] = [path_dir_list[i][0], path_dir_list[i][1]]

    while choice != -1:
        try:
            print("\n\n\n      " + os.path.basename(os.getcwd()) + " Contents      ")
            line_str = ""
            for i in range(len(os.path.basename(os.getcwd()))):
                line_str += "="
            print("=====================" + line_str)
            for i in range(len(path_dir_list)):
                file_list_str = ">  Index: " + str(path_dir_list[i][0])
                if os.path.isfile(path_dir_list[i][1]):
                    file_list_str += "   File: " + path_dir_list[i][1]
                else:
                    file_list_str += "   Directory: " + path_dir_list[i][1]
                print(file_list_str)
            print("> ", "Current Directory:", os.path.basename(os.getcwd()))
            choice = int(input("Choose an action.\n"
                               "Type the index of the item to sort things by.\n"
                               "If it's a directory, it will search for everything with its name in it.\n"
                               "Type 0 to navigate / change path.\n"
                               "Type -1 to do nothing and end software.\n"
                               "Type -2 to insert your own string to search by.\n"
                               "Type -3 to sort everything into its own subfolder by country\n"
                               "Hint: To refresh list, type 0 then '.' then -1.\n"
                               "What do you want to?: "))
            if choice == 0 or choice == -1:
                if choice == 0:
                    main(True)
                    return
                if not recur:
                    print("Closing script.")
                return
            elif len(path_dir_list) >= choice > 0 or choice == -2 or choice == -3:
                if choice != -3:
                    temp_str_list: List[Any] = []
                    temp_dir = ""

                    for i in range(len(path_dir_list)):
                        if path_dir_list[i][0] == choice:
                            if os.path.isfile(os.getcwd() + "\\" + path_dir_list[i][1]):
                                print("\nFound file: ", path_dir_list[i][1])
                                temp_str_list = os.path.splitext(path_dir_list[i][1])[0].split(" ")
                                break
                            else:
                                print("\nFound directory: ", path_dir_list[i][1])
                                temp_dir = path_dir_list[i][1]
                                break

                    if temp_dir == "" and choice != -2:
                        for i in range(len(temp_str_list)):
                            temp_str_list[i] = [i + 1, temp_str_list[i]]
                            print(temp_str_list[i])

                        print("\nWhat range of strings do you want to move into a subdirectory?"
                              "\nIf you want to return to pick a new option, enter 0 on either option.")
                        str_range_one = -1
                        str_range_two = -1
                        back_to_list_flag = False

                        while not (str_range_two >= str_range_one > 0) and not back_to_list_flag:
                            try:
                                str_range_one = int(input("For the first string, type its number here: "))
                                str_range_two = int(input("For the second string, type its number here. "
                                                          "To keep it at only one string, write the same number here: "))

                                if str_range_one == 0 or str_range_two == 0:
                                    print("\nReturning to previous menu...")
                                    back_to_list_flag = True
                                elif not len(temp_str_list) >= str_range_one > 0 or not len(
                                        temp_str_list) >= str_range_one > 0:
                                    print("\nOne or both numbers out of range. Try again.")
                                elif str_range_one > str_range_two:
                                    print("The first number cannot be greater than the second. Try again.")
                            except ValueError:
                                print("Enter an integer. Try again.")

                        if back_to_list_flag:
                            continue

                        regex_string = ""
                        for i in range(str_range_one - 1, str_range_two):
                            if i != (str_range_two - 1):
                                regex_string += temp_str_list[i][1] + " "
                            else:
                                regex_string += temp_str_list[i][1]
                        filename = parentheses_check(regex_string)

                    elif choice == -2:
                        regex_string = input("What string would you like to search by?: ")
                        filename = parentheses_check(regex_string)

                    else:
                        regex_string = temp_dir
                        filename = os.getcwd() + "\\" + regex_string
                        question = "When searching for files with the directory's name " + regex_string + ", did you" \
                                   " want parentheses on the directory name to search through files (y/n)?: "
                        answer = yes_no_question(question)
                        if answer:
                            regex_string = "(" + regex_string + ")"

                    print("\nSorting items by:", regex_string)
                    print("Filename directory: ", filename)
                    time.sleep(1)
                    print("Starting...")
                    time.sleep(1)

                    if not os.path.exists(filename):
                        print("Creating new directory:", filename)
                        os.makedirs(filename)
                        time.sleep(1)

                    file_list = []
                    for i in range(len(path_dir_list)):
                        if not os.path.isfile(os.getcwd() + "\\" + path_dir_list[i][1]):
                            pass
                        else:
                            if regex_string in path_dir_list[i][1]:
                                file_list.append(path_dir_list[i][1])

                    if len(file_list) == 0:
                        print("No files with", regex_string, "exist in", os.getcwd(), ".")
                        continue

                    print("\nGames found")
                    print("===========")
                    for i in range(len(file_list)):
                        print(file_list[i])

                    print("\nMoving files...")
                    time.sleep(1)
                    for i in range(len(file_list)):
                        shutil.move(os.getcwd() + "\\" + file_list[i], filename + "\\" + file_list[i])

                    path_dir_list = go_to_path_return_directory(os.getcwd())
                    for i in range(len(path_dir_list)):
                        path_dir_list[i]: List[Any] = [path_dir_list[i][0], path_dir_list[i][1]]
                else:
                    with open(__file__ + "\\..\\regionlist.txt") as f:
                        region_list = [line.strip() for line in f]
                    region_list.pop(0)
                    print(region_list)

                    question = "Did you want to remove parentheses and brackets from the new directories (y/n)?: "
                    answer = yes_no_question(question)

                    print("Automating sorting of currently available regions and BIOS: ")
                    for i in range(len(region_list)):
                        print(region_list[i])

                    print("\nMoving files...")
                    time.sleep(1)
                    temp_dir_list: List[Any] = path_dir_list.copy()
                    for i in range(len(region_list)):
                        current_region = region_list[i]
                        if answer:
                            temp_dir = os.getcwd() + "\\" + region_list[i].replace("(", "").replace(")", "").replace("[", "").replace("]", "")
                        else:
                            temp_dir = os.getcwd() + "\\" + region_list[i]

                        for j in range(len(temp_dir_list) - 1, -1, -1):
                            if current_region in temp_dir_list[j][1]:
                                if not os.path.exists(temp_dir):
                                    print("Creating new directory:", temp_dir)
                                    os.makedirs(temp_dir)
                                print("Moving", temp_dir_list[j][1])
                                shutil.move(os.getcwd() + "\\" + temp_dir_list[j][1], temp_dir + "\\" + temp_dir_list[j][1])
                                temp_dir_list.pop(j)

                        print("Things left in list", temp_dir_list)

                    path_dir_list = go_to_path_return_directory(os.getcwd())
                    for i in range(len(path_dir_list)):
                        path_dir_list[i]: List[Any] = [path_dir_list[i][0], path_dir_list[i][1]]

                    print("Region and BIOS move complete!")

        except ValueError:
            print("Enter an integer. Try again.")


if __name__ == '__main__':
    main()
