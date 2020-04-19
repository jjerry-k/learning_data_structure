# Dictionary

grades = {}

# key - value
grades["현승"] = 80
grades["태호"] = 60
grades["영훈"] = 90
grades["지웅"] = 70
grades["동욱"] = 96
print(grades)
grades["태호"] = 100
print(grades)

# Searching using key
print(grades["동욱"])
print(grades["현승"])

# Deleting using key
grades.pop("태호")
print(grades)
grades.pop("지웅")
print(grades)



# Set

finished_classes = set()

# Insert (Not overlap)
finished_classes.add("자료 구조")
finished_classes.add("알고리즘")
finished_classes.add("프로그래밍 기초")
finished_classes.add("인터랙티브 웹")
finished_classes.add("데이터 사이언스")
print(finished_classes)

finished_classes.add("자료 구조")
print(finished_classes)

# Search
print("자료 구조" in finished_classes)

# Delete
finished_classes.remove("자료 구조")
print(finished_classes)
finished_classes.remove("알고리즘")
print(finished_classes)