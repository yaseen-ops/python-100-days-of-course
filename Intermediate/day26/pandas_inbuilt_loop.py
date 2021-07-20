import pandas

student_dict = {
    "student": ["Sachin", "Dhoni", "Kohli"],
    "score": [79, 83, 80],
}

print("## get key and value in a dict ##")
for (key, value) in student_dict.items():
    print(key)
    print(value)

print("\n## looping in a pandas dataframe ##")
df = pandas.DataFrame(student_dict)
for (key, value) in df.items():
    print(key)
    print(value)

print("\n## Loop through rows of a data frame ##")
print("        ##printing Index numbers##")
for (index, row) in df.iterrows():
    print(index)
print("        ##printing rows##")
for (index, row) in df.iterrows():
    print(row)
print("        ##printing value of rows##")
for (index, row) in df.iterrows():
    print(row.student)
for (index, row) in df.iterrows():
    print(row.score)
print("      ##gettting score of a particular person##")
for (index, row) in df.iterrows():
    if row.student == "Dhoni":
        print(row.score)

print("\n\n## Creating a new dictionary from a dataframe ##")
new_dict = {row.student: row.score for (index, row) in df.iterrows()}
print(new_dict)
