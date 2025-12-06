# Linear Regression Toolkit

## 1. Problem Description
This project implements a reusable Linear Regression toolkit using plain Python classes and NumPy. The toolkit includes:
- A `LinearRegressionClosedForm` class that implements the closed-form solution (Normal Equation) with optional L2 (Ridge) regularization.
- Evaluation metrics: Mean Squared Error (MSE) and R-squared (R2).
- Data utilities: Train/test split function.
- Visualization tools: Plotting residuals and predictions.
- A Jupyter Notebook demonstrating experiments with synthetic data.

## 2. How to Run the Solution

### Dependencies
- Python 3
- NumPy
- Matplotlib
- Jupyter (for the notebook)

Install them via pip:
```bash
pip install numpy matplotlib jupyter
``` 

### Running Tests
To verify the core functionality (model fitting, prediction, metrics):

```bash
python tests/test_core.py
``` 

### Running Experiments
To view and run the experiments:
1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook examples/demo.ipynb
   ``` 
2. Run all cells to see the results of:
   - Simple linear regression on noisy data.
   - Effect of Ridge Regularization on collinear features.
   - Polynomial regression.

## 3. Associate Explanations

### Mathematical Model
The model solves for weights $\theta$ using the Normal Equation:
$$ \theta = (X^T X + \alpha I)^{-1} X^T y $$
Where $\alpha$ is the regularization parameter (Ridge). If $\alpha=0$, it performs standard OLS regression.

### Key Components
- **`linear_models.py`**: Contains the class with `fit(X, y)`, `predict(X)`, and `score(X, y)` methods.
- **`metrics.py`**: Implements `mse` and `r2_score` from scratch.
- **`selection.py`**: Randomly splits data into training and testing sets.

## 4. Sample Input and Output

**Example Output from Experiment 1 (Straight Line):**

```text
Coefficients: [1.954]
Intercept: 3.021
MSE: 0.98234
R2 Score: 0.96543
``` 

**Example Output from Experiment 2 (Regularization):**

```text
Alpha      MSE                  Norm(coef)          
--------------------------------------------------
0.0        1.05231              15.43210            
0.001      1.05232              12.12345            
1.0        1.08456              2.34567             
```
