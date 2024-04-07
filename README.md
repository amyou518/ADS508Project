# X-Ordinary Laboratories: Lung Disease Recognition Software
#### In this repository, you will discover resources that are related to our initiative to develop a recognition software that is capable of differentiating various lung diseases from X-ray images. This software aims to improve patient care by enhancing diagnostic accuracy and streamlining medical workflows.

# Overview
#### X-Ordinary Laboratory is a startup company that is dedicated to leveraging advanced machine learning techniques to automate disease detection from X-ray images. The goal of this project is to develop recognition software to interpret X-ray images of lung diseases such as pneumonia and COVID-19 to enhance diagnostic process efficiency and accuracy.

# Structure of the Project
## Problem Statement
#### Automated disease detection software is needed to reduce human bias from manual interpretation.

### Goals
#### Scalability and adaptability
#### Repeatability and transparency
#### Diastic accuracy improvement

### Non-Goals
#### Interpreting non-X-rays images
#### Developing custom hardware
#### Providing treatments to patients

### Data Sources
#### Chest X-ray Pneumonia Dataset
#### COVIDx CXR-2 Dataset

### Data Exploration
#### Analysis of image data types: .jpg, .jpeg, .png
#### Ingest images into SageMaker Studio Notebook for exploration

### Data Preparation
#### Removal of duplicate X-rays
#### Reformatting images for consistency
#### Creation of balanced training, validation, and test datasets

### Model Training
#### Utilizing SageMaker's built-in image classifier
#### Setting hyperparameters for training
#### 3000 images were used
#### 90% train, 5% validation, and 5% test
#### Evaluation metrics: Accuracy and F1 score

### Security and Privacy
#### No personally identifiable information stored
#### Data stored in publicly accessible S3 buckets

### Future Enhancements
#### Model Selection and Hyperparameter Tuning
#### Infrastructure Optimization
#### Data Augmentation

### Contributors
#### Amy Ou
#### Jessica Hin
#### Katie Mears
