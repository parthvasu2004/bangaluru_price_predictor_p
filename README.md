🏡 **Bengaluru House Price Predictor**


🔗 Repository: parthvasu2004/bangaluru_price_predictor_p


🚀 Overview


The Bengaluru House Price Predictor is a machine learning-powered web application designed to estimate the price of residential properties in Bengaluru based on various factors such as location, number of bedrooms, square footage, and amenities. The application utilizes Ridge Regression for prediction and is deployed using Flask.


🛠️ Features
✔️ Accurate House Price Prediction using real estate market data.
✔️ Machine Learning Model trained using Ridge Regression.
✔️ Flask Web Application with a user-friendly interface.
✔️ Data-Driven Insights for informed property buying/selling decisions.
✔️ Live Deployment on Render for real-time predictions.


📂 Project Structure


bangaluru_price_predictor_p/
│── templates/              # HTML templates for the web app  
│── app.py                  # Flask web application  
│── Cleaned_data.csv        # Preprocessed dataset  
│── RidgeModel.pkl          # Trained ML model  
│── requirements.txt        # Python dependencies  
│── .gitignore              # Ignored files  
│── README.md               # Project documentation 


⚙️ Installation & Setup


1️⃣ Clone the Repository


git clone https://github.com/parthvasu2004/bangaluru_price_predictor_p.git
cd bangaluru_price_predictor_p


2️⃣ Create & Activate Virtual Environment (Optional but Recommended)


python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


3️⃣ Install Dependencies


pip install -r requirements.txt


4️⃣ Run the Application


python app.py
Visit http://127.0.0.1:5000/ in your browser to access the web app.


🎯 How It Works


1️⃣ Enter Property Details – Input specifications like location, square footage, number of bedrooms, and amenities.

2️⃣ Predict House Price – The model estimates the property's market value.

3️⃣ Make Informed Decisions – Helps buyers and sellers understand fair market prices.


🔍 Machine Learning Model


Algorithm Used: Ridge Regression

Dataset: Preprocessed Bengaluru housing dataset (Cleaned_data.csv).

Pretrained Model: Stored as RidgeModel.pkl.


🔗 Live Deployment

The application is deployed on Render. Try it out here: https://bangaluru-price-predictor-mhp.onrender.com


🤝 Contribution

Contributions are welcome! Feel free to fork this repository, create feature branches, and submit pull requests.


📜 License

This project is licensed under the MIT License – free to use and modify.


📬 Contact

👤 Parth Pandey
📧 parthvasu2004@gmail.com
🔗 https://www.linkedin.com/in/parth-pandey-3442a9256/
