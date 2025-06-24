import re


def match_string(pattern, text):
    arr = text.split(" ")
    for item in arr:
        match = re.match(pattern, item)
        if match:
            print(f"{item} matches the pattern")
        else:
            print(f"{item} does not match the pattern")


# text = "ab abbb ab a abb ab sahb sajha sd sh ds jdjskd sdkd b"

# 1

# pattern = r"ab*"

# 2

# pattern = r"a(bb|bbb)"

# 3

# pattern = r"\b[a-z]+_[a-z]+\b"
# text = "abc def abc_def Aabc_def abc_defA"
# print(re.findall(pattern, text))

# 4

# text = "Hello World, this is a Python Program"
# pattern = r"[A-Z][a-z]+"

# match_string(pattern, text)


# 5

# text = "abcdefg hi, jklmn b"
# pattern = r"^a.*b$"
# print("matched" if re.match(pattern, text) else "not matched")

# print("#########################################")

# 6

# pattern = r"[ ,.]"
# text = "abcdefg hi, jklmn b"
# print(re.sub(pattern, ":", text))


# 7


# def snake_to_camel(snake):
#     words = snake.split("_")
#     return words[0] + "".join(word.capitalize() for word in words[1:])


# text = "hello_world"
# print(snake_to_camel(text))


# 8

# pattern = r"[A-Z]?[a-z]*"
# text = "SplitThisStringAtUppercaseLetters"
# result = re.findall(pattern, text)
# print([word[1::] for word in result])
