import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Mise à jour stock Tissu :scissors: :shirt:")

df = pd.read_csv("tissu.csv").drop("Unnamed: 0", axis = 1)

st.dataframe(df)

st.title("Choisis le tissu découpé :")

tissu = st.selectbox("Tissu", df.Tissu.values)
if tissu :
    st.dataframe(df[df.Tissu == tissu])
    actual_length = df[df.Tissu == tissu].Longueur.values[0]
    st.text("La longueur actuelle est de " + str(actual_length) + " m.")
    if actual_length == 0:
        st.text("Il n'y a plus de " + str(tissu) + " en stock.")
    else :
        st.title("Choisis la longueur à découper : :straight_ruler:")
        to_cut = st.slider("Longueur à découper", min_value = 0, max_value = int(actual_length))
        st.text("La longueur découpée est de " + str(to_cut) + " m.")
        new_length = int(int(actual_length) - int(to_cut))
        new_stock = st.button("Mettre à jour le stock.")
        if new_stock:
            df.loc[df["Tissu"]==tissu, ["Longueur"]] = new_length
            df.loc[df["Tissu"]==tissu, ["Date de Modification"]] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            st.dataframe(df)
            df.to_csv("tissu.csv")