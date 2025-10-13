import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import sweetviz as sv
from ydata_profiling import ProfileReport, compare

# Load data
X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42, stratify=y)

# Reporting
df = X.copy()
df["target"] = y

profile = ProfileReport(df, title="Iris Dataset Report", explorative=True)
profile.to_file("iris_dataset_ydata_profiling.html")

# Reporting 2
# Erstelle den Analysebericht
report = sv.analyze(df)

# Zeige den Bericht an (öffnet automatisch eine HTML-Datei im Browser)
report.show_html('Mein_Datenbericht.html')

# Comparison
df_train = X_train.copy()
df_train["target"] = y_train
profile_train = ProfileReport(df_train, title="Iris Dataset Train")

df_test = X_test.copy()
df_test["target"] = y_test
profile_test = ProfileReport(df_test, title="Iris Dataset Test")

comparison_report = compare([profile_train, profile_test])

statistics = comparison_report.get_description()

comparison_report.to_file("comparison.html")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_scaled, y_train)

# Evaluate
y_pred = clf.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))