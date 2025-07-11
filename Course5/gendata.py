import pandas as pd
import numpy as np

# Create synthetic dataset
np.random.seed(0)
genes = [f"Gene_{i}" for i in range(1, 11)]
data = {
    "Gene": genes,
    "Tissue_A": np.random.normal(10, 2, size=10),
    "Tissue_B": np.random.normal(12, 3, size=10),
    "Tissue_C": np.random.normal(8, 1.5, size=10),
    "Condition": ["Healthy"] * 5 + ["Treated"] * 5,
    "Biomarker": [True, False, True, False, True, False, False, True, False, True]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("gene_expression_data.csv", index=False)
