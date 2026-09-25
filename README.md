# Flight Price Prediction

Machine Learning project for predicting airplane ticket prices using supervised regression.

## Project Objective

The objective of this project is to build a regression model capable of predicting the price of a flight from different flight and reservation characteristics.

The project covers the complete Machine Learning workflow:

* Data exploration and analysis
* Data preprocessing
* Model training
* Cross-validation
* Model evaluation
* Model export
* Streamlit deployment

## Dataset

The dataset contains **300,153 flight records** and the following variables:

* `airline`
* `flight`
* `source_city`
* `departure_time`
* `stops`
* `arrival_time`
* `destination_city`
* `class`
* `duration`
* `days_left`
* `price`

The `price` column is the target variable.

The `id` column is not used as a predictive feature.

## Machine Learning Workflow

### 1. Data Exploration

The dataset was analyzed to understand:

* Dataset structure
* Variable types
* Missing values
* Duplicate values
* Numerical distributions
* Categorical variables
* Relationships between variables and flight price

### 2. Preprocessing

The preprocessing pipeline includes:

* Median imputation for numerical features
* Most-frequent imputation for categorical features
* Standardization of numerical features
* One-hot encoding of categorical features
* `handle_unknown="ignore"` for unseen categorical values

The preprocessing is integrated directly into the Machine Learning pipeline.

### 3. Models

The following regression models were evaluated:

* Dummy Regressor
* Linear Regression
* Ridge Regression
* Random Forest Regressor

Ridge Regression was evaluated with several values of `alpha`:

```text
0.01
0.1
1
10
100
```

### 4. Cross-Validation

A **5-Fold Cross-Validation** strategy was used on the training set.

The evaluation metrics are:

* MAE — Mean Absolute Error
* RMSE — Root Mean Squared Error
* R² — Coefficient of Determination

### 5. Final Model

The final exported model is a **Random Forest Regressor** with:

```text
n_estimators = 100
random_state = 42
```

The complete preprocessing + model pipeline is stored in:

```text
artifacts/flight_price_model.joblib
```

Model metadata is stored in:

```text
artifacts/flight_price_model.meta.json
```

## Model Evaluation

Performance on the independent test set:

| Model             |      MAE |     RMSE |     R² |
| ----------------- | -------: | -------: | -----: |
| Dummy Regressor   | 19768.69 | 22704.24 |  ~0.00 |
| Linear Regression |  4254.04 |  6197.24 | 0.9255 |
| Ridge (α=100)     |  4589.42 |  6883.61 | 0.9081 |
| Random Forest     |  2403.68 |  4776.70 | 0.9557 |

The Random Forest model was selected as the final model based on the evaluation performed during the project.

## Uncertainty Around MAE

A 95% confidence interval was calculated for the MAE using the absolute errors on the independent test set.

This measures the uncertainty around the estimated test-set MAE. It is not a prediction interval for an individual flight price.

## Streamlit Application

A Streamlit application was created to allow users to enter flight information and obtain a predicted ticket price.

Run the application with:

```bash
python -m streamlit run app/app.py
```

The application uses the exported `.joblib` pipeline directly, so preprocessing does not need to be manually reproduced inside the application.

## Project Structure

```text
Flight-Price-Prediction/
│
├── data/
│   └── Clean_Dataset.csv
│
├── notebooks/
│   └── flight_price_prediction.ipynb
│
├── artifacts/
│   ├── flight_price_model.joblib
│   └── flight_price_model.meta.json
│
├── app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m streamlit run app/app.py
```

The application will then be available locally through the Streamlit URL displayed in the terminal.

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

## Author

Flight Price Prediction — Machine Learning Project
