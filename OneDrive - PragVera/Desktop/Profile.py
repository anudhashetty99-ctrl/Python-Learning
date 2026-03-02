# My Personal Profile Card
# Author: Your Name
# Date: Today's Date

# My details
name = "Your Name"
age = 26
profession = "Mechanical Engineer"
goal = "Robotics Design Engineer"
skills = ["Creo", "SolidWorks", "2D Drafting", "GD&T"]

# Function to display profile
def show_profile(name, age, profession, goal, skills):
    print("=" * 35)
    print("       MY PROFILE CARD")
    print("=" * 35)
    print("Name       : " + name)
    print("Age        : " + str(age))
    print("Current    : " + profession)
    print("Goal       : " + goal)
    print("Skills     :")
    for skill in skills:
        print("  - " + skill)
    print("=" * 35)

# Ask user for a greeting
user = input("What is your name? ")
print("Hello " + user + "! Here is my profile:")
print("")

# Show the profile
show_profile(name, age, profession, goal, skills)

# Simple calculation
months_to_goal = 12
print("")
print("Months to robotics goal: " + str(months_to_goal))git remote add origin https://github.com/anudhashetty99-ctrl/Python-Learning.git
