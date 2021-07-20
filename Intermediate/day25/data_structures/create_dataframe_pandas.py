import pandas

data_dict = {
    "students": ["Sachin", "Dhoni", "Yuvraj"],
    "scores": [65, 76, 55],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")