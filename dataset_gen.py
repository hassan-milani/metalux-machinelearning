import pandas as pd
import numpy as np

# Generate synthetic data
num_samples = 1000
num_datacenters = 5
num_features = 5  # Example features like latency, CPU utilization, etc.
num_classes = num_datacenters  # Each class represents a datacenter

np.random.seed(42)

data = []
for _ in range(num_samples):
    datacenter = np.random.randint(0, num_datacenters)
    features = np.random.rand(num_features)
    label = datacenter
    data.append(np.concatenate((features, [label])))

columns = [f'feature_{i}' for i in range(num_features)] + ['datacenter']
df = pd.DataFrame(data, columns=columns)

# Save the generated dataset
df.to_csv('cloud_resource_dataset.csv', index=False)