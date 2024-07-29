import streamlit as st
import requests

st.title("Prédiction du comportement des  Clients")

# Saisie des informations client
gender = st.selectbox("Genre", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (mois)", min_value=0, max_value=100)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)

# Créer un dictionnaire avec les données
data = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

# Faire la prédiction
if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict", json=data)
    result = response.json()
    prediction_proba = result["probability"]
    st.write("Probabilité = ", prediction_proba)

    # Affichage du résultat avec des messages de succès, avertissement et erreur
    if prediction_proba < 0.33:
        st.success("Le client n'est pas susceptible de vous quitter. ")
    elif 0.33 <= prediction_proba < 0.67:
        st.warning("Le client a un risque moyen de vous quitter.")
    else:
        st.error("Le client est susceptible de vous quitter.")


# Sidebar
st.sidebar.write("**Mes Coordonnées :**")
st.sidebar.write("**Nom:** MAMA Moussinou")
st.sidebar.write("**Email:** mamamouhsinou@gmail.com")
st.sidebar.write("**Téléphone:** +229 95231680")
st.sidebar.write("**LinkedIn:** moussinou-mama-8b6270284")

# Ajouter une photo
#sst.sidebar.image("mm.png", caption='MAMA Moussinou')

# Ajouter un message sous la photo
st.write("**Made by MAMA Moussinou**")
