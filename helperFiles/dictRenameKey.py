# dict rename key:
# https://datascienceparichay.com/article/python-dictionary-rename-key/
# format:
my_dict[new_key] = my_dict.pop(old_key)

# Note: key's value MUST BE SAME!

# Example:   
# create a dictionary
capital_info = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "UK": "London"
}
# rename key in dictionary
capital_info["United States of America"] = capital_info.pop("USA")

# display the dictionary
print(capital_info)


