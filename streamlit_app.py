import streamlit as st 

import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="House Price Prediction App", layout="wide")
st.sidebar.title("House Price Prediction App")

def generate_house_data(n_samples=100):
    np.random.seed(50)
    size = np.random.normal(1400, 50, n_samples)
    price = size * 50 + np.random.normal(0, 50, n_samples)
    return pd.DataFrame({'size': size, 'price': price})

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model():
    df = generate_house_data(100)
    X = df[['size']]
    Y = df['price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    model= LinearRegression()
    model.fit(X_train, Y_train)
    
    return model 

def main():
    st.title("House Price Prediction App")
    st.write("Put the size of the house in square feet to predict its price.")
    
    model= train_model()
    size = st.number_input("House size", min_value=500, max_value=2000, value=1500)
    
    if st.button("Predict Price"):
        predicted_price = model.predict(np.array([[size]]))
        st.success(f"The predicted price for a house of size {size} sqft is ${predicted_price[0]:,.2f}")
        
        df = generate_house_data()
        fig = px.scatter(df, x='size', y='price', title='House Size vs Price')
        fig.add_scatter(x=[size], y=[predicted_price[0]],
                        mode='markers',
                        marker=dict(color='red', size=10),
                        name='Predicted Price')
        st.plotly_chart(fig)
        
if __name__ == "__main__":
    main()





