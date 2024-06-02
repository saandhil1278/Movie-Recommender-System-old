# Movie Recommendation System

This project involves the development of a Movie Recommendation System utilizing various feature engineering techniques, text vectorization, cosine similarities, and integrated APIs. The project also leverages Streamlit's interactive widgets for effortless deployment and user interaction.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  
## Introduction

The Movie Recommendation System is designed to provide personalized movie recommendations based on user preferences. By applying comprehensive feature engineering techniques, the system ensures high accuracy and relevance in the recommendations.

## Features

- **Feature Engineering**: Applied various techniques including feature transformation, feature extraction, and One Hot Encoding.
- **Data Analysis**: Utilized pandas profiling for thorough data analysis.
- **Text Vectorization**: Implemented text vectorization to process textual data.
- **Cosine Similarities**: Used cosine similarities to measure the similarity between movie features.
- **Interactive Widgets**: Integrated APIs with Streamlit's interactive widgets for user-friendly interactions.
- **Effortless Deployment**: Easy deployment of the application using Streamlit.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv env
   Source `env\Scripts\activate`  
3.  **Install Dependencies**
  ```bash
  `pip install -r requirements.txt`

4. **Run the Application**
  ```bash
   streamlit run app.py


Usage
Launch the application using the streamlit run app.py command.
Interact with the application through the Streamlit interface.
Input your preferences and get movie recommendations.

Project Structure

movie-recommendation-system/
│
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│   └── ...
│
├── src/
│   ├── feature_engineering.py
│   ├── text_vectorization.py
│   ├── recommendation_engine.py
│   └── ...
│
├── app.py
├── requirements.txt
└── README.md

data/: Contains the dataset files.
src/: Contains the source code for feature engineering, text vectorization, and recommendation engine.
app.py: The main application script for Streamlit.
requirements.txt: Lists the dependencies required for the project.
README.md: The readme file.
