# Streamlit_App_House

## House Price Prediction App

A user-friendly web application built with Streamlit that predicts house prices based on the size of the house (in square feet) using a simple linear regression model. The app also visualizes the relationship between house size and price with an interactive Plotly scatter plot.

## Features

### 1. Interactive User Interface
The app provides an intuitive interface where users can input the size of a house and receive an instant price prediction. The interface is built using Streamlit, making it easy to use directly from the browser.

### 2. Synthetic Data Generation
The app generates synthetic house data (size and price) using NumPy and pandas. This data simulates real-world house pricing trends and is used to train the regression model and for visualization.

### 3. Machine Learning Model
A linear regression model from scikit-learn is trained on the generated data. The model learns the relationship between house size and price, allowing it to make predictions for new input values.

### 4. Real-Time Prediction
Users can enter a house size (between 500 and 2000 sqft) and click a button to get an immediate price prediction. The result is displayed clearly on the page.

### 5. Data Visualization
The app uses Plotly Express to create an interactive scatter plot showing the relationship between house size and price. When a prediction is made, the predicted price is highlighted on the plot for easy comparison.

## How It Works
1. **Data Generation:** The app creates a dataset of house sizes and prices with some random noise to mimic real-world data.
2. **Model Training:** A linear regression model is trained on this data each time the app runs.
3. **User Input:** The user enters a house size using a number input field.
4. **Prediction:** When the user clicks the "Predict Price" button, the app uses the trained model to predict the price for the entered size.
5. **Visualization:** The app displays a scatter plot of the data and marks the predicted price in red.

## Requirements
- Python 3.8+
- Streamlit
- pandas
- numpy
- plotly
- scikit-learn

You can install all dependencies using [uv](https://github.com/astral-sh/uv) or pip:

```
uv pip install streamlit pandas numpy plotly scikit-learn
```

or

```
pip install streamlit pandas numpy plotly scikit-learn
```

## How to Run
1. Open a terminal in the project directory.
2. Run the following command:
   ```
   streamlit run main.py
   ```
3. The app will open in your default web browser.

## File Structure
- `main.py` – The main application file containing all logic for data generation, model training, prediction, and visualization.
- `pyproject.toml` – (Optional) Project metadata and dependencies if using uv or poetry.
- `README.md` – Project documentation.

## Customization
You can modify the data generation logic, model parameters, or UI elements in `main.py` to fit your own use case or dataset.

## License
This project is for educational purposes. Feel free to use and modify it for your own learning or projects.
