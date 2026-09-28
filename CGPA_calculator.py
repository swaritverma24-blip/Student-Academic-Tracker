import math
#To calculate mean and standard deviation
def calculate_mean_std_devation(marks):
#checking the number of marks
    num_marks = len(marks)
    if (num_marks == 0):
          return 0, 0
    #Calculate the mean of marks
    mean = sum(marks) / num_marks
    #Calculate variance
    if (num_marks > 1):
          variance = ((sum((x - mean) ** 2) for x in marks)) / (num_marks - 1)
    else:
          variance = 0
   #Calculate standard deviation
    std_devation = math.sqrt(variance)
    return mean, std_devation


# Function to calculate grade and grade point
def grade(mark, mean, std_devation):
     #If standard deviation is zero
    if (std_devation == 0):
        #grade A if marks are 50 or above
        if (mark >= 50):
            return 8, "A"
        else:
            return 5, "C"
    #clculate Z-score to determine the grade based on the relative performance of the student
    z = (mark - mean) / (std_devation)




    #check the grade 
    if (z >= 1.5):
        return 10, "S"
    elif (z >= 1.0):
        return 9, "A+"
    elif (z >= 0.5):
        return 8, "A"
    elif (z >= 0):
        return 7, "B+"
    elif (z >= -0.5):
        return 6, "B"
    elif (z >= -1.0):
        return 5, "C"
    elif (z >= -1.5):
        return 4, "P"
    else:
        return 0, "F"


#calculate the final CGPA
def cgpa(marks, credits):
    # Calculate mean and standard deviation
    mean, std_devation = calculate_mean_std_devation(marks)
    total_points = 0.0
    total_credits = 0.0



    # Display the Grading details
    print("""\n           RELATIVE GRADING                       """)
    print("\n________________________________________________________")
    print("\nMean =", f"{ mean:.2f}")
    print("\n_________________________________________________________")
    print("\nStandard Deviation =", f"{ std_devation:.2f}")
    print("\n________________________________________________________")



    # Calculate grade for each subject
    for i in range(len(marks)):
         # Get marks and credits
        mark = marks[i]
        credit = credits[i]
        # Calculate grade and grade point
        gp,gr = grade(mark, mean, std_devation)

        # Calculate Z-score
        if (std_devation != 0):
            z =( (mark - mean) / (std_devation))
        else:
            z = 0


        # Display subject details
        print("\nSubject", i + 1,
              "Marks:", mark,
              "Z-Score:", (round(z, 2)),
              "Grade:", gr,
              "GP:", gp,
              "Credits:", credit)

        # Calculate total weighted grade points
        total_points = (total_points + (gp * credit))

        # Calculate total credits
        total_credits = total_credits + credit
    if (total_credits == 0):
     return 0

    # Calculate CGPA
    CGPA = total_points / total_credits

    #Return CGPA
    return f"{CGPA:.2f}"