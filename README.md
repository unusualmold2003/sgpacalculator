# SGPA & Percentage Calculator

This Python project calculates the **SGPA (Semester Grade Point Average)** and the **total percentage** based on the marks, grade points, and credits of multiple subjects entered by the user. The project uses **NumPy** for efficient array operations.

## Features

- **User Input**: 
  - Enter the number of subjects.
  - For each subject, input the subject name, marks, and credits.
  
- **Grade Calculation**: 
  - Automatically assigns a grade point based on the marks using the following scale:
    - Marks >= 90: Grade 10
    - Marks >= 80 and < 90: Grade 9
    - Marks >= 70 and < 80: Grade 8
    - Marks >= 60 and < 70: Grade 7
    - Marks >= 55 and < 60: Grade 6
    - Marks >= 50 and < 55: Grade 5
    - Marks >= 40 and < 50: Grade 4

- **SGPA Calculation**: 
  - Calculates the SGPA by multiplying grade points with respective credits and dividing by the total number of credits.
  
- **Percentage Calculation**: 
  - Calculates the total percentage by dividing the sum of all marks by the total possible marks.

## Project Structure

1. **marks_input()**:
    - Takes user input for subject name, marks, and credits.
    - Assigns a grade point based on the marks.

2. **sgpa_calc()**:
    - Calculates the SGPA using the formula:
      \[
      SGPA = \frac{\sum (Grade \times Credits)}{\sum Credits}
      \]

3. **Percentage Calculation**:
    - The total percentage is calculated as:
      \[
      Percentage = \frac{\sum Marks}{Total Marks} \times 100
      \]

## Example

Here's how the program works for 3 subjects:

```python
Enter number of subjects: 3

Enter Subject Name: Mathematics
Enter the marks: 92
Enter the no of credits: 4

Enter Subject Name: Physics
Enter the marks: 81
Enter the no of credits: 3

Enter Subject Name: Chemistry
Enter the marks: 78
Enter the no of credits: 3

Subject: Mathematics Marks: 92 Grade Point: 10 Credits: 4
Subject: Physics Marks: 81 Grade Point: 9 Credits: 3
Subject: Chemistry Marks: 78 Grade Point: 8 Credits: 3

Total percentage is: 83.66666666666667
Total SGPA is: 9.1
