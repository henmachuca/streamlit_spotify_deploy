import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs",
)


@st.cache_data
def load_data():
    df = pd.read_csv("Files/01 Spotify.csv")
    # Operação pesada
    return df


df = load_data()
st.session_state["df_spotify"] = df

df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artist", artists)
df_filtered = df[df["Artist"] == artist]

albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)

df_filtered2 = df[df["Album"] == album]

col1, col2 = st.columns([0.6, 0.4])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

df
