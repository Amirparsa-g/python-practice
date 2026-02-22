# Linear Regression 📈

This folder contains my implementation and experiments with **Linear Regression**, one of the fundamental algorithms in Machine Learning.

Linear Regression is used for predicting continuous values by modeling the relationship between input features and a target variable.

---

## 🧠 Mathematical Background

For univariate linear regression:

\[
f(x) = wx + b
\]

Where:
- `w` = weight (slope)
- `b` = bias (intercept)

The model is trained by minimizing the **Mean Squared Error (MSE)**:

\[
J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} (f(x_i) - y_i)^2
\]

Optimization is performed using **Gradient Descent**.

---

## 📂 Contents

This folder may include:

- `from_scratch.py` → Implementation using NumPy
- `sklearn_comparison.py` → Validation using scikit-learn
- `visualization.py` → Plotting regression line and cost curve
- `multivariate.py` → Extension to multiple features

---

## 🔍 Concepts Practiced

- Cost Function (MSE)
- Gradient Descent
- Learning Rate Tuning
- Convergence Behavior
- Feature Scaling
- Overfitting vs Underfitting

---

## 📊 Visualization

Possible visualizations included:
- Regression line vs training data
- Cost vs iterations
- Effect of learning rate on convergence

---

## ⚙️ Tools Used

- Python
- NumPy
- Matplotlib
- scikit-learn (for comparison)

---

## 🎯 Learning Goal

The goal of this project is to:

- Understand linear regression mathematically
- Implement gradient descent from scratch
- Build strong intuition for optimization
- Prepare for more advanced supervised learning models

---

> Linear Regression is the foundation of many advanced Machine Learning algorithms.
