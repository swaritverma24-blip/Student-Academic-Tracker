# Problem Statement & Project Scope: Student Academic Tracker

## Problem Statement
University students frequently face administrative challenges tracking mandatory class attendance thresholds (e.g., maintaining at least 75% attendance) and estimating academic standing under relative grading models. Relative grading relies on sample statistics—specifically the class mean ($\mu$), sample standard deviation ($\sigma$), and Z-score metrics—making manual grade prediction error-prone and complex. Additionally, existing basic calculator scripts lack robust input validation, leading to application crashes when encountering non-numeric entries, zero-division attempts, or invalid parameter bounds.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Scope of Project
The **Student Academic Tracker** is a modular Python CLI application built to address these challenges. The project scope encompasses:
* Calculating single-subject and multi-subject attendance percentages formatted to two decimal places.
* Flagging eligibility status against mandatory institutional attendance limits (75% cutoff).
* Providing step-by-step instructional breakdowns of attendance calculations.
* Automating statistical Gaussian curve derivations, Z-score transformations, relative grade mappings, and weighted credit CGPA calculations.
* Enforcing custom input validation and defensive exception handling across all input interfaces.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Target Users
In accordance with the project criteria, this tool is designed for:
* **Undergraduate & Postgraduate Students:** To track attendance thresholds, prevent debarment, and project expected semester CGPA under relative grading curves.
* **Academic Advisors & Faculty:** To evaluate class performance distributions, compute class means and standard deviations, and generate relative grade assignments.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

## High-Level Features

1. **Single-Subject Attendance & Status Evaluator:** Calculates attendance percentages and evaluates student eligibility against the 75% cutoff threshold.
2. **Step-by-Step Explanation Engine:** Outputs an educational breakdown displaying intermediate fraction generation and scaling steps.
3. **Multi-Subject Aggregate Tracker:** Aggregates attended and total classes across 4 core courses concurrently to compute overall academic compliance.
4. **Relative Grading & CGPA Module:** Computes sample mean ($\mu$), sample standard deviation ($\sigma$), Z-scores ($Z = \frac{x - \mu}{\sigma}$), maps relative letter grades (S to F), and derives weighted credit CGPA.
5. **Custom Input Validation Engine:** Verifies inputs prior to integer parsing, filtering out empty strings, non-numeric characters, negative values, and zero-division attempts.
