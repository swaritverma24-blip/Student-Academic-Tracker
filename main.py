from valid import is_valid_number, string_to_int
from calculator import calculate_percentage
from status_checker import check_attendance_status
from explain import explain_calculation
from CGPA_calculator import calculate_mean_std_devation,grade,cgpa
run=True

while (run==True):

    print("__________________________________________")
    print(" \n     STUDENT ACADEMIC TRACKER          ")   
    print("__________________________________________")
    print("\n1. Calculate Attendance Percentage")
    print("\n2. Step-by-Step Calculation of Attendance Percentage")
    print("\n3. Check Multiple Subjects Average")
    print("\n4. Calculate CGPA and Relative Grading")
    print("\n5. Exit")
    print("__________________________________________")


    choice =input("Enter choice (1-5): ")

    #  1: Calculate Percentage & Status
    if (choice == "1"):
        attended_str = input("\nEnter classes attended: ")
        total_str = input("\nEnter total classes held: ")

        if (is_valid_number(attended_str) and is_valid_number(total_str)):
            attended = string_to_int(attended_str)
            total = string_to_int(total_str)

            if (attended > total):
                print("Wrong Input: Attended classes cannot be greater than total classes!")
            elif (total == 0):
                print("Wrong Input: Total classes must be greater than 0!")
            else:
                per = calculate_percentage(attended, total)
                print("\nAttendance Percentage: " + str(per) + "%")
                check_attendance_status(per)
            
        else:
            print("Wrong Input: Please enter valid numbers only")

        # 2: Step-by-Step Calculation
    elif (choice == "2"):
        attended_str = input("\nEnter classes attended: ")
        total_str = input("Enter total classes held: ")

        if (is_valid_number(attended_str) and is_valid_number(total_str)):
            attended = string_to_int(attended_str)
            total = string_to_int(total_str)

            if (total == 0):
                print("Wrong Input: Total classes must be greater than 0")
            else:
                explain_calculation(attended, total)
        else:
            print("Wrong Input: Please enter valid numbers only")

    # 3: Average of 4 Subjects
    elif (choice == "3"):
        print("\n--- Calculate 4 Subject Average ---")
        sub1_attended = input("Subject 1 - Classes Attended: ")
        sub1_total = input("Subject 1 - Total Classes   : ")
        
        sub2_attended = input("Subject 2 - Classes Attended: ")
        sub2_total = input("Subject 2 - Total Classes   : ")

        sub3_attended = input("Subject 3 - Classes Attended: ")
        sub3_total = input("Subject 3 - Total Classes   : ")

        sub4_attended = input("Subject 4 - Classes Attended: ")
        sub4_total = input("Subject 4 - Total Classes   : ")

        if (is_valid_number(sub1_attended) and is_valid_number(sub1_total) and 
            is_valid_number(sub2_attended) and is_valid_number(sub2_total) and
            is_valid_number(sub3_attended) and is_valid_number(sub3_total) and
            is_valid_number(sub4_attended) and is_valid_number(sub4_total)):
            
            att1 = string_to_int(sub1_attended)
            tot1 = string_to_int(sub1_total)
            att2 = string_to_int(sub2_attended)
            tot2 = string_to_int(sub2_total)
            att3 = string_to_int(sub3_attended)
            tot3 = string_to_int(sub3_total)
            att4 = string_to_int(sub4_attended)
            tot4 = string_to_int(sub4_total)

            total_attended = att1 + att2 + att3 + att4
            total_classes = tot1 + tot2 + tot3 + tot4  

            if (total_classes != 0):
               
                print("\nTotal Attended across subjects: " + str(total_attended) + " / " + str(total_classes))
                overall_percent = calculate_percentage(total_attended, total_classes)
                print("\nOverall Attendance: " + str(overall_percent) + "%")
                check_attendance_status(overall_percent)
            else:
                print("Wrong Input: Total classes must be greater than 0")
        else:
            print("Wrong Input: Please enter valid numbers")

           
    elif (choice == "4"):
     #Calculate CGPA using relative grading
      print("\n--- Calculate CGPA & Grades ---")
      marks = []
      credits = []
      valid_input = True

      #Take marks and credits for 4 subjects
      for i in range(1, 5):
        mark = int(input("Enter Marks for Subject " + str(i) + "IN  (0-100): "))
        credit = int(input("Enter Credit Hours for Subject " + str(i) + "IN (1-4): "))

        # Check whether marks and credits are valid
        if (0 <= mark <= 100 and credit > 0):
            marks.append(mark)
            credits.append(credit)

        else:
            print("Wrong Input: Marks must be 0-100 and Credits must be greater than 0")
            valid_input = False
            break

    # Calculate CGPA 
      if (valid_input==True):

           final_cgpa = cgpa(marks, credits)

           print("Final Relative CGPA:", final_cgpa, "/ 10.00")
    # 4: Exit
    elif (choice == "5"):
        print("\nExiting program")
        print("Thank you for using the Academics  Tracker!")
        run = False

    else:
        print("Invalid choice Please select 1, 2, 3, 4 or 5 number only.")