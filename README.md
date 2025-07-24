# 🌾 KrishiSathi – Empowering Farmers with AI & Technology

> **A full-stack AI-based agricultural platform for smart farming.**

**KrishiSathi** is an end-to-end Django-powered platform designed for farmers, integrating **AI-powered crop disease detection**, a **digital marketplace**, **weather forecasting**, and **agri-news updates** — all in one place. It aims to support small and mid-scale farmers with actionable insights and digital tools to improve crop health, productivity, and market access.

---

## 🔑 Key Features

### 🩺 1. Crop Disease Detection
- Upload a leaf image and get instant disease prediction using a **VGG16 deep learning model**.
- Detects diseases such as:
  - Spider Mite
  - Rust
  - Leaf Blight, etc.
- Trained with transfer learning on a well-curated dataset.

### 🛒 2. Digital Marketplace
- Farmers can **sell** or **buy** agricultural tools, seeds, and products.
- Easy-to-use interface for listing products and making transactions.

### 🌦️ 3. Weather Forecasting
- Live weather forecasts using **web scraping** from trusted sources.
- Helps farmers plan irrigation, sowing, and harvesting.

### 📰 4. Agriculture News Feed
- Get the **latest agricultural and climate news** via scraping.
- Keeps farmers updated and informed.

---

## 🧱 Tech Stack

| Layer        | Technologies Used                                   |
|--------------|-----------------------------------------------------|
| Frontend     | HTML, CSS, Bootstrap                                |
| Backend      | Django (Python)                                     |
| AI Model     | VGG16 (Transfer Learning using Keras/TensorFlow)    |
| Database     | MySQL                                               |
| Web Scraping | BeautifulSoup, Requests                             |
| Project Structure | Cookiecutter Data Science Template             |

---

## 📁 Project Structure

```bash
Crop Disease Detection System  # Project Root: KrishiSathi
├── data/
│   ├── raw/                  # Original image datasets
│   ├── processed/            # Preprocessed/augmented data
│
├── models/                   # Trained AI/ML models
├── notebooks/                # Data exploration, training experiments
├── reports/                  # Visualizations, model metrics
├── src/
│   ├── data/                 # Data loading/transformation scripts
│   ├── features/             # Feature engineering
│   ├── models/               # Model training/prediction
│   └── visualization/        # Visual output of model performance
│
├── docs/                     # Project documentation (Sphinx)
├── requirements.txt          # Python dependencies
├── setup.py                  # Install project as package
├── LICENSE
├── README.md
└── tox.ini

## 📽 Demo

👉 [Click here to view the project demo on LinkedIn](https://www.linkedin.com/posts/vaidehi-kokare-9012aa273_krishisathi-aiinagriculture-django-activity-7340650091248037888-I-2e?utm_source=share&utm_medium=member_desktop&rcm=ACoAAELI-pEBeSyLhk61IR1r3LkwAw_SLypR2Mo)

The demo includes a walkthrough of:
- Crop disease detection using VGG16
- Digital marketplace for farmers
- Real-time weather updates
- Agri-news feed powered by web scraping

