# Movie Recommender

**Authors**: Brent Smart

## Overview

For this project, I investigated the movie rating history at Webflix to provide movie recommendations for users. This investigation uses the ratings of 943 members. Webflix's ability to recommend new movies for its users depends on it's ability to accurately predict a customer's likelyhood of enjoying a movie. Hence, the primary goal of this investigation is to accurately predict a customer's movie rating. Another goal is to make recommendations for customers new to the company. I was able to build a models that predicts their rating with a margin of error of just 0.67.

## Business Problem

Webflix will be able to recommend movies for users using the rating history of 943 of its customers. Doing so will help Webflix individualize recommendations to customers and help customers determine the movie they should (or should not) watch next. By providing users with movies they would mostly likely enjoy, the company will potentially keep customers enrolled in the monthly movie program and recommend the platform to friends and family members. Hence, the questions used in this analysis are as follows:

Which movies does a particular user enjoy? 

Which movies would users most likely enjoy based on users with similar rating history (content-based filtering)?

## Data

This project uses the MovieLens data set GroupLens Research. The data set provides 100,000 ratings (1-5) from 943 users on 1682 movies. Movies with less than 10 ratings were removed from this investigation. Each user has a unique user id, demographics, and rated at least 20 movies. Since the purpose of this project is to investigate the types of movies users enjoy to help make recommendations, the target variable is the user ratings. All features are included except for the movie release date.


## Modeling

The final model with the target variable Default_Next_Month includes all original columns. 

## Evaluation

The model underwent multiple interactions, each time investigating how well the model addressed Accuracy, Recall, and Precision. Accuracy was emphasized to prevent misidentify defaulting customers. At the end the final model showed overall improvement in accuracy. 


## For More Information

Please review our full analysis in [our Jupyter Notebook](./Documents/Flatiron/phase_4/project_4/phase4/Movie Recommender.ipynb) or our [presentation](./credit_default/reports/Phase 3_ Classification Models - Credit Card Default Prediction.pdf).

For any additional questions, please contact **Brent Smart smartbrent1@gmail.com**

## Repository Structure

```
├── README.md        <-- Main README file explaining the project's business case,
│                        methodology, and findings
│
├── data             
│   └── README       <-- Information about the dataset
│   └── u.data       <-- The full u data set, 100000 ratings by 943 users.
│   └── u.item       <-- Information about the movies.
│   └── u.user       <-- Demographic information about the users.
├── functions            
│   └── __init__.py  <-- Information about the dataset
│   └── data_prepara <-- Functions with repeatable code.
│       tion.py
├── Movie Recommender<-- Jupyter Notebooks for exploration and presentation
│   .ipynb        
│   ├── exploratory  <-- Unpolished exploratory data analysis (EDA) notebooks
│   └── report       <-- Polished final notebook(s)
│
└── images            
    └── figures      <-- Generated graphics and figures to be used in reporting

## Repository Contents

Below is a list of the contents of this repository.

- `README.md`: The README for this repo branch explaining it's contents - you're reading it now
- `TEMPLATE_README.md`: An example of a project README that provides a brief overview of your whole project
- `dsc-phase1-project-template.ipynb`: A starter Jupyter Notebook with headings, code examples and guiding questions
- `DS_Project_Presentation_Template.pdf`: A starter slide deck presenting your project - here is an [editable version](https://docs.google.com/presentation/d/1PaiH1bleXnhiPjTPsAXQSiAK0nkaRlseQIr_Yb-0mz0/copy)
- `__init__.py`: Python helper file that tells Python that there are packages in the repository that can be imported
- `data` folder: A folder for the data you reference with your code
- `images` folder: A folder for the images you reference in your files
- `code` folder: A folder for the python scripts that your Jupyter Notebook imports
  - `__init__.py`: Python helper file that tells Python that there are packages in this folder that can be imported
  - `data_cleaning.py`: Code to prepare data for analysis
  - `visualizations.py`: Code to produce visualizations
  - `eda_notebook.ipynb`: Notebook with any messy EDA so the main notebook can be more readable
- `.gitignore`: A hidden file that tells git to not track certain files and folders
