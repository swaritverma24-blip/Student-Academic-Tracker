def explain_calculation(attended, total):
    # Prints the step-by-step formula breakdown
    print("\n Calculation Breakdown for Attendance Percentage:")
    print("\nFormula: (Attended Classes / Total Classes) * 100")
    print("\nStep 1: Divide attended classes by total classes ")

    if (total > 0):
        fraction = attended / total
        print("   Result = " + str(f"{fraction:.3f}"))


        print("Step 2: Multiply by 100")
        percentage = fraction * 100  #Calculating percentage
        print("   Result = " + str(f"{percentage:.2f}")    + "%")
    else:
        print("Total classes cannot be 0")