import streamlit as st
import requests

# Titre de l'application
st.title("Prédiction du Comportement des Clients")

# Formulaire pour saisir les informations des clients
st.header("Informations Client")
gender = st.selectbox("Genre", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partenaire", ["Yes", "No"])
Dependents = st.selectbox("Dépendants", ["Yes", "No"])
tenure = st.number_input("Durée d'adhésion (mois)", min_value=0, max_value=100)
PhoneService = st.selectbox("Service Téléphonique", ["Yes", "No"])
MultipleLines = st.selectbox("Lignes Multiples", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Service Internet", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Sécurité en Ligne", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Sauvegarde en Ligne", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Protection des Appareils", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Support Technique", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Films", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contrat", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Facturation sans papier", ["Yes", "No"])
PaymentMethod = st.selectbox("Méthode de Paiement", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
MonthlyCharges = st.number_input("Frais Mensuels", min_value=0.0)
TotalCharges = st.number_input("Frais Totaux", min_value=0.0)

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
if st.button("Prédire"):
    try:
        response = requests.post("https://msnchurnpredict.onrender.com/predict", json=data)
        response.raise_for_status()  # Vérifie s'il y a des erreurs HTTP
        result = response.json()
        prediction_proba = result["probability"]
        st.write(f"Probabilité de churn: {prediction_proba:.2f}")

        # Affichage du résultat avec des messages de succès, avertissement et erreur
        if prediction_proba < 0.33:
            st.success("Le client n'est pas susceptible de vous quitter.")
        elif 0.33 <= prediction_proba < 0.67:
            st.warning("Le client a un risque moyen de vous quitter.")
        else:
            st.error("Le client est susceptible de vous quitter.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur dans l'appel de l'API: {e}")

# Sidebar avec les coordonnées
with st.sidebar:
    st.write("**Mes Coordonnées :**")
    st.write("**Nom:** MAMA Moussinou")
    st.write("**Email:** mamamouhsinou@gmail.com")
    st.write("**Téléphone:** +229 95231680")
    st.write("**LinkedIn:** [moussinou-mama-8b6270284](https://www.linkedin.com/in/moussinou-mama-8b6270284/)")
    st.image("mm.png", caption='MAMA Moussinou', width=150)
