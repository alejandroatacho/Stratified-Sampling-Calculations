import math
# Stratified sampling calculations

n = 30  # sample size
N = 8000  # Population Size
N1 = 4000
N2 = 2400
N3 = 1600

def stratified_calc():
    n1 = n * (N1 / N)
    n2 = n * (N2 / N)
    n3 = n * (N3 / N)
    print(f"{n1} is the sample size for group 1")
    print(f"{n2} is the sample size for group 2")
    print(f"{n3} is the sample size for group 3")
    print(f"Total sample size: {n1 + n2 + n3}")

# Execute 
stratified_calc()
