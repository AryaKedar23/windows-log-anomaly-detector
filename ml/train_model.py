import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Parse the log file line by line into structured columns
log_entries = []

with open("samples/synthetic_attack.log", "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) < 5:
            continue  # skip lines that do not have enough parts
        timestamp = " ".join(parts[0:3])  # e.g., 'Nov 07 20:00:01'
        host = parts[3]
        process = parts[4]
        message = " ".join(parts[5:])  # rest of the line is message
        log_entries.append([timestamp, host, process, message])

# Create DataFrame with explicit column names
data = pd.DataFrame(log_entries, columns=["timestamp", "host", "process", "message"])

# Check parsing result
print(data.head())

# Create feature: length of message string
data['message_length'] = data['message'].astype(str).apply(len)

# Prepare feature matrix
X = data[['message_length']].values

# Train IsolationForest anomaly detection model
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X)

# Save the trained model
joblib.dump(model, 'ml/iforest_model.joblib')

print("Model training complete and saved.")
