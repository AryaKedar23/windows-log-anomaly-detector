Windows Log Anomaly Detector
A modular framework for real-time Windows log monitoring, anomaly detection using machine learning, and interactive dashboard visualization.

⭐️Features
Real-time PowerShell log streaming and parsing
Machine learning anomaly detection (Isolation Forest)
Web dashboard built with Flask for log analytics
Extensible structure for custom log sources and automated responses
Simple management scripts for training and detection


🛰️Tech Stack
Python (pandas, scikit-learn, joblib)
Flask for dashboard
PowerShell for log streaming


📦 Project Structure
log-analytics-framework/
├── ml/
│   ├── train_model.py        # Model training script
│   └── iforest_model.joblib  # Saved ML model
├── dashboard/
│   ├── app.py                # Flask dashboard
│   └── templates/
│       └── dashboard.html    # Dashboard HTML template
├── samples/
│   └── synthetic_attack.log  # Example log file (do not upload large logs!)
├── scripts/
│   └── response.ps1          # Automated response (optional)
├── log_stream.ps1            # PowerShell log streaming script
├── README.md                 # This documentation
├── .gitignore                # Files to exclude from repo



How it Works
Training: Model is trained using synthetic_attack.log, extracts features (e.g. message length), and saves via joblib.
Detection: Incoming logs are parsed, features extracted, and anomalies flagged using the Isolation Forest model.
Dashboard: View logs and analytics with the Flask web app.
Response: Automated PowerShell scripts can be integrated to act on alerts.


Notes
Do not commit sensitive, large, or real log files—use .gitignore.
For testing, use small synthetic samples.
Licensed under MIT. Feel free to fork and improve!


Contributing
Pull requests, issues, and suggestions are welcome!
