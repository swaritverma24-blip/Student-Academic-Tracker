def calculate_percentage(attended, total):
    #Calculates attendance percentage
    if (total == 0):
        return "0.00"
    percentage = (attended / total) * 100
    return f"{percentage:.2f}"  # Format to 2 decimal places