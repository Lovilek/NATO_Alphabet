# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
import pandas

#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
print(dictionary)

value = True
while value:
    try:
        word = input("Enter the word: ").upper()
        letters = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        value = False
        print(letters)
