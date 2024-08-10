import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


st.write("Dataset Selection and Machine Learning")

st.sidebar.header('Upload Your Datasets')  

dataset_name= st.sidebar.selectbox ("Select the Database", ("Expresso churn", "Financial Inclusion in Africa") )

st.write (dataset_name)

classifier_name = st.sidebar.selectbox ("Select Classifier", ("Logistic Regression", "KNN", "SVC") )

def load_data(uploaded_file):
    # Check if the file is uploaded
    if uploaded_file is not None:
        # Read the file into a pandas DataFrame
        data = pd.read_csv(uploaded_file)
        return data
    return None


uploaded_file1 = st.sidebar.file_uploader("Choose the first dataset", type="csv")
uploaded_file2 = st.sidebar.file_uploader("Choose the second dataset", type="csv")

# Allow the user to select between the two datasets
dataset_choice = st.sidebar.radio("Select dataset to use", ["Dataset 1", "Dataset 2"])

# Load the selected dataset
if dataset_choice == "Dataset 1":
    data = load_data(uploaded_file1)
else:
    data = load_data(uploaded_file2)

if data is not None:
    st.write("Data preview:")
    st.write(data.head())
    st.write("Shape of the Dataset" , data.shape)



    
target_column = st.sidebar.selectbox("Select Target Column", data.columns, key="target_column")


def add_parameter(clf_name) :
        params = dict()
        if clf_name == "KNN" :
            K = st.sidebar.slider ("K", 3, 30)
            params ["K"] = K
            return params
        elif clf_name == "SVC" :
            C = st.sidebar.slider ("C", 0.01, 10.0)
            params ["C"] = C
        else :
            max_iterations = st.sidebar.slider ("Max_iterations", 10, 600)
            params ["max_iterations"] = max_iterations
        return params

params = add_parameter(classifier_name)

def get_classifier (clf_name, params) :
    if clf_name == "KNN" :
        clf = KNeighborsClassifier(n_neighbors= params["K"])        
    elif clf_name == "SVC"     :
        clf = SVC (C = params["C"])
    else :
        clf = LogisticRegression (max_iter = params["max_iterations"])
    return clf
clf = get_classifier(classifier_name, params)



if data is not None:
    if not data.empty:  # Vérifie que les données ne sont pas vides
    
        y = data[target_column].values
        features = data.drop(target_column , axis = 1)
        x = features.values
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)

        acc = accuracy_score(y_test, y_pred)
        st.write(f"classifier = {classifier_name}")
        st.write(f"accuracy = {acc}")
    else:
        st.write("There is no data uploaded.")
else:
    st.write("Upload your data.")