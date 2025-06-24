import os

path = "/Users/Qushtar/Desktop/Code/Python"


# 1
# def list_directories_and_files(path):
#     dirs = []
#     files = []
#     all = []

#     items = os.listdir(path)

#     for item in items:
#         full_path = os.path.join(path, item)
#         all.append(full_path)

#         if os.path.isfile(full_path):
#             files.append(full_path)

#         if os.path.isdir(full_path):
#             dirs.append(full_path)
#             # sub_dirs, sub_files, sub_all = list_directories_and_files(full_path)
#             # dirs.append(sub_dirs)
#             # files.append(sub_files)
#             # all.append(sub_all)

#     return dirs, files, all


# dirs, files, all = list_directories_and_files(path)

# print("Dirs:")
# for dir in dirs:
#     print(dir)


# print("Files:")
# for file in files:
#     print(file)


# 2
# def check_path_access(path):
#     access_info = {
#         "exists": os.path.exists(path),
#         "readable": os.access(path, os.R_OK),
#         "writable": os.access(path, os.W_OK),
#         "executable": os.access(path, os.X_OK),
#     }
#     return access_info


# access_info = check_path_access(path)
# print(access_info)


# 3
# def check_path(path):
#     if os.path.exists(path):
#         directory, filename = os.path.split(path)
#         return True, directory, filename
#     else:
#         return False, None, None


# exists, directory, filename = check_path(path)

# if exists:
#     print("Path exists")
#     print("Directory:", directory)
#     print("Filename:", filename)
# else:
#     print("Path does not exist.")


# 4
# def count_lines(file):
#     with open(file, "r") as content:
#         line_count = 0
#         for _ in content:
#             line_count += 1
#     return line_count


# file = "words.txt"
# lines = count_lines(file)
# print(lines)


# 5
# def write_list_to_file(file_name, list):
#     with open(file_name, "w") as file:
#         for item in list:
#             file.write(item)


# list = ["first item", "second item"]
# write_list_to_file("output.txt", list)

# 6
# import string


# def generate_files():
#     letters = string.ascii_uppercase

#     for letter in letters:
#         file_path = f"files/{letter}.txt"

#         dir = os.path.dirname(file_path)
#         if not os.path.exists(dir):
#             os.makedirs(dir)

#         with open(file_path, "w") as file:
#             file.write("There should be some text")


# generate_files()


# 7


# def copy_file(path, dest_path):
#     with open(path, "r") as content:
#         with open(dest_path, "w") as dest:
#             dest.write(content.read())


# file_path = "/Users/Qushtar/Desktop/Code/Python/PP2/lab6/words.txt"
# dest_path = "/Users/Qushtar/Desktop/Code/Python/PP2/lab6/words_copy.txt"

# copy_file(file_path, dest_path)


# 8


def delete_file(path):
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception as e:
        print("No delete access")


file_path = "/Users/Qushtar/Desktop/Code/Python/PP2/lab6/output.txt"

delete_file(file_path)
