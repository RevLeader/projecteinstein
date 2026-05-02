print(f"\n{'#':<5} {'Course':<30} {'Duration'}\n")
print("-" * 45)
course_list = [
    ("Graphic Design",              "1 Year"),
    ("Software Development",        "2 Year"),
    ("Networking & Cybersecurity",  "2 Years")
]
for i, (course, duration) in enumerate(course_list, start=1):
    print(f"{i:<5} {course:<30} {duration}")

print()

#iloveyou@123