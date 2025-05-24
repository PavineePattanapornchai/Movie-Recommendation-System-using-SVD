# Movie Recommendation System using SVD

A collaborative filtering-based recommendation system built using the MovieLens dataset. This system applies Singular Value Decomposition (SVD) for generating personalized movie recommendations.

---

## 📂 Project Structure

```
.
├── .github/workflows
│   └── run_training.yml         # CI/CD pipeline configuration
├── data
│   ├── movies.csv               # Movie metadata
│   ├── ratings_train.csv        # Training dataset
│   └── ratings_valid.csv        # Validation dataset
├── src
│   └── recommendation_system.py # Core recommendation system implementation
├── .gitignore                   # Git ignore file
├── requirements.txt             # Python dependencies
└── environment.yml              # Conda environment configuration
```

---

## 🚀 Key Features

* **Collaborative Filtering**: Personalized recommendations using user-movie interactions.
* **SVD Model**: Efficient and scalable latent factor model.
* **Validation**: Performance measured by RMSE on validation data.
* **CI/CD Integration**: Automated testing and deployment via GitHub Actions with Micromamba or Conda.
* **Modular Code**: Clean architecture for easy maintenance and extensibility.

---

## 📈 Workflow Overview

![Flow Diagram](images/Flow%20Diagram.png)

---

## 🏗️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/PavineePattanapornchai/Movie-Recommendation-System-using-SVD.git
cd Movie-Recommendation-System-using-SVD
```

### 2️⃣ Setup Conda Environment

```bash
conda env create -f environment.yml
conda activate movie-env
```

### 3️⃣ Install Dependencies (Optional: if using pip)

```bash
pip install -r requirements.txt
```

### 4️⃣ Train Model Locally

```bash
python src/recommendation_system.py
```

---

## 🔁 CI/CD with GitHub Actions

* **Micromamba/Conda Setup**: Efficient environment management and build pipelines.
* **Automated Testing**: Runs training and evaluation on push/pull requests.
* **Fail-Safe Checks**: Ensures model integrity and performance.

---

## 📊 Results

* **Validation RMSE**: 0.88 (example)
* **Model Persistence**: Trained models saved as `svd_model.pkl`

---

## 👤 Author

Pavinee Pattanapornchai

---

## 🔗 License

This project is licensed under the MIT License.
