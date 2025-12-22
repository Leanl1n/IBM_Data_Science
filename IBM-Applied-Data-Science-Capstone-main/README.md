# SpaceX Falcon 9 Landing Prediction

**Author:** Lean Lerry Delgado

## Overview
Predict the successful landing of SpaceX's Falcon 9 first stage to estimate launch costs. SpaceX advertises launches at $62M, significantly cheaper than competitors at $165M+. This cost advantage comes from reusing the first stage. By accurately predicting landing success, companies can better estimate launch costs for competitive bidding against SpaceX.

## Project Modules
1. **Data Collection** - SpaceX API requests and data wrangling for historical launch data
2. **Web Scraping** - Falcon 9 launch records extracted from Wikipedia using BeautifulSoup
3. **Exploratory Data Analysis** - Patterns and correlations analyzed using Matplotlib & Seaborn
4. **Database Integration** - Data loaded into Db2 with SQL queries for insights
5. **Feature Engineering** - New features created with Folium interactive maps for launch sites
6. **Interactive Dashboard** - Plotly Dash application with dropdown filters and range sliders
7. **Machine Learning** - Model comparison: SVM, Decision Trees, and Logistic Regression with hyperparameter tuning

## Results
- **Decision Tree Classifier**: 94.44% accuracy (best performing model)
- **SVM & K-Nearest Neighbors**: 83.33% accuracy each
- Models trained on standardized data with 80/20 train-test split

## Key Technologies
Python, Pandas, Scikit-learn, Plotly Dash, SQL, BeautifulSoup, Matplotlib, Seaborn, Folium

## Files
- Jupyter notebooks for each analysis module
- `spacex_dash_app.py` - Interactive Dash application
- `spacex_launch_dash.csv` - Dataset with launch information

Explore this repository to dive into the complete workflow, methodologies, and innovative techniques employed in this capstone project. Whether you're a data science enthusiast, a space exploration aficionado, or a professional seeking insights into predictive modeling, this project offers something for everyone.
