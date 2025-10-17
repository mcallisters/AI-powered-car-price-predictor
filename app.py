import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import joblib
import pandas as pd

# Create FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory where this script lives
base_dir = os.path.dirname(os.path.abspath(__file__))

# Print current working directory and script location for debugging
print("Running script from:", os.getcwd())
print("Script is located at:", os.path.abspath(__file__))
print("Base directory:", base_dir)
print("Looking for index.html at:", os.path.join(base_dir, "index.html"))
print("index.html exists:", os.path.exists(os.path.join(base_dir, "index.html")))

# Build path to the model in the same directory as app.py
model_path = os.path.join(base_dir, 'model.pkl')

print("Looking for model at:", os.path.abspath(model_path))
# Load the trained model using joblib
model = joblib.load(model_path)
print("Model loaded successfully!")


# -----------------------------
# Serve the frontend
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    """
    Serves the index.html file at the root URL
    """
    try:
        html_path = os.path.join(base_dir, "index.html")
        print(f"Attempting to serve: {html_path}")
        with open(html_path, "r") as f:
            content = f.read()
            print(f"Successfully read index.html, size: {len(content)} bytes")
            return content
    except FileNotFoundError as e:
        print(f"ERROR: index.html not found at {html_path}")
        return "<h1>index.html not found in " + base_dir + "</h1>"
    except Exception as e:
        print(f"ERROR reading file: {e}")
        return f"<h1>Error: {str(e)}</h1>"


# -----------------------------
# Health check endpoint
# -----------------------------
@app.get("/health")
def health_check():
    """
    Simple endpoint to check if the server is running.
    Returns a JSON dictionary with a "status" key.
    """
    return {"status": "healthy"}


# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict_car_price(payload: dict):
    """
    Expects payload dictionary with keys:
    "manufacturer", "model", "year", "mileage", "fuel_type", "engine_size"
    """

    # Extract features from payload
    manufacturer = str(payload.get("manufacturer"))
    model_name = str(payload.get("model"))
    year = int(payload.get("year"))
    mileage = float(payload.get("mileage"))
    fuel_type = str(payload.get("fuel_type"))
    engine_size = float(payload.get("engine_size"))

    # Derived features (required by training pipeline)
    CURRENT_YEAR = 2025
    age = max(CURRENT_YEAR - year, 0)
    mileage_per_year = mileage / age if age > 0 else mileage
    vintage = int(age > 20)

    # Organize features into a dictionary with exact column names the model expects
    row = {
        "Manufacturer": manufacturer,
        "Model": model_name,
        "Year": year,
        "Mileage": mileage,
        "Fuel type": fuel_type,
        "Engine size": engine_size,
        "age": age,
        "mileage_per_year": mileage_per_year,
        "vintage": vintage
    }

    # Create a DataFrame for the model
    df = pd.DataFrame([row])
    
    # Debug: Print the dataframe columns and data
    print(f"DataFrame columns: {df.columns.tolist()}")
    print(f"DataFrame:\n{df}")
    print(f"DataFrame dtypes:\n{df.dtypes}")

    # Make a prediction
    try:
        prediction = model.predict(df)[0]
        return {"predicted_price": round(prediction)}
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        raise


if __name__ == "__main__":
    import uvicorn
    print("\n✓ Starting backend server...")
    print("API will be available at: http://localhost:8000")
    print("Frontend: http://localhost:8000/")
    print("Press CTRL+C to stop the server\n")
    # RUN the app with Uvicorn directly without the need to use the command line.
    # I removed the reload=True parameter. Now when you run python app.py from VSCode, 
    # it will start without that warning. The server will run fine—you just won't get 
    # automatic reloading when you change the code (you'd need to stop and restart 
    # the server manually if you make changes).
    uvicorn.run(app, host="127.0.0.1", port=8000)
