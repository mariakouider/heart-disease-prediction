# Heart Disease Prediction

This project leverages machine learning to predict the presence of heart disease based on clinical and physiological variables. The model is trained using the `RandomForestClassifier` and evaluates critical features such as cholesterol levels, blood pressure, and ECG results.

## Features
- **Interactive Web Application**: Built with Flask, allowing users to input clinical data and receive predictions.
- **Machine Learning Model**: Predicts the likelihood of heart disease and provides the result along with probability.
- **Tooltips**: Offers guidance for each input field.
- **Visualizations**: Displays an interactive graph showcasing important features.
- **User-Centric Design**: Designed with simplicity and clarity to accommodate healthcare professionals and researchers.

## Dataset
The dataset used in this project is:
1. [Heart Attack Prediction on Kaggle](https://www.kaggle.com/code/sainikhiljallepalli/heart-attack-prediction-90-accuracy/input)
2. [UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)

### Dataset Details
- **Source**: The data is sourced from reputable repositories to ensure quality and reliability.
- **Features**:
  - Age
  - Sex
  - Chest pain type
  - Resting blood pressure
  - Cholesterol level
  - Maximum heart rate achieved
  - Exercise-induced angina
  - ST depression induced by exercise
- **Significance**: Each feature was selected based on its relevance to predicting cardiovascular health.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd heart-disease-prediction
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Local Deployment
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open the browser and navigate to `http://127.0.0.1:5001`.
3. Input the clinical data and click **Predict**.

### Deployment on Heroku
1. Ensure you have the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed and are logged in.
2. Create a new Heroku app:
   ```bash
   heroku create <your-app-name>
   ```
3. Add the remote repository for Heroku:
   ```bash
   git remote add heroku https://git.heroku.com/<your-app-name>.git
   ```
4. Add a `Procfile` to your project with the following content:
   ```text
   web: python app.py
   ```
5. Push your code to Heroku:
   ```bash
   git push heroku main
   ```
6. Scale the web dynos:
   ```bash
   heroku ps:scale web=1
   ```
7. Open the app in your browser:
   ```bash
   heroku open
   ```

## File Structure
- **`app.py`**: Main application file.
- **`templates/`**: HTML templates for the web pages.
- **`static/`**: Static files such as images.
- **`model/`**: Directory containing the pre-trained Random Forest model (`rf_model.pkl`).
- **`data/`** (optional): Stores the original dataset for reference.

## Technical Details
- **Programming Language**: Python
- **Framework**: Flask
- **Machine Learning Library**: Scikit-learn
- **Visualization Libraries**: Matplotlib, Plotly
- **User Guidance**: Integrated tooltips to explain input fields.
- **Deployment**: Local deployment through Flask; can be extended for cloud services like Heroku.

## Future Improvements
- Adding more visualizations for better interpretability.
- Expanding the dataset for improved generalization.
- Adding real-time data integration for dynamic predictions.
- Introducing a confidence score for predictions.

## Personal Touch
As a passionate advocate for data-driven healthcare solutions, I designed this project to combine simplicity with precision. The goal is to empower healthcare professionals with accessible machine learning tools that can aid in early detection and preventive care.

## Credits
The dataset is sourced from Kaggle and the UCI Machine Learning Repository. Special thanks to the open-source community for providing tools that made this project possible.

