import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    A = np.array(a)
    B = np.array(b)

    normA = np.linalg.norm(A)
    normB = np.linalg.norm(B)

    if normA == 0 or normB == 0:
        return 0.0
    
    return float(np.dot(A, B)/(normA * normB))