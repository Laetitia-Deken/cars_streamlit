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

st.title('Graphique de corrélations')

viz_correlation = sns.heatmap(round(df_cars.corr(), 2), 
                                center=0, annot = True,
                                cmap = sns.color_palette("vlag", as_cmap=True)
                                )

st.pyplot(viz_correlation.figure)

st.write('On observe de fortes corrélations entre les colonnes cylinders, cubicinches, hp et weightlbs.')
st.write('Au contraire, pas de corrélation forte entre les autres colonnes. Les coefficients sont négatifs.')
         

    
st.title("Autre graphiques") 

st.subheader('Exemple à partir des colonnes weightlbs et cylinders.')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.scatter(
        df_cars["cylinders"],
        df_cars["weightlbs"],
    )

ax.set_title("Distribution between cylinders and weightlbs")
ax.set_xlabel("cylinders")
ax.set_ylabel("weightlbs")

st.pyplot(ax.figure)

st.write('On remarque que plus la voiture possède de cylindres et plus elle est lourde.')


st.title('Et voici un graphique interactif !')

continent = st.radio('Choisissez une région :', ('US', 'Europe', 'Japan'))
if continent == 'US':
    df_cars = df_cars[df_cars.continent == 'US.']
if continent == 'Europe':
    df_cars = df_cars[df_cars.continent == 'Europe.']
if continent == 'Japan':
    df_cars = df_cars[df_cars.continent == 'Japan.']
    

cars_scatter = sns.scatterplot(data=df_cars, x='hp', y='cubicinches')
plt.xlabel('Horsepower')
plt.ylabel('Cubic inches')
plt.title('Cars distribution by continent given there Horsepower and Cubicinches')
st.pyplot(cars_scatter.figure)

st.write('Ces deux colonnes sont fortement corrélées. Les voitures les plus puissantes sont américaines.')
                      
                      
                  



