# SpamSense

SpamSense is an AI-powered tool that predicts whether your marketing emails will land in the inbox or spam folder. Built for agencies to optimize campaign deliverability before sending.  
It leverages Streamlit for the user interface and scikit-learn for building and serving the spam classifier.

## Features

- Predicts if marketing emails will be classified as spam or delivered to the inbox
- Optimized for agencies and campaign managers
- Simple web interface built with Streamlit
- Pre-trained machine learning model

## Working Project

![Demo](assets/demo.gif)

## Project Structure

```
.
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── setup.sh                # Streamlit server setup script
├── Procfile                # For deployment (e.g., Heroku)
├── ml-model-training/
│   ├── sms-spam-classifier.ipynb  # Model training notebook
│   └── spam.csv                   # Dataset
├── models/
│   ├── model.pkl           # Trained model
│   └── vectorizer.pkl      # Trained vectorizer
├── .gitignore
├── .slugignore
└── README.md
```

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd SpamSense
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```sh
   streamlit run app.py
   ```

## Deployment

- The app is ready for deployment on platforms like Heroku or Slug.
- The `Procfile` and `setup.sh` are included for deployment configuration.

## Training

- Model training is done in [`ml-model-training/sms-spam-classifier.ipynb`](ml-model-training/sms-spam-classifier.ipynb) using the [`ml-model-training/spam.csv`](ml-model-training/spam.csv) dataset.
- Trained artifacts are saved in the [`models/`](models/) directory.

## License

MIT License
