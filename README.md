# Movie Recommendation System using SVD

This project demonstrates a collaborative filtering-based recommendation system leveraging the MovieLens dataset. The system utilizes Singular Value Decomposition (SVD) to generate personalized movie recommendations and is designed for performance, scalability, and maintainability.

---

## Project Structure

```
Movie-Recommendation-SVD
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
└── environment.yml              
```

---

## Key Features

* **Collaborative Filtering**: Generates personalized movie recommendations based on user-movie interaction data.
* **SVD Model Implementation**: Efficient and scalable approach to collaborative filtering using latent factor models.
* **Performance Validation**: Model accuracy assessed using RMSE on validation data.
* **CI/CD Integration**: Automated workflows with GitHub Actions and Micromamba/Conda for environment management and testing.
* **Modular and Maintainable Codebase**: Clean architecture enabling easy updates and enhancements.

---

## Workflow Overview

![Flow Diagram](images/Flow%20Diagram.png)

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/PavineePattanapornchai/MovieRecSystem.git
cd Movie-Recommendation-System-using-SVD
```

### Set Up Conda Environment

```bash
conda env create -f environment.yml
conda activate movie-env
```

### Install Dependencies (Optional)

```bash
pip install -r requirements.txt
```

### Run the Training Script Locally

```bash
python src/recommendation_system.py
```

---

## Continuous Integration and Deployment (CI/CD)

* **Automated Workflows**: Runs model training and validation on each push or pull request.
* **Micromamba/Conda Environment**: Efficient management of Python dependencies and isolated environments.
* **Quality Checks**: Ensures model stability and performance before merging changes.

---

## Results

* **Validation RMSE**: 0.88 (example value for demonstration purposes)
* **Model Output**: Trained model saved as `svd_model.pkl` for reuse.

---

## Author

Pavinee Pattanapornchai

---

## License

This project is licensed under the MIT License.
