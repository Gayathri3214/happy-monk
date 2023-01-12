import numpy as np

# Load dataset A
A = np.load("dataset_A.npy")

# Calculate summary statistics for dataset A
A_mean = np.mean(A)
A_std = np.std(A)
A_min = np.min(A)
A_max = np.max(A)

# Load dataset B
B = np.load("dataset_B.npy")

# Calculate summary statistics for dataset B
B_mean = np.mean(B)
B_std = np.std(B)
B_min = np.min(B)
B_max = np.max(B)

# Compare summary statistics
if (np.isclose(A_mean, B_mean, rtol=1e-05, atol=1e-08) and
    np.isclose(A_std, B_std, rtol=1e-05, atol=1e-08) and
    np.isclose(A_min, B_min, rtol=1e-05, atol=1e-08) and
    np.isclose(A_max, B_max, rtol=1e-05, atol=1e-08)):
    print("Datasets A and B identify the same variable.")
else:
    print("Datasets A and B do not identify the same variable.")