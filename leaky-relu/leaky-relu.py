import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here

    arr = np.array(x)
    zeros = np.zeros(arr.shape)

    return np.maximum(arr, zeros) + alpha * np.minimum(arr, zeros)