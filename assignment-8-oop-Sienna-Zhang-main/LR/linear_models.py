import numpy as np

class LinearRegressionClosedForm:
    def __init__(self, fit_intercept=True, alpha=0.0):
        self.fit_intercept = fit_intercept
        self.alpha = alpha
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        """
        Fit linear model.
        """
        X = np.array(X)
        y = np.array(y)
        
        if X.ndim == 1:
            X = X.reshape(-1, 1)
            
        n_samples, n_features = X.shape
        
        if self.fit_intercept:
            X_b = np.c_[np.ones((n_samples, 1)), X]
            I = np.eye(n_features + 1)
            I[0, 0] = 0  # Do not penalize intercept
        else:
            X_b = X
            I = np.eye(n_features)
            
        # Normal Equation: theta = (X.T * X + alpha * I)^-1 * X.T * y
        A = X_b.T @ X_b + self.alpha * I
        b = X_b.T @ y
        
        try:
            theta = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            # Fallback to pseudo-inverse if singular (though ridge usually fixes this)
            theta = np.linalg.pinv(A) @ b
            
        if self.fit_intercept:
            self.intercept_ = theta[0]
            self.coef_ = theta[1:]
        else:
            self.intercept_ = 0.0
            self.coef_ = theta
            
        return self

    def predict(self, X):
        """
        Predict using the linear model.
        """
        if self.coef_ is None:
            raise ValueError("Model is not fitted yet.")
            
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
            
        return X @ self.coef_ + self.intercept_

    def score(self, X, y):
        """
        Return the coefficient of determination R^2 of the prediction.
        """
        from .metrics import r2_score
        y_pred = self.predict(X)
        return r2_score(y, y_pred)
