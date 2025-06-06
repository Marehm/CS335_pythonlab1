name = "marehm"
age = 21
ai_course = True

print("Name:", name)
print("Age in 5 years:", age + 5)
print("Is enrolled in CS335 course?", ai_course)
print("\n")

topics = ["Logic", "Search", "NLP", "ML", "Bayesian Inference", "Chatbots", "Prompt Engineering"]

count = 1
for topic in topics:
  print("We will study: " + str(count) + ". " + topic)
  count += 1

student = {'name': "marehm", 'score': 90}

if student['score'] >= 95:
  grade = "A+"
elif student['score'] >= 90:
  grade = "A"
elif student['score'] >= 80:
  grade = "B"
else:
  grade = "C or below"

print("\n")
print(f"{student['name']} received a grade of {grade}.")

def squareNumber(num):
  return num ** 2

print("\n")
print(squareNumber(2))
print(squareNumber(10))

