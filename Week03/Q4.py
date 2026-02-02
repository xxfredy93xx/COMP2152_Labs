monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Both classes: {monday_class & wednesday_class}") #shift + 7
print(f"Attended either classes: {monday_class | wednesday_class}") # | = pipe, shift + \
print(f"Only monday: {monday_class - wednesday_class}")
print(f"only one class: {monday_class ^ wednesday_class}")# ^ = caret, shift + 6
all_students = monday_class | wednesday_class
print(f"is monday subset of all students: ", monday_class <= all_students)