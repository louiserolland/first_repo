import pandas as pd
import numpy as np

def create_simulated_data(n_households=10, max_members=4, seed=42):
    """
    Simulate individual-level data for a set of households.

    Parameters:
        n_households (int): Number of households to simulate.
        max_members (int): Maximum number of individuals per household.
        seed (int): Random seed for reproducibility.

    Returns:
        pd.DataFrame: Individual-level simulated dataset.
    """
    np.random.seed(seed)
    data = []

    for h in range(1, n_households + 1):
        n_members = np.random.randint(1, max_members + 1)
        for i in range(1, n_members + 1):
            data.append({
                "household_id": h,
                "individual_id": f"H{h}_I{i}",
                "age": np.random.randint(18, 85),
                "gender": np.random.choice(["Male", "Female"]),
                "income": np.random.randint(0, 6000),
                "employment_status": np.random.choice([
                    "Employed", "Unemployed", "Student", "Retired"
                ])
            })

    return pd.DataFrame(data)
