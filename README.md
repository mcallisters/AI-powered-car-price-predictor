# 🚗 AI-Powered Car Price Predictor

A machine learning web application that predicts used car prices based on vehicle characteristics. Built with FastAPI, deployed using Docker, and hosted on Render.

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.120.0-009688.svg)
![Docker](https://img.shields.io/badge/docker-enabled-2496ED.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Installation](#local-installation)
  - [Running with Docker](#running-with-docker)
- [API Documentation](#api-documentation)
- [Model Information](#model-information)
- [Deployment](#deployment)
- [Usage](#usage)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This application uses a machine learning model to predict the price of used cars based on key features such as manufacturer, model, year, mileage, fuel type, and engine size. The model is trained using XGBoost and scikit-learn, and is served through a FastAPI backend with a modern, responsive web interface.

### Key Highlights

- **Real-time predictions** using a trained XGBoost model
- **Modern web interface** with gradient design and animations
- **RESTful API** for easy integration
- **Dockerized** for consistent deployment across environments
- **Auto-deployment** via GitHub integration with Render
- **Health check endpoint** for monitoring

## ✨ Features

- 🎨 **Beautiful UI**: Modern, gradient-based design with smooth animations
- 🚀 **Fast Predictions**: Sub-second response times
- 📊 **Advanced ML Model**: XGBoost-based ensemble model
- 🔄 **Auto-Deploy**: Push to GitHub, automatically deploys to production
- 🐳 **Docker Support**: Containerized for portability and consistency
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- ✅ **Form Validation**: Client-side validation for better UX
- 🏥 **Health Monitoring**: Built-in health check endpoint
- 🌐 **CORS Enabled**: Ready for frontend integration from any domain

## 🎬 Demo

**Live Demo**: [https://your-app.onrender.com](https://your-app.onrender.com)

### Example Prediction

**Input:**
- Manufacturer: Toyota
- Model: Camry
- Year: 2020
- Mileage: 30,000 miles
- Fuel Type: Petrol
- Engine Size: 2.5L

**Output:** Predicted Price: $24,500

## 🛠️ Technology Stack

### Backend
- **FastAPI** (0.120.0) - Modern, fast web framework
- **Uvicorn** (0.38.0) - ASGI server
- **Python** (3.11) - Programming language

### Machine Learning
- **XGBoost** (3.1.1) - Gradient boosting framework
- **scikit-learn** (1.7.2) - ML utilities and preprocessing
- **pandas** (2.2.0) - Data manipulation
- **numpy** (1.26.4) - Numerical computing
- **joblib** (1.3.2) - Model serialization

### DevOps
- **Docker** - Containerization
- **Render** - Cloud hosting platform
- **GitHub** - Version control and CI/CD

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling with gradients and animations
- **JavaScript (ES6)** - Client-side logic
- **Fetch API** - Async HTTP requests

## 📁 Project Structure

```
AI-powered-car-price-predictor/
│
├── app.py                 # FastAPI application
├── index.html            # Frontend interface
├── model.pkl             # Trained ML model
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore        # Docker ignore rules
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)
- Git

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-powered-car-price-predictor.git
   cd AI-powered-car-price-predictor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   Navigate to: http://localhost:8000
   ```

### Running with Docker

1. **Build the Docker image**
   ```bash
   # For Apple Silicon (M1/M2/M3):
   docker build --platform linux/amd64 -t car-price-predictor .
   
   # For Intel/AMD:
   docker build -t car-price-predictor .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 car-price-predictor
   ```

3. **Access the application**
   ```
   http://localhost:8000
   ```

## 📚 API Documentation

### Base URL
```
http://localhost:8000  (local)
https://your-app.onrender.com  (production)
```

### Endpoints

#### 1. Home Page
```http
GET /
```
Returns the HTML interface.

**Response:** HTML page

---

#### 2. Health Check
```http
GET /health
```
Check if the server is running.

**Response:**
```json
{
  "status": "healthy"
}
```

---

#### 3. Predict Car Price
```http
POST /predict
```

Predict the price of a car based on its features.

**Request Body:**
```json
{
  "manufacturer": "Toyota",
  "model": "Camry",
  "year": 2020,
  "mileage": 30000,
  "fuel_type": "Petrol",
  "engine_size": 2.5
}
```

**Response:**
```json
{
  "predicted_price": 24500
}
```

**Supported Fuel Types:**
- Petrol
- Diesel
- Hybrid
- Electric
- LPG

**Validation Rules:**
- Year: 1980 - 2025
- Mileage: ≥ 0
- Engine Size: ≥ 0.5L

### Example cURL Request

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "manufacturer": "Toyota",
    "model": "Camry",
    "year": 2020,
    "mileage": 30000,
    "fuel_type": "Petrol",
    "engine_size": 2.5
  }'
```

### Example Python Request

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "manufacturer": "Toyota",
    "model": "Camry",
    "year": 2020,
    "mileage": 30000,
    "fuel_type": "Petrol",
    "engine_size": 2.5
}

response = requests.post(url, json=data)
print(response.json())
# Output: {'predicted_price': 24500}
```

## 🤖 Model Information

### Training Features

The model uses the following features for prediction:

**Input Features:**
- Manufacturer (categorical)
- Model (categorical)
- Year (numeric)
- Mileage (numeric)
- Fuel type (categorical)
- Engine size (numeric)

**Engineered Features:**
- Age (derived from year)
- Mileage per year (derived)
- Vintage flag (cars > 20 years old)

### Model Architecture

- **Algorithm**: XGBoost (Gradient Boosting)
- **Framework**: scikit-learn preprocessing pipeline
- **Serialization**: joblib (.pkl format)
- **Training Data**: Historical used car sales data

### Model Performance

The model's performance metrics will depend on your specific training data. Common metrics include:
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## 🌐 Deployment

### Deploying to Render

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create new Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository

3. **Configure the service**
   - **Name**: `car-price-predictor`
   - **Environment**: Docker
   - **Branch**: main
   - **Health Check Path**: `/health`
   - **Plan**: Free (or paid)

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy
   - Your app will be live at `https://car-price-predictor-xxxx.onrender.com`

### Auto-Deployment

Every time you push to the `main` branch, Render automatically:
1. Pulls the latest code
2. Builds a new Docker image
3. Deploys the updated app
4. Runs health checks

### Deployment via Docker Hub (Alternative)

1. **Build and tag the image**
   ```bash
   docker build --platform linux/amd64 -t yourusername/car-price-predictor:latest .
   ```

2. **Push to Docker Hub**
   ```bash
   docker login
   docker push yourusername/car-price-predictor:latest
   ```

3. **Configure Render to use Docker Hub**
   - Set Image URL: `yourusername/car-price-predictor:latest`
   - Render pulls and deploys the image

## 💻 Usage

### Web Interface

1. Navigate to the application URL
2. Fill in the car details:
   - Enter manufacturer name (e.g., Toyota, Honda, BMW)
   - Enter model name (e.g., Camry, Civic, 3 Series)
   - Select year (1980-2025)
   - Enter mileage in miles
   - Select fuel type from dropdown
   - Enter engine size in liters
3. Click "Predict Price"
4. View the estimated price

### Programmatic Access

Use the API endpoints to integrate with other applications:

```javascript
// JavaScript/Node.js example
const prediction = await fetch('https://your-app.onrender.com/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    manufacturer: 'Toyota',
    model: 'Camry',
    year: 2020,
    mileage: 30000,
    fuel_type: 'Petrol',
    engine_size: 2.5
  })
});

const data = await prediction.json();
console.log(`Predicted price: $${data.predicted_price}`);
```

## 🔧 Development

### Running in Development Mode

```bash
# With auto-reload (for development only)
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Project Configuration

**requirements.txt** - Production dependencies (minimal):
```txt
fastapi==0.120.0
uvicorn==0.38.0
pandas==2.2.0
numpy==1.26.4
scikit-learn==1.7.2
xgboost==3.1.1
joblib==1.3.2
```

**Dockerfile** - Multi-stage build for optimization:
- Base: Python 3.11 slim (120MB)
- Installs system dependencies (gcc, g++)
- Installs Python packages
- Copies application code
- Exposes port 8000
- Runs uvicorn server

### Environment Variables

The application currently uses hardcoded values. For production, consider using environment variables:

```python
import os

CURRENT_YEAR = int(os.getenv('CURRENT_YEAR', 2025))
MODEL_PATH = os.getenv('MODEL_PATH', 'model.pkl')
PORT = int(os.getenv('PORT', 8000))
```

### Adding New Features

1. **Update the model** - Retrain with new features
2. **Update app.py** - Add feature extraction in `predict_car_price()`
3. **Update index.html** - Add input fields for new features
4. **Update requirements.txt** - If new dependencies are needed
5. **Test locally** - Verify predictions work
6. **Push to GitHub** - Auto-deploys to Render

## 🐛 Troubleshooting

### Common Issues

#### 1. Model Not Found Error
```
FileNotFoundError: model.pkl not found
```
**Solution**: Ensure `model.pkl` is in the same directory as `app.py` and is committed to Git.

---

#### 2. Module Not Found Error
```
ModuleNotFoundError: No module named 'xgboost'
```
**Solution**: Install missing dependencies:
```bash
pip install -r requirements.txt
```

---

#### 3. Docker Build Fails on M1 Mac
```
exec format error
```
**Solution**: Build for linux/amd64 platform:
```bash
docker build --platform linux/amd64 -t car-price-predictor .
```

---

#### 4. Port Already in Use
```
Error: Address already in use
```
**Solution**: Kill the process using port 8000:
```bash
# Find the process
lsof -ti:8000

# Kill it
kill -9 $(lsof -ti:8000)
```

---

#### 5. CORS Errors
```
Access to fetch has been blocked by CORS policy
```
**Solution**: The app already has CORS enabled for all origins. If still blocked, check browser console for specific error.

---

#### 6. Render Cold Start Delay
The first request after 15 minutes of inactivity takes 30-60 seconds.

**Solution**: This is normal on Render's free tier. Upgrade to a paid plan for always-on service, or use a service like [UptimeRobot](https://uptimerobot.com/) to ping your app periodically.

### Getting Help

- **Check Logs**: 
  - Local: Check terminal output
  - Render: View logs in Render dashboard
- **GitHub Issues**: Open an issue in the repository
- **Render Support**: [Render Documentation](https://render.com/docs)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
   ```bash
   python app.py  # Test locally
   docker build -t test . && docker run -p 8000:8000 test  # Test with Docker
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI team for the excellent web framework
- XGBoost developers for the powerful ML library
- Render for easy deployment platform
- The open-source community

## 📞 Contact

**Your Name** - [@yourhandle](https://twitter.com/yourhandle)

**Project Link**: [https://github.com/yourusername/AI-powered-car-price-predictor](https://github.com/yourusername/AI-powered-car-price-predictor)

**Live Demo**: [https://car-price-predictor.onrender.com](https://car-price-predictor.onrender.com)

---

**Made with ❤️ by [Your Name]**

*Last Updated: October 2025*
