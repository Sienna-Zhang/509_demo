import unittest
import numpy as np
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from linear_models import LinearRegressionClosedForm

class TestLinearRegression(unittest.TestCase):
    def test_predict_shape(self):
        X = np.random.rand(10, 3)
        y = np.random.rand(10)
        model = LinearRegressionClosedForm()
        model.fit(X, y)
        y_pred = model.predict(X)
        self.assertEqual(y_pred.shape, (10,))

    def test_perfect_linear_data(self):
        # y = 2x + 1
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([3, 5, 7, 9, 11])
        model = LinearRegressionClosedForm()
        model.fit(X, y)
        
        self.assertAlmostEqual(model.coef_[0], 2.0, places=5)
        self.assertAlmostEqual(model.intercept_, 1.0, places=5)

    def test_regularization_reduces_coefficients(self):
        # Create collinear features
        np.random.seed(42)
        n_samples = 50
        X1 = np.random.rand(n_samples, 1)
        X2 = X1 + 0.01 * np.random.randn(n_samples, 1) # Highly correlated
        X = np.hstack([X1, X2])
        y = 3 * X1.flatten() + 2 * X2.flatten() + np.random.randn(n_samples) * 0.1
        
        model_no_reg = LinearRegressionClosedForm(alpha=0.0)
        model_no_reg.fit(X, y)
        norm_no_reg = np.linalg.norm(model_no_reg.coef_)
        
        model_reg = LinearRegressionClosedForm(alpha=1.0)
        model_reg.fit(X, y)
        norm_reg = np.linalg.norm(model_reg.coef_)
        
        self.assertLess(norm_reg, norm_no_reg)

if __name__ == '__main__':
    unittest.main()
