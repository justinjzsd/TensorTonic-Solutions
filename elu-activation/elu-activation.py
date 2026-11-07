import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    res = x

    for i in range(len(res)):
        if(res[i] <= 0):
            res[i] = alpha * (math.pow(math.e, res[i]) - 1)

    return res