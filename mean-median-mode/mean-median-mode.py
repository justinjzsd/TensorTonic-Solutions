from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here

    c = Counter(x)
    maxFreq = max(c.values())
    modes = []
    for value, count in c.items():
        if count == maxFreq:
            modes.append(value)
    
    return {
        'mean': float(np.mean(x)),
        'median': float(np.median(x)),
        'mode': float(min(modes))
    }