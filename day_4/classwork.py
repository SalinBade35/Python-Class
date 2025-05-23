name = input("Enter your name: ")  # by default : string type
marks = int(input("Enter your marks out of 100: ")) # int type 

print(f"Hello, {name}!")

if marks >= 90:
    print("Outstanding! You’re the Rancho of your batch.")
elif marks >= 75:
    print("Great job! You’re like Farhan — doing what you love.")
elif marks >= 60:
    print("Good! Keep going like Raju.")
    
else:
    print("Oh no! Virus will be very disappointed.")
    if name.lower() == "raju":
        print("But Raju always bounces back. Believe in yourself!")

# RAJU -> lower() -> raju

