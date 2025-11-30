# Project Statement – AI Disease Prediction System

## 1. Introduction
This project aims to create a simple AI model that predicts the most likely disease based on symptoms provided by the user. 
Many medical applications today use Machine Learning to help in diagnosis, and this project is a small demonstration of that idea.

## 2. Objective
- To build a basic Machine Learning model for health prediction
- To understand how symptom data can be converted into features
- To show the working of Naive Bayes classifier
- To create a user-friendly terminal-based prediction system

## 3. Problem Description
Users may not know which illness they might be suffering from based only on symptoms.  
This system tries to help by providing a likely answer based on patterns learned from data.

Given a set of symptoms, the model predicts one of the following diseases:
- Flu
- Migraine
- Heart Issue
- Food Poisoning
- Arthritis

## 4. Methodology
1. A small sample dataset is created with symptoms and diseases.
2. Symptoms are encoded using MultiLabelBinarizer.
3. Data is split into training and testing sets.
4. Naive Bayes algorithm is trained on this data.
5. User inputs symptoms.
6. Model predicts the most likely disease.

## 5. Results
The system is able to successfully identify the disease from the small dataset 
and provides an instant prediction based on the learned pattern.

## 6. Difficulties Faced
- Choosing an appropriate and simple ML model
- Preparing a dataset manually due to limited resources
- Encoding symptom text into numerical values
- Installing the required Python libraries (sklearn, pandas)
- Keeping the program simple but still AI-based for academic requirements

## 7. Future Improvements
- Expanding dataset for higher accuracy
- Adding more medical conditions
- Using RandomForest or Neural Networks
- Providing a GUI for easier usage
- Exporting predictions to PDF report
- Adding real-time medical suggestion system

## 8. Tools and Libraries Used
- Python
- Pandas
- Scikit-Learn (Naive Bayes)
- MultiLabelBinarizer

## 9. Conclusion
This project successfully demonstrates how AI and Machine Learning can be applied to basic healthcare prediction. 
Even though the dataset is small, the system reflects the core idea of medical diagnosis models used in the real world.
