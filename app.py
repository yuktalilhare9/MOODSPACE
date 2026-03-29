# ===== IMPORTS =====
from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime
import os

# Fix matplotlib GUI error
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

# ===== FILE SETUP =====
FILE = "mood_data.csv"

# Create file if not exists or empty
if not os.path.exists(FILE) or os.stat(FILE).st_size == 0:
    pd.DataFrame(columns=["date", "text", "sentiment", "score"]).to_csv(FILE, index=False)


# ===== SENTIMENT DETECTION =====
def analyze_sentiment(text):
    text = text.lower()

    if any(word in text for word in ["happy","good","great","excited","love"]):
        return "Happy"
    elif any(word in text for word in ["sad","bad","upset","cry","depressed","lonely","tired"]):
        return "Sad"
    elif any(word in text for word in ["angry","mad","frustrated","annoyed"]):
        return "Angry"
    elif any(word in text for word in ["stress","anxious","worried","overthinking"]):
        return "Anxious"
    else:
        return "Neutral"


# ===== HUMAN-LIKE RESPONSE =====
def generate_response(mood, text):

    if mood == "Sad":
        return [
            "That sounds really heavy. I'm really glad you shared it here.",
            "You don’t have to deal with everything at once.",
            "Try doing one small thing for yourself right now—even drinking water helps."
        ]

    elif mood == "Angry":
        return [
            "I can sense your frustration.",
            "It's okay to feel angry—it usually means something matters.",
            "Pause for a moment and take a few slow breaths."
        ]

    elif mood == "Anxious":
        return [
            "It sounds like your mind is racing.",
            "You're not alone—this happens to many people.",
            "Try grounding: name 5 things you can see around you."
        ]

    elif mood == "Happy":
        return [
            "That’s really nice to hear 😊",
            "Moments like these matter more than we realize.",
            "Take a second to appreciate this feeling."
        ]

    else:
        return [
            "Thanks for sharing that with me.",
            "Even small check-ins matter.",
            "Take things one step at a time."
        ]


# ===== GRAPH FUNCTION =====
def generate_graph():
    try:
        df = pd.read_csv(FILE)

        if df.empty:
            return None

        df = df.dropna()

        df["date"] = pd.to_datetime(df["date"], errors='coerce')
        df = df.dropna(subset=["date"])

        mapping = {
            "Happy": 2,
            "Neutral": 1,
            "Sad": 0,
            "Angry": -1,
            "Anxious": -2
        }

        df["value"] = df["sentiment"].map(mapping)
        df = df.dropna()

        df = df.sort_values("date")

        plt.figure(figsize=(10,5))

        plt.plot(df["date"], df["value"], marker='o')

        plt.title("Your Mood Journey 💜")
        plt.xlabel("Date")
        plt.ylabel("Mood Level")

        plt.xticks(rotation=30)
        plt.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig("static/mood_graph.png")
        plt.close()

        return "static/mood_graph.png"

    except Exception as e:
        print("Graph Error:", e)
        return None


# ===== MAIN ROUTE =====
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    response = []

    try:
        df = pd.read_csv(FILE)
    except:
        df = pd.DataFrame(columns=["date", "text", "sentiment", "score"])

    if request.method == "POST":
        text = request.form.get("mood", "")

        if text.strip() != "":
            mood = analyze_sentiment(text)
            response = generate_response(mood, text)

            file_exists = os.path.exists(FILE) and os.stat(FILE).st_size > 0

            pd.DataFrame([{
                "date": datetime.now().strftime("%Y-%m-%d"),
                "text": text,
                "sentiment": mood,
                "score": 0
            }]).to_csv(FILE, mode='a', header=not file_exists, index=False)

            message = f"Detected Mood: {mood}"

    graph = generate_graph()

    try:
        df = pd.read_csv(FILE)
    except:
        df = pd.DataFrame()

    return render_template(
        "index.html",
        message=message,
        response=response,
        graph=graph,
        data=df.tail(5)
    )


# ===== RUN =====
if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))