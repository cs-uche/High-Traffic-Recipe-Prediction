# High-Traffic Recipe Prediction

## Overview
This repository focuses on predicting recipes that generate high traffic for a Grocery App's official webpage. The Grocery App, initially designed for grocery shopping, observed a significant increase in traffic (29%) when posting certain recipes on their webpage.

In response to this discovery, an analyst on the team identified recipes that generated high traffic on the day of posting. It's important to note that this list is not exhaustive.

## Objective
The goal for data scientists involved in this project is to analyze the provided data and uncover patterns in the relationship between recipes and their popularity. The objective is to gain insights into the factors that contribute to a recipe becoming popular, enabling accurate predictions of high-traffic recipes to be posted on the website daily.

## Dataset
The dataset contains information about recipes that have historically generated high traffic. Data scientists will explore, analyze, and model this dataset to extract meaningful patterns and develop a predictive model.

## Key Tasks
1. **Data Exploration:** Dive into the dataset to understand its structure, variables, and potential patterns. [Link to Notebook](notebooks/data_analysis.ipynb)
2. **Analysis:** Uncover insights into the characteristics of recipes that lead to high traffic. [Link to Notebook](notebooks/data_analysis.ipynb)
3. **Model Development:** Build a predictive model to accurately forecast popular recipes. [Link to Notebook](notebooks/predictive_modelling.ipynb)
4. **Evaluation:** Assess the model's performance and refine as necessary for optimal predictions. [Link to Notebook](notebooks/predictive_modelling.ipynb)
5. **Interactive API Endpoints**: Enhance the usability of the model by implementing interactive API endpoints, facilitating seamless interaction for prediction generation.  For more details, refer to the [app README](app/README.md).
6. **DataOps + MLOps:** Steps to ensure the model is seamlessly integrated into production, continuously monitored, and efficiently manages data operations and machine learning operations for sustained performance and reliability.

## Visualizations
**Data Exploration and Analysis**
<br/> Below is the plot to analyze the pattern in the feature columns(servings, protein, sugar, carbohydrates, calories) with respect to the target(for high/low traffic).
![Pair plot of Numeric columns](imgs/pair_plot.png)

**Model Development**
<br/> Below are plots for the champion model.
<br/>The first plot is a confusion matrix, highlighting the model's performance in classifying unseen data.
![confusion matrix](imgs/champion_model_confusion_matrix.png)
<br/>The second plot is a receiver operating characteristic curve. The closer the curve leans to the vertical left y-axis (orange line), the better the model. The dashed diagonal blue line represents a random choice model and can be used as a baseline.
![roc curve](imgs/champion_model_roc.png)

**Interacting with the Model**
- CLI (coming soon)
- REST API controllers/endpoints
- REST API
![Prediction on Swagger](./imgs/swagger_response_prediction.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.