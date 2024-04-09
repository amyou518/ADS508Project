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

### License
#### CC BY 4.0
#### Permission is granted to view and use the BIMCV-COVID19 Dataset without charge for research purposes only. Its sale is prohibited. Any non-academic research use need to be evaluated case by case by BIMCV- BIMCV-COVID19. If you intend to use this dataset for any non-academic research use, you need to communicate it describing the intended use and receive approval by the BIMCV-COVID19.

#### In agreement with the mission of the BIMCV-COVID19 to promote the publication of scientific knowledge as open data, any computational model or algorithm that have used the BIMCV-COVID19 Dataset and is publicly referenced (e.g. in a publication etc..) is suggested to be shared including the code and model weights and any case will give appropriate credit by citing the BIMCV-COVID19 article but not in any way that suggests that the BIMCV – BIMCV-COVID19 endorses you or your use.

#### Other than the rights granted herein, the BIMCV retains all rights, title, and interest in the BIMCV-COVID19 Dataset.

#### You may make a verbatim copy of the BIMCV-COVID19 Dataset for personal, research use as permitted in this Research Use Agreement. If another user within your organization wishes to use the BIMCV-COVID19 Dataset, they must comply with all the terms of this Research Use Agreement.

#### YOU MAY NOT DISTRIBUTE, PUBLISH, OR REPRODUCE A COPY of any portion or all of the BIMCV-COVID19 Dataset to others without specific prior written permission from BIMCV-COVID19.

#### You must not modify, reverse engineer, decompile, or create derivative works from the BIMCV-COVID19 Dataset with the exception of works in agreement with the clause number 2. You must not remove or alter any copyright or other proprietary notices in the BIMCV-COVID19 Dataset.

#### The BIMCV-COVID19 Dataset has not been reviewed or approved by the Food and Drug Administration or the European Medicines Agency, and is for Research Use Only. In no event shall data or images generated through the use of the BIMCV-COVID19 Dataset be used or relied upon in the diagnosis or provision of patient care.

#### THE BIMCV-COVID19 DATASET IS PROVIDED «AS IS,» AND BIMCV AND ITS COLLABORATORS DO NOT MAKE ANY WARRANTY, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, NOR DO THEY ASSUME ANY LIABILITY OR RESPONSIBILITY FOR THE USE OF THIS BIMCV-COVID19 DATASET.

#### You will not make any attempt to re-identify any of the individual data subjects. Re-identification of individuals is strictly prohibited. Any re-identification of any individual data subject shall be immediately reported to BIMCV-COVID19 project team. Please note that this project was approved by the institutional research committee, and both the images and the associated reports were made anonymous and de-identified by the Medical Image Bank of the Valencian Community at the Department of Universal Health and Public Health Services (BIMCV-CSUSP) and the Health Informatics Department at San Juan Hospital.

#### Any violation of this Research Use Agreement or other impermissible use shall be grounds for immediate termination of use of this BIMCV-COVID19 Dataset. In the event that the BIMCV – BIMCV-COVID19 determines that the recipient has violated this Research Use Agreement or other impermissible use has been made, the BIMCV – BIMCV-COVID19 may direct that the undersigned data recipient immediately return all copies of the BIMCV-COVID19 Dataset and retain no copies thereof even if you did not cause the violation or impermissible use.

#### You are agree to indemnify and hold BIMCV – BIMCV-COVID19 harmless from any claims, losses or damages, including legal fees, arising out of or resulting from your use of the BIMCV-COVID19 Dataset or your violation or role in violation of these Terms. You agree to fully cooperate in BIMCV- BIMCV-COVID19 defense against any such claims.
