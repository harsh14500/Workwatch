import streamlit as st
import pandas as pd
import psycopg2
import joblib
from datetime import datetime

# Load model
model = joblib.load("models/smart_model.pkl")

# Streamlit UI
st.title("📊 WorkWatch - Smart Drive Failure Predictor")
uploaded_file = st.file_uploader("Upload SMART log (.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Uploaded Data Preview:", df.head())
    
    expected_columns = [
        'power_on_hours','temperature','reallocated_sectors_count',
        'reported_uncorrectable_errors','spin_retry_count','seek_error_rate',
        'udma_crc_error_count'
    ]
    
    if all(col in df.columns for col in expected_columns):
        X_input = df[expected_columns]
        predictions = model.predict(X_input)
        df['predicted_failure'] = predictions
        st.success("✅ Prediction complete")
        st.dataframe(df)

        # Show alert message
        if 1 in predictions:
            st.error("⚠️ Potential risk detected in one or more drives!")

        # Store results to PostgreSQL
        try:
            conn = psycopg2.connect(
                dbname="workwatch_db", user="postgres", password="1234", host="localhost", port="5432"
            )
            cursor = conn.cursor()
            for _, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO smart_predictions (
                        power_on_hours, temperature, reallocated_sectors_count,
                        reported_uncorrectable_errors, spin_retry_count, seek_error_rate,
                        udma_crc_error_count, predicted_failure, timestamp
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    float(row['power_on_hours']), float(row['temperature']), float(row['reallocated_sectors_count']),
                    float(row['reported_uncorrectable_errors']), float(row['spin_retry_count']), float(row['seek_error_rate']),
                    float(row['udma_crc_error_count']), int(row['predicted_failure']), datetime.now()
                ))
            conn.commit()
            st.success("📝 Prediction logged to database")
        except Exception as e:
            st.error(f"❌ Database error: {e}")
        finally:
            conn.close()
    else:
        st.error("❌ Uploaded file is missing one or more required columns.")