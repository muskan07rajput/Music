import streamlit as st
import matplotlib.pyplot as plt
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import pygame
import os

# Make sure to download VADER lexicon


# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define music paths
music_paths = {
    "Very Happy": r"C:\Users\muska\OneDrive\Desktop\java11\Carvine_-_Very_Happy.mp3",
    "Happy": r"C:\Users\muska\OneDrive\Desktop\java11\Wonder_-_Exogenis.Official.mp3",
    "Neutral": r"C:\Users\muska\OneDrive\Desktop\java11\mitwa.mp3",
    "Sad": r"C:\Users\muska\OneDrive\Desktop\java11\sad_song_-_chausson-opium.mp3",
    "Very Sad": r"C:\Users\muska\OneDrive\Desktop\java11\A_very_sad_story_-_Dave_Imbernon.mp3"
}

# Mood detection function
def detect_mood(compound):
    if compound >= 0.6:
        return "Very Happy"
    elif compound >= 0.2:
        return "Happy"
    elif compound >= -0.2:
        return "Neutral"
    elif compound >= -0.6:
        return "Sad"
    else:
        return "Very Sad"


st.title("🎶 Mood Music Player")
text = st.text_area("How are you feeling today?")

if text:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    st.write("TextBlob Polarity Score:", polarity)

    vader_scores = analyzer.polarity_scores(text)
    st.write("VADER Sentiment Scores:", vader_scores)

    compound = vader_scores['compound']
    mood = detect_mood(compound)
    st.subheader(f"🎭 Detected Mood: {mood}")

    # Plotting VADER scores
    st.write("🔍 VADER Sentiment Breakdown")
    fig, ax = plt.subplots()
    ax.bar(vader_scores.keys(), vader_scores.values(), color='skyblue')
    ax.set_title("VADER Sentiment Scores")
    st.pyplot(fig)

    music_file = music_paths.get(mood)
    if os.path.exists(music_file):
        st.success(f"🎵 Playing {mood} song.")
        st.audio(music_file, format='audio/mp3')
    else:
        st.warning("Music file not found for this mood.")







