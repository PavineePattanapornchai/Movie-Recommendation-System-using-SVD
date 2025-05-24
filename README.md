# Movie Recommendation System using SVD

## 📚 Overview
This project presents a **Movie Recommendation System** using the **Singular Value Decomposition (SVD)** approach on the **MovieLens dataset**. The goal is to accurately predict user-movie ratings and improve personalized recommendations.

## 🎯 Objective
- Develop a recommendation model leveraging collaborative filtering.
- Train using `ratings_train.csv` and validate with `ratings_valid.csv`.
- Utilize `movies.csv` for enriching the data.
- Evaluate model performance using **Root Mean Square Error (RMSE)**.

## 🏗️ Project Structure
```
├── .github/workflows
│   └── run_training.yml
├── data
│   ├── movies.csv
│   ├── ratings_train.csv
│   └── ratings_valid.csv
├── src
│   └── recommendation_system.py
├── .gitignore
├── requirements.txt
├── environment.yml
└── svd_model.pkl
```

## 🔍 Key Features
- Collaborative Filtering with **SVD**.
- Model serialization for efficient reuse.
- Automated training and validation with GitHub Actions.
- Professional project structure for scalability.

## 🚀 Setup
```bash
# Clone repository
git clone https://github.com/PavineePattanapornchai/Movie-Recommendation-System-using-SVD.git
cd Movie-Recommendation-System-using-SVD

# Create conda environment
conda env create -f environment.yml
conda activate movie-env

# Run training script
python src/recommendation_system.py
```

## 📈 Evaluation
- RMSE on validation set is displayed after training.
- Model is saved as `svd_model.pkl`.

## 📂 Workflow Automation
- **GitHub Actions** automates training on every push.

## 🗺️ Data Flow Diagram
![Data Flow Diagram](C:/Users/asus/Downloads/Flow Diagram.png)

## 👩‍💻 Author
- **Pavinee Pattanapornchai**

## 📬 Contact
For inquiries or collaborations, please reach out via [GitHub](https://github.com/PavineePattanapornchai).
