# Basic Dictionary Operations

# student = {
#     "name": "John",
#     "age": 20,
#     "grades": [85,90,92]
# }
# print("Name: ",student["name"])

# student["major"] = "Computer Science"
# print("Name: ",student["major"])

# for key, value in student.items():
#     print(f"{key}:{value}")

# del (student["age"]) 
# print("After deletion: ", student)


# Using Tuples as Values in a Dictionary

# employee_skills = {
#     "Alice": ("AWS", "Docker", "Python"),
#     "Bob": ("Java", "K8s", "SQL")
# }
# print("Employee Skills: ", employee_skills["Alice"])


# Nesting Tuples and Dictionaries

company = {
    "employees": {
        "Alice": {
            "age": 30,
            "skills": ("Python", "Docker")
        },
        "Bob": {
            "age": 35,
            "skills": ("Java", "C++")
        }
    },
    "Location": "USA"
}
print("Company Alice Skills are: ", company["employees"]["Alice"]["skills"])