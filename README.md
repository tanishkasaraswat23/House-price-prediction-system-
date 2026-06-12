# 🏠 House Price Prediction System

A Machine Learning web application that predicts house prices using Linear Regression trained on the California Housing Dataset.

## 📌 Project Overview

This project builds a complete end-to-end Machine Learning pipeline that:
- Loads and explores the California Housing Dataset
- Preprocesses and scales the data
- Trains a Linear Regression model
- Evaluates model performance
- Serves predictions through an interactive Streamlit web application

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine Learning model |
| Streamlit | Web application interface |

## 📊 Dataset

- **Name:** California Housing Dataset
- **Source:** Scikit-learn built-in dataset
- **Size:** 20,640 samples, 8 features
- **Target:** Median house value

### Features Used:
| Feature | Description |
|---------|-------------|
| MedInc | Median income in block group |
| HouseAge | Median house age in block group |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Block group population |
| AveOccup | Average number of household members |
| Latitude | Block group latitude |
| Longitude | Block group longitude |

## 🤖 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | 0.5758 |
| MAE | 0.5332 |
| MSE | 0.5559 |

## 📁 Project Structure
## ⚙️ Installation and Setup

**1. Clone the repository:**
```bash
git clone https://github.com/tanishkasaraswat23/House-price-prediction-system-.git
```

**2. Install required libraries:**
```bash
pip install -r requirements.txt
```

**3. Train the model:**
```bash
python src/train_model.py
```

**4. Run the application:**
```bash
streamlit run app.py
```

## 🚀 How to Use

1. Run the Streamlit app using the command above
2. Adjust the sliders on the left sidebar
3. Click **"Predict Price"** button
4. View the estimated house price

## 📈 Data Visualizations

The project generates the following visualizations:
- **Price Distribution** - Distribution of house prices in the dataset
- **Income vs Price** - Relationship between median income and house price
- **Age vs Price** - Relationship between house age and price
- **Actual vs Predicted** - Model prediction accuracy visualization

## 🎓 Learning Outcomes

Through this project, I learned:
- End-to-end Machine Learning pipeline development
- Data preprocessing and feature scaling
- Linear Regression model training and evaluation
- Building interactive web applications with Streamlit
- Version control with Git and GitHub

## 👩‍💻 Author

**Tanishka Saraswat**  
B.Tech - Artificial Intelligence and Machine Learning  
GitHub: [@tanishkasaraswat23](https://github.com/tanishkasaraswat23)