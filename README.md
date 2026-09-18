# Student-Marks-Predictor-Using-Machine-Learning
# STUDENT MARKS PREDICTOR USING MACHINE LEARNING

## 1. Project Overview

Student Marks Predictor Using Machine Learning is a beginner-friendly Machine Learning project developed as part of the Fundamentals of Artificial Intelligence and Machine Learning course.

The project predicts a student's final marks based on different academic factors such as study hours, attendance, previous marks, and assignment scores.

The system uses Machine Learning techniques to analyze historical student data, train a prediction model, and estimate the expected marks of a student.

The project demonstrates the complete Machine Learning workflow, including data collection, data preprocessing, analysis, model training, prediction, evaluation, and visualization.

The primary Machine Learning algorithm used in this project is Linear Regression.

---

## 2. Problem Statement

Student marks can be influenced by various academic factors such as the number of hours studied, attendance percentage, previous examination marks, and assignment performance.

Manually analyzing these factors and estimating student performance can be difficult when dealing with a large number of students.

The purpose of this project is to develop a simple Machine Learning system that learns patterns from existing student data and predicts the expected marks of a student.

The system provides a practical demonstration of how Machine Learning can be applied to an educational prediction problem.

---

## 3. Objectives

The main objectives of this project are:

- To understand the fundamentals of Artificial Intelligence and Machine Learning.
- To understand supervised Machine Learning.
- To implement a regression-based Machine Learning model.
- To analyze student academic data.
- To preprocess and validate the dataset.
- To train a Machine Learning model using student data.
- To predict student marks.
- To evaluate the performance of the trained model.
- To visualize student performance and prediction results.
- To implement a modular Machine Learning project.
- To use Git and GitHub for version control.

---

## 4. Scope of the Project

The project focuses on predicting student marks using academic and study-related information.

The system includes:

- Student data loading.
- Student data validation.
- Data preprocessing.
- Student performance analysis.
- Machine Learning model training.
- Student marks prediction.
- Model performance evaluation.
- Data visualization.
- Basic automated testing.

The project is intended for educational purposes and demonstrates fundamental Machine Learning concepts.

---

## 5. Target Users

The target users of the project are:

- Students learning Artificial Intelligence and Machine Learning.
- Students developing academic ML projects.
- Teachers and faculty members demonstrating ML concepts.
- Beginners learning regression algorithms.
- Educational users interested in basic student performance analysis.

---

# 6. Functional Requirements

The system contains four major functional modules.

## Module 1: Student Data Management

The system should:

- Load student data from a CSV file.
- Display student records.
- Validate the dataset.
- Check for missing values.
- Handle invalid data.

INPUT:
Student academic dataset.

OUTPUT:
Validated student data.

---

## Module 2: Student Performance Analysis

The system should:

- Calculate basic statistics.
- Analyze study hours.
- Analyze attendance.
- Analyze previous marks.
- Analyze assignment scores.
- Analyze the relationship between academic factors and final marks.

INPUT:
Student dataset.

OUTPUT:
Analysis results and statistics.

---

## Module 3: Student Marks Prediction

The system should:

- Select relevant input features.
- Split the dataset into training and testing data.
- Train a Machine Learning model.
- Accept new student information.
- Predict the expected final marks.

INPUT:

- Study Hours
- Attendance
- Previous Marks
- Assignment Score

OUTPUT:

Predicted Final Marks.

---

## Module 4: Model Evaluation and Visualization

The system should:

- Calculate Mean Absolute Error.
- Calculate Mean Squared Error.
- Calculate R² Score.
- Compare actual and predicted marks.
- Generate graphs.
- Display model performance.

INPUT:
Testing data and prediction results.

OUTPUT:
Evaluation metrics and visualization.

---

# 7. Non-Functional Requirements

## 7.1 Usability

The system should be easy to use and provide clear instructions for entering student information.

## 7.2 Performance

The system should process the available dataset and generate predictions within a reasonable amount of time.

## 7.3 Reliability

The system should produce consistent results when the same dataset and configuration are used.

## 7.4 Maintainability

The project should be divided into separate modules so that individual components can be easily modified.

## 7.5 Error Handling

The system should handle invalid numerical input, missing values, and incorrect dataset formats.

## 7.6 Scalability

The project should allow additional features, larger datasets, and other Machine Learning algorithms to be added in the future.

---

# 8. Technologies Used

Programming Language:
Python

Machine Learning Library:
Scikit-learn

Data Processing:
Pandas
NumPy

Data Visualization:
Matplotlib

Development Environment:
Visual Studio Code

Version Control:
Git

Repository:
GitHub

Dataset Format:
CSV

---

# 9. Machine Learning Algorithm

## Linear Regression

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

In this project, Linear Regression learns the relationship between student academic factors and final marks.

Input features:

- Study Hours
- Attendance
- Previous Marks
- Assignment Score

Target variable:

- Final Marks

The basic Linear Regression equation is:

y = mx + b

For multiple features, the model learns the relationship between several input variables and the target variable.

---

# 10. Why Linear Regression?

Linear Regression was selected because:

- It is simple and beginner-friendly.
- It is suitable for numerical prediction.
- It is easy to understand and explain.
- It is computationally efficient.
- It provides an interpretable Machine Learning model.
- It is suitable for demonstrating the fundamentals of supervised learning.

---

# 11. Dataset Description

The project uses a student performance dataset.

The dataset contains the following attributes:

+------------------+--------------------------------------+
| Column           | Description                          |
+------------------+--------------------------------------+
| Study_Hours      | Number of hours studied              |
| Attendance       | Student attendance percentage        |
| Previous_Marks   | Previous examination marks           |
| Assignment_Score | Assignment performance score         |
| Final_Marks      | Final marks to be predicted          |
+------------------+--------------------------------------+

The first four columns are used as input features.

Final_Marks is the target variable.

---

# 12. Input and Output

## Input

The system accepts:

- Study hours
- Attendance percentage
- Previous examination marks
- Assignment score

Example:

Study Hours: 6
Attendance: 85
Previous Marks: 72
Assignment Score: 80

## Output

The system provides:

- Predicted final marks
- Model evaluation metrics
- Data analysis
- Graphical visualization

Example:

Predicted Final Marks: 76.50

---

# 13. System Workflow

The overall workflow of the system is:

Student Dataset
       |
       v
Load Dataset
       |
       v
Validate Data
       |
       v
Preprocess Data
       |
       v
Analyze Student Data
       |
       v
Select Features
       |
       v
Split Training and Testing Data
       |
       v
Train Linear Regression Model
       |
       v
Evaluate Model
       |
       v
Enter New Student Data
       |
       v
Predict Final Marks
       |
       v
Display Results
       |
       v
Generate Visualization

---

# 14. System Architecture

The system follows a modular architecture.

                 USER
                   |
                   v
              main.py
                   |
        +----------+----------+
        |          |          |
        v          v          v
   Data Loader  Analysis  Preprocessing
        |          |          |
        +----------+----------+
                   |
                   v
            Model Training
                   |
                   v
              Prediction
                   |
                   v
         Evaluation Module
                   |
                   v
        Visualization Module
                   |
                   v
                RESULTS

---

# 15. Project Structure

student-marks-predictor/
|
|-- data/
|   |-- student_performance.csv
|
|-- src/
|   |-- __init__.py
|   |-- data_loader.py
|   |-- data_analysis.py
|   |-- preprocessing.py
|   |-- model_training.py
|   |-- prediction.py
|   |-- visualization.py
|
|-- tests/
|   |-- __init__.py
|   |-- test_project.py
|
|-- outputs/
|   |-- .gitkeep
|
|-- main.py
|-- requirements.txt
|-- README.md
|-- statement.md
|-- .gitignore

---

# 16. Description of Project Modules

## data_loader.py

Responsible for:

- Loading the CSV dataset.
- Checking the dataset.
- Handling missing values.
- Returning the processed data.

## data_analysis.py

Responsible for:

- Calculating statistics.
- Analyzing student performance.
- Generating basic data insights.

## preprocessing.py

Responsible for:

- Selecting features.
- Selecting the target variable.
- Preparing the data for Machine Learning.

## model_training.py

Responsible for:

- Creating the Linear Regression model.
- Splitting training and testing data.
- Training the Machine Learning model.

## prediction.py

Responsible for:

- Accepting new student information.
- Generating predicted marks.

## visualization.py

Responsible for:

- Creating graphs.
- Displaying actual and predicted values.
- Visualizing relationships in the dataset.

## main.py

Acts as the main application controller and connects all project modules.

---

# 17. Installation

## Step 1: Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

## Step 2: Open the Project

cd student-marks-predictor

## Step 3: Install Required Libraries

pip install -r requirements.txt

---

# 18. How to Run

Run the following command:

python main.py

The program will:

1. Load the student dataset.
2. Validate the data.
3. Analyze the dataset.
4. Prepare the data.
5. Train the Linear Regression model.
6. Evaluate the model.
7. Ask for student details.
8. Predict final marks.
9. Display the results.
10. Generate visualization.

---

# 19. Model Evaluation

The project uses three evaluation metrics.

## Mean Absolute Error (MAE)

MAE calculates the average absolute difference between actual and predicted marks.

Lower MAE generally indicates smaller prediction errors.

## Mean Squared Error (MSE)

MSE calculates the average squared difference between actual and predicted marks.

Lower MSE generally indicates smaller prediction errors.

## R² Score

R² Score measures the proportion of variation in the target variable explained by the model.

A value closer to 1 indicates that the model explains a larger proportion of the variation in the target data.

---

# 20. Testing

The project contains a tests folder for validating important components.

Run the tests using:

python -m unittest discover tests

The testing module checks:

- Dataset loading.
- Dataset columns.
- Data validation.
- Model training.
- Prediction output.
- Basic input validation.

---

# 21. Design Diagrams

The project documentation includes the following diagrams:

1. Use Case Diagram
2. Workflow Diagram
3. Sequence Diagram
4. Component/Class Diagram
5. Dataset Schema

These diagrams explain how the different components of the Student Marks Predictor interact with each other.

---

# 22. Design Decisions

## Python

Python was selected because it is easy to learn and provides powerful libraries for Machine Learning and data analysis.

## Linear Regression

Linear Regression was selected because it is simple, interpretable, and suitable for numerical prediction.

## CSV Dataset

CSV was selected because it is lightweight, easy to create, and suitable for a small educational Machine Learning project.

## Modular Architecture

The system is divided into multiple modules to improve code organization, maintainability, testing, and future development.

---

# 23. Advantages

- Simple and beginner-friendly.
- Directly related to Machine Learning.
- Easy to understand.
- Uses a supervised learning algorithm.
- Provides actual predictions.
- Includes model evaluation.
- Includes data visualization.
- Uses modular code.
- Includes testing.
- Can be extended in the future.

---

# 24. Limitations

- The dataset may be relatively small.
- The model may not capture complex relationships between academic factors.
- Prediction accuracy depends on the quality of the dataset.
- The project is primarily designed for educational purposes.
- Predicted marks should not be considered official academic results.

---

# 25. Future Enhancements

The project can be improved by:

- Adding more student records.
- Using a larger real-world dataset.
- Implementing Decision Tree Regression.
- Implementing Random Forest Regression.
- Comparing multiple Machine Learning models.
- Adding a graphical user interface.
- Creating a web application.
- Adding database support.
- Creating a student performance dashboard.
- Deploying the application online.

---

# 26. Expected Results

After running the project, the system should:

- Successfully load the student dataset.
- Train the Machine Learning model.
- Display model evaluation metrics.
- Accept new student information.
- Predict the student's expected marks.
- Display graphical analysis.

The exact prediction and evaluation values depend on the dataset and model configuration.

---

# 27. Conclusion

The Student Marks Predictor Using Machine Learning project demonstrates the application of Artificial Intelligence and Machine Learning concepts to an educational problem.

The system uses student academic information to train a Linear Regression model and predict final marks.

The project covers important Machine Learning concepts including supervised learning, feature selection, data preprocessing, train-test splitting, model training, prediction, model evaluation, and visualization.

The modular implementation also demonstrates software development practices such as code organization, validation, testing, documentation, and GitHub version control.

This project provides a practical introduction to building and documenting a complete Machine Learning application.

---

# 28. References

- Python Documentation
- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Scikit-learn Documentation

---

# 29. Course Information

Course:
Fundamentals of Artificial Intelligence and Machine Learning

Project Title:
Student Marks Predictor Using Machine Learning

Algorithm:
Linear Regression

Programming Language:
Python

Version Control:
Git and GitHub

Project Type:
Machine Learning Prediction System
