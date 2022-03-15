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



st.title('Graphique interactif de distribution filtré par région')

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
    st.write("Les voitures américaines sont celles qui possèdent le plus de cylindres. Ce sont les plus puissantes.")
    st.write("Le nombre moyen de cylindres des voitures européennes et japonaises sont très proches.")
       
    
st.title('Graphique de corrélations filtré par région')


continent2 = st.radio("Choix de la zone géographique pour la heatmap de corrélations :", ("US", "Europe", "Japon"))
if continent2 == "US":
    hm_cars = sns.heatmap(round(df_cars[df_cars['continent'].str.contains('US.')].corr(), 2), annot = True, center=0, cmap=sns.color_palette("vlag", as_cmap=True))
    st.pyplot(hm_cars.figure, clear_figure = True)
    st.write('Voici la heatmap filtré sur les US.')
elif continent2 == "Europe" :
    hm_cars2 = sns.heatmap(round(df_cars[df_cars['continent'].str.contains('Europe.')].corr(), 2), annot = True, center=0, cmap=sns.color_palette("vlag", as_cmap=True))
    st.pyplot(hm_cars2.figure, clear_figure = True)
    st.write("Voici la heatmap filtrée sur l'Europe.")
elif continent2 == "Japon":
    hm_cars3 = sns.heatmap(round(df_cars[df_cars['continent'].str.contains('Japan.')].corr(), 2), annot = True, center=0, cmap=sns.color_palette("vlag", as_cmap=True))
    st.pyplot(hm_cars3.figure, clear_figure = True)
    st.write("Voici la heatmap filtrée sur le Japon.")
    st.write("Pour les trois régions, on reconnaît bien une corrélation positive entre 'cylinders', 'cubicinches', 'hp' et 'weightlbs'.")




                  



