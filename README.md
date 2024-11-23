# DatathonFME2024
## Real estate price prediction model using MLflow and Streamlit developed during the Datathon.

This project was developed during the Datathon FME 2024, where we aimed to create a real estate price prediction tool. The application leverages machine learning to estimate the price of a house based on user-defined parameters, using a trained model and a simple, user-friendly web interface.

### Project Overview

This project predicts real estate prices using a machine learning model trained on a dataset of over 100,000 houses from Chicago and surrounding areas. Key features include data preprocessing, model training, and evaluation using MLflow for experiment tracking. The file where the pipeline is fit is a reference of an initial model given by the organizers, at the end of the README file it can be found a link to their repository. The model is deployed through a Streamlit application where users can input house details and receive price predictions. Key files include:
- **model_training.ipynb**: Contains the model training pipeline, this file is for reference only and cannot be executed.
- **model.pkl**: Contains the model that the application uses.
- **app.py**: Contains the Streamlit app for interactive predictions, the file to be run.

### Repository Structure

```plaintext
├── LICENSE
├── requirements.txt
├── models
│   ├── model.pkl
├── src
    ├── app.py
    │   
    └── model_training.ipynb
```
- **`LICENSE`**: Contains the license information.
- **`requirements.txt`**: Lists all the Python packages required to run the app.py file.
- **`models/`**: Contains the training model file.
  - **`model.pkl`**: Machine learning model trained on the real estate dataset.
- **`src/`**: Contains the source code.
  - **`app.py`**: Contains the Streamlit application.
  - **`model_training.ipynb`**: Jupyter notebook detailing the full pipeline for data preprocessing, model training, evaluation, and feature importance analysis.

### Setup and Installation

#### Clone the Repository
```plaintext
git clone <repository-url>
```
#### Navigate to the Repository
```plaintext
cd <repository-directory>
```
#### Create a Virtual Environment
```plaintext
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```
#### Install the Dependencies
```plaintext
pip install -r requirements.txt
```

### Objectives
- Use a large dataset of houses from Chicago and its surrounding areas to train a price prediction model.
- Develop an intuitive application where users can input house details and get an estimated price.

### Description of the project

#### Clean Data
- The dataset contains over 100,000 records of houses with more than 50 features, such as the number of bathrooms, lot size, location, and rooms quality and condition.
- Irrelevant or redundant features were removed to improve the model's performance.

#### Model Training
- Choose the Random Forest Regressor model to capture complex patterns in the data.
- Prepare a pipeline by combining the preprocessor and the model choosen.
- Fit the pipeline using MLflow tracking.
- Evaluate the model
- Save the model to a .pkl file

#### Streamlit Application
- Using the Streamlit library in python an interactive application was built to test the model. Users can input details about a hypothetical house (size, number of rooms, parking, etc) to receive an estimated price instantly.

### Acknowledgments
I would like to express my heartfelt thanks to my amazing team members who contributed to this project:
- Víctor Brull, me
- Francesc Baiget 
- Oriol Carreras
- Carolina Henao

Together, we worked hard to develop this real estate price prediction model and make it a reality.
Lastly, I’d like to give credit to the FME of the UPC for providing a repository, which helped us in developing our machine learning solution.

Link to the repository: https://github.com/JoanObregonLopez/mlflow_uni_demo.git

