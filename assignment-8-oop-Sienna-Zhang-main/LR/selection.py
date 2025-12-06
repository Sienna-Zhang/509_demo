import numpy as np

def train_test_split(X, y, test_size=0.2, random_state=None, shuffle=True):
    """
    Split arrays or matrices into random train and test subsets.
    """
    X = np.array(X)
    y = np.array(y)
    
    if len(X) != len(y):
        raise ValueError("X and y must have the same length")
        
    n_samples = len(X)
    n_test = int(n_samples * test_size)
    n_train = n_samples - n_test
    
    if shuffle:
        if random_state is not None:
            np.random.seed(random_state)
        indices = np.random.permutation(n_samples)
    else:
        indices = np.arange(n_samples)
        
    test_indices = indices[:n_test]
    train_indices = indices[n_test:]
    
    X_train = X[train_indices]
    X_test = X[test_indices]
    y_train = y[train_indices]
    y_test = y[test_indices]
    
    return X_train, X_test, y_train, y_test
