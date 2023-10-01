import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Hello Wilders, bienvenue ! Analysons le dataset des voitures !')

st.subheader('Découverte des possibilités de streamlit en affichant la base des voitures en entier (désolée pour le scroll ;).')

st.title("Importons d'abord le dataset :")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.table(df_cars)



st.title('Graphique interactif de distribution')

continent = st.radio("Choix de la zone géographique pour afficher les voitures selon leur cylindre", ("US", "Europe", "Japon"))
if continent == "US":
    dp_cars = sns.countplot(df_cars[df_cars['continent'].str.contains('US.')]['cylinders'])
    st.pyplot(dp_cars.figure)
    st.write('Voici le graphique filtré sur les US.')
    st.write('Le nombre moyen de cylindres est :', round(df_cars[df_cars['continent'].str.contains('US.')]['cylinders'].mean(),2))
elif continent == "Europe" :
    dp_cars2 = sns.countplot(df_cars[df_cars['continent'].str.contains('Europe.')]['cylinders'])
    st.pyplot(dp_cars2.figure)
    st.write("Voici le graphique filtré sur l'Europe.")
    st.write('Le nombre moyen de cylindres est :', round(df_cars[df_cars['continent'].str.contains('Europe.')]['cylinders'].mean(),2))
elif continent == "Japon":
    dp_cars3 = sns.countplot(df_cars[df_cars['continent'].str.contains('Japan.')]['cylinders'])
    st.pyplot(dp_cars3.figure)
    st.write("Voici le graphique filtré sur le Japon.")
    st.write('Le nombre moyen de cylindres est :', round(df_cars[df_cars['continent'].str.contains('Japan.')]['cylinders'].mean(),2))
    
       
    
st.title('Graphique de corrélations filtré par région')


# Charger les données dans df_cars
# Nettoyer les valeurs de la colonne 'continent'
df_cars['continent'] = df_cars['continent'].str.strip()

# Sélectionner uniquement les données numériques
num_cols = df_cars.select_dtypes(include='number')

continent2 = st.radio("Choix de la zone géographique pour la heatmap de corrélations :", ("US", "Europe", "Japon"))

if continent2 == "US":
    corr_matrix = num_cols[df_cars['continent'].str.contains('US.')].corr()
    st.write('Voici la heatmap filtrée sur les US.')
elif continent2 == "Europe":
    corr_matrix = num_cols[df_cars['continent'].str.contains('Europe.')].corr()
    st.write("Voici la heatmap filtrée sur l'Europe.")
elif continent2 == "Japon":
    corr_matrix = num_cols[df_cars['continent'].str.contains('Japan.')].corr()
    st.write("Voici la heatmap filtrée sur le Japon.")
    st.write("Pour les 3 régions, 4 colonnes sont positivement corrélées (en rouge).")

plt.figure(figsize=(10, 6))
hm_cars = sns.heatmap(corr_matrix, center=0, cmap=sns.color_palette("vlag", as_cmap=True))
st.pyplot(hm_cars.figure, clear_figure=True)

    



                  



