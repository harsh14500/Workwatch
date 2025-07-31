import pandas as pd
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# 🔗 1. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="workwatch_db",
    user="postgres",
    password="1234",   
    port="5432"
)

# 📥 2. Load data from 'smart_logs' table
query = "SELECT * FROM smart_logs"
df = pd.read_sql(query, conn)

# ✅ 3. Preprocessing: Drop non-feature columns
df = df.dropna()  # optional: remove missing rows if any
X = df.drop(columns=['prediction', 'serial_number', 'timestamp'])
y = df['prediction']

# ✂️ 4. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🧠 5. Train RandomForest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 📊 6. Evaluate model
y_pred = model.predict(X_test)

print("\n✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\n📄 Classification Report:\n", classification_report(y_test, y_pred))

# 💾 7. Save model to disk
joblib.dump(model, "models/smart_model.pkl")
print("\n📁 Model saved to 'models/smart_model.pkl'")

# 🔚 Close connection
conn.close()