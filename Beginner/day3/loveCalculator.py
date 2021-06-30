first_name = input("Enter a male name : ").lower()
second_name = input("Enter a female name : ").lower()

combined_name = first_name + second_name
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
number_one = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
number_two = l + o + v + e

love_score = int(str(number_one) + str(number_two))

if love_score < 10 or love_score >= 90:
    print(f"Your Score Is {love_score}, You are doing great")
elif love_score >= 40 and love_score <= 50:
    print(f"Your Score Is {love_score}, you are doing fine")
else:
    print(f"Your Score Is {love_score}, you are doing not bad")
