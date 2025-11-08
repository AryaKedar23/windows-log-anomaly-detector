import sys
import numpy as np
import joblib
import subprocess

# Load the trained IsolationForest model
model = joblib.load('ml/iforest_model.joblib')

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    # Feature extraction: message length as earlier
    message_length = len(line)
    X = np.array([[message_length]])
    
    # Predict anomaly (-1 is anomaly)
    pred = model.predict(X)
    if pred[0] == -1:
        print("ANOMALY DETECTED:", line)
        
        # Example: call response script with appropriate action and target
        # Customize IP or action extraction as per your log format
        # subprocess.run(['powershell', '.\\scripts\\response.ps1', '-Action', 'BLOCK_IP', '-Target', '192.168.1.10'])
