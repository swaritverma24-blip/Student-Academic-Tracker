def check_attendance_status(percentage):
    #Checks whether attendance meets or falls below the required threshold
    target = 75.0  # Minimum required attendance percentage
    if (float(percentage) >= float(target)):
        print("Status: ELIGIBLE(Keep it up!)")
    else:
        print("Status: NOT ELIGIBLE(You need to improve your attendance!)")