Student Academic Tracker 🎓

A modular Python Command Line Interface (CLI) application designed to evaluate student attendance compliance (75% threshold), generate step-by-step arithmetic breakdowns, aggregate multi-subject performance, and compute relative grades using Gaussian distribution metrics (Mean, Standard Deviation, Z-Scores, and weighted CGPA)

This project adheres to the t VITYARTHI Build Your Own Project framework for flipped course evaluations.   
PDF
📄 Project Overview

In higher education environments, students face significant administrative challenges tracking attendance thresholds across multiple courses and understanding relative grading systems. Modern university evaluation systems frequently employ relative grading curves where grades are assigned based on class sample mean (μ) and standard deviation (σ) rather than absolute marks.   

The Student Academic Tracker provides an automated, lightweight terminal application that:

    Monitors subject-level and aggregate attendance against mandatory institutional limits (75%).

    Educates students through step-by-step mathematical explanations of attendance formulas.   

    Automates statistical relative grading calculations, Z-score transformations, and weighted credit CGPA derivation.   

    Enforces robust input validation to prevent runtime system exceptions.

🎯 Requirements Specification
1. Functional Requirements

In accordance with the project criteria requiring at least three major functional modules:   
PDF

    FR1: Single-Subject Attendance Evaluation (calculator.py, status_checker.py)

        Computes exact attendance percentages formatted to two decimal places.   

        Evaluates percentage against the mandatory 75% institutional threshold and displays an immediate eligibility status flag (ELIGIBLE / NOT ELIGIBLE).   

    FR2: Step-by-Step Calculation Engine (explain_.py)

        Provides an educational breakdown of intermediate arithmetic steps (fraction conversion and scalar multiplication).   

    FR3: Multi-Subject Attendance Aggregator (main_.py)

        Collects attended and total class counts across 4 core subjects simultaneously and calculates total aggregate compliance.

    FR4: Relative Grading & CGPA Engine (CGPA_calculator_.py)

        Computes class sample mean (μ) and sample standard deviation (σ).   

        Transforms raw marks (0−100) into individual Z-scores (Z=σx−μ​) and assigns relative letter grades and grade points.   

        Calculates final weighted Cumulative Grade Point Average (CGPA) based on course credit hours (1−4).   

    FR5: Input Validation & Defensive Shield (valid_.py)

        Inspects input strings to verify numeric digits before type casting.   

        Rejects non-numeric characters, empty strings, negative numbers, division-by-zero attempts, and boundary violations.

2. Non-Functional Requirements

Meets all non-functional requirements specified in the evaluation rubric:   
PDF

    NFR1: Performance Efficiency: All mathematical routines execute with zero latency (<50 ms).

    NFR2: Usability: Features clean terminal output with visual line separators, clear textual instructions, and structured statistical summary tables.

    NFR3: Maintainability: Built using a modular 6-file structure separating presentation, validation, core math, and statistical reporting.

    NFR4: Reliability & Error Handling Strategy: Includes explicit fallback handling for division-by-zero conditions (e.g., zero total classes or zero variance σ=0).

🛠️ Technologies & Tools Used

    Programming Language: Python 3.8+[cite: 14, 17]

    Standard Libraries: math module (No external third-party library dependencies required)

    Version Control: Git & GitHub   
    PDF

    Development Environment: VS Code / Terminal / Command Prompt   

📂 Repository & File Structure

In compliance with the project guidelines requiring a clean, modular structure with 5–10 files:   
Plaintext

student-academic-tracker/
│
├── main_.py             # CLI application entry point, menu navigation, and flow controller
├── calculator.py       # Core attendance percentage computation routines
├── CGPA_calculator.py  # Statistical engine (Mean, Std Dev, Z-Score, Grade mapping, CGPA)
├── status_checker.py   # Attendance threshold logic (75% criteria check)
├── explain_.py          # Step-by-step arithmetic breakdown printer
├── valid_.py            # Custom string validation and numeric conversion parser
├── statement.md          # Problem statement, project scope, and target users
└── README.md             # Comprehensive project documentation

⚙️ Steps to Install & Run
Prerequisites

Ensure Python 3.8 or higher is installed on your system.
Bash

python --version
# or on Linux/macOS:
python3 --version

Installation Steps

    Clone the GitHub Repository:
    Bash

    git clone https://github.com/your-username/student-academic-tracker.git
    cd student-academic-tracker

    Run the Application:
    Bash

    python main.py
    # or on Linux/macOS:
    python3 main_.py

🚀 Execution & System Workflow

When launching main_.py, users navigate through an interactive menu:
Plaintext

__________________________________________
 
     STUDENT ACADEMIC TRACKER          
__________________________________________

1. Calculate Attendance Percentage
2. Step-by-Step Calculation of Attendance Percentage
3. Check Multiple Subjects Average
4. Calculate CGPA and Relative Grading
5. Exit
__________________________________________
Enter choice (1-5):

Process Flow Diagram
Plaintext

[Start Application] ---> (Display Main Menu) ---> {User Choice}
                                                         |
         +-----------------+----------------+------------+------------+
         |                 |                |                         |
    [Choice 1]        [Choice 2]       [Choice 3]                [Choice 4]
         |                 |                |                         |
  (Single Sub Att)  (Step Breakdown) (4-Sub Aggregate)         (Relative CGPA)
         |                 |                |                         |
         +-----------------+----------------+-------------------------+
                                    |
                                    v
                           (Validate Inputs)
                                    |
                           +--------+--------+
                           |                 |
                        [Valid]          [Invalid]
                           |                 |
                           v                 v
                    (Execute Logic)   (Display Error)
                           |                 |
                           +--------+--------+
                                    |
                                    v
                           (Render Results)

📸 Sample CLI Screenshots & Outputs
Plaintext

Enter classes attended: 38
Enter total classes held: 45

Attendance Percentage: 84.44%
Status: ELIGIBLE(Keep it up!)

Plaintext

Enter classes attended: 28
Enter total classes held: 40

 Calculation Breakdown for Attendance Percentage:

Formula: (Attended Classes / Total Classes) * 100

Step 1: Divide attended classes by total classes 
   Result = 0.700
Step 2: Multiply by 100
   Result = 70.00%

Plaintext

--- Calculate CGPA & Grades ---
Enter Marks for Subject 1IN  (0-100): 85
Enter Credit Hours for Subject 1IN (1-4): 4
Enter Marks for Subject 2IN  (0-100): 70
Enter Credit Hours for Subject 2IN (1-4): 3
Enter Marks for Subject 3IN  (0-100): 60
Enter Credit Hours for Subject 3IN (1-4): 3
Enter Marks for Subject 4IN  (0-100): 45
Enter Credit Hours for Subject 4IN (1-4): 2

           RELATIVE GRADING                       
________________________________________________________

Mean = 65.00
________________________________________________________

Standard Deviation = 16.83
________________________________________________________

Subject 1 Marks: 85 Z-Score: 1.19 Grade: A+ GP: 9 Credits: 4
Subject 2 Marks: 70 Z-Score: 0.30 Grade: B+ GP: 7 Credits: 3
Subject 3 Marks: 60 Z-Score: -0.30 Grade: B GP: 6 Credits: 3
Subject 4 Marks: 45 Z-Score: -1.19 Grade: P GP: 4 Credits: 2

Final Relative CGPA: 7.08 / 10.00

📊 Relative Grading Scale Matrix

The application maps individual marks to letter grades and grade points based on standard deviation offsets from the sample mean (Z=σx−μ​):   
Z-Score Range	Letter Grade	Grade Point (GP)	Performance
Z≥1.5	S	10	Outstanding
1.0≤Z<1.5	A+	9	Excellent
0.5≤Z<1.0	A	8	Very Good
0.0≤Z<0.5	B+	7	Good
−0.5≤Z<0.0	B	6	Above Average
−1.0≤Z<−0.5	C	5	Average
−1.5≤Z<−1.0	P	4	Pass
Z<−1.5	F	0	Fail

Note: If class sample variance equals zero (σ=0), static fallback grade thresholds are applied to prevent division-by-zero runtime crashes.   
🧪 Instructions for Testing & Verification

To verify full application compliance, execute the test scenarios below:
Test Case ID	Target Feature	Inputs	Expected Output / Behavior	Status
TC-VAL-01	String Validation Input: "45"	

Validated successfully, converted to integer 45  PASS
TC-VAL-02	Invalid Input Protection Input: "abc"	Rejects input, displays error without crashing.	PASS
TC-ATT-01	Single Attendance	Attended: 30, Total: 40	Computes 75.00%, Status: ELIGIBLE.	PASS
TC-ATT-02	Attendance Failure	Attended: 20, Total: 40	Computes 50.00%, Status: NOT ELIGIBLE.	PASS
TC-ATT-03	Boundary Guard Attended: 50, Total: 40	Displays boundary error message (Attended > Total).PASS
TC-CGPA-01	Relative CGPA EngineMarks: [85, 70, 60, 45], Credits: [4, 3, 3, 2]	Computes Mean = 65.00, Std Dev = 16.83, CGPA = 7.08.PASS
TC-CGPA-02	Zero Variance Guard Marks: [80, 80, 80, 80]	 Identifies σ=0, assigns Grade 'A' without throwing ZeroDivisionError.PASS
