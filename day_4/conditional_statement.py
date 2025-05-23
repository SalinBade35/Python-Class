name = input("Enter your name: ")  # string type
marks = int(input("Enter your marks out of 100: "))

# if statement
# if marks > 90:  # false
#     print("Excellent! You might be Rancho in disguise.")






# if - else statement
# if marks >= 60:  # 60 and 60 above
#     print(f"{name}, you're safe from Virus")
# else:
#     print(f"{name}, pack your bags — you might get a call from Virus!")









# elif - statement

if marks >= 90: 
    print("Outstanding! Just like Rancho.")
elif marks >= 75: 
    print("Very Good! Like Farhan — steady and sincere.")
elif marks >= 60:
    print("Good. You're like Raju — surviving but struggling.")
else:
    print("Needs Improvement. Hope Virus doesn’t see this!")





# #Nested - statement
if marks >= 60:     # marks = 50
    if marks >= 90:
        print("Topper! Virus is impressed.")
    else:
        print("Passed, but keep your head down around Virus.")
        
        
        
else:
    if name.lower() == "raju":
        print("Raju, sab theek ho jayega. Don't lose hope!")
    else:
        print("Fail. Virus will NOT be happy.")
