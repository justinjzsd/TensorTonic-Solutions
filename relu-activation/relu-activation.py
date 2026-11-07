import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    arr = np.array(x)
    return np.maximum(arr, np.zeros(arr.shape))