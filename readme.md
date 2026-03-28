# 💜 MoodSpace

> An AI-powered web application that allows users to express their emotions, receive supportive responses, and track their mental well-being over time.

---
🌸 Overview

MoodSpace is a web-based emotional wellness application designed to provide a safe, non-judgmental space for users to express their feelings, track their mood, and gain insights into their emotional patterns over time.

It combines AI-powered conversations with mood tracking and visualization, making it more than just a journaling tool — it acts like a digital companion.

🧩 Problem Statement

In today’s fast-paced student life, many individuals face:

Stress and anxiety
Emotional isolation
Lack of someone to talk to
Limited access to affordable therapy

Most existing solutions:

Feel robotic or impersonal
Offer generic responses
Do not track emotional progress

👉 This creates a gap where users have emotions but no consistent outlet to express them.
------
## 📌 What This Project Does

MoodSpace is designed as a **digital emotional companion**.

It allows users to:

* Share how they feel in natural language
* Receive empathetic, human-like responses
* Automatically detect their mood
* Track emotional patterns using graphs
* Gain insights into their mental well-being

The goal is simple:

> *Provide a safe space for people who need someone to listen.*
------
🎯 Why It Matters

Mental health affects:

📚 Academic performance
🧠 Decision-making
🤝 Relationships
🌱 Overall well-being

MoodSpace aims to:

Encourage emotional expression
Reduce mental burden
Help users understand their emotional trends
💡 Solution
---

## 🎯 Key Features

* 💬 **AI Chat Support** — Real-time emotional responses
* 📊 **Mood Tracking** — Stores user entries with timestamps
* 📈 **Mood Graph** — Visual representation of emotional trends
* 🧠 **Smart Insights** — Detects patterns in mood data
* 🎨 **Premium UI** — Clean lavender-themed interface

---

## 🛠️ Technologies Used

* **Python (Flask)** — Backend framework
* **HTML & CSS** — Frontend design
* **Pandas** — Data handling
* **Matplotlib** — Graph generation
* **Requests** — API communication
* **Ollama (LLaMA 3)** — Local AI for chat
---

MoodSpace provides:

*🗣️ Natural language emotional expression
*🤖 Empathetic AI responses
*📈 Mood tracking with graphs
*🔍 Insights into emotional patterns
*⚙️ Tech Stack
*🔹 Backend
*Python (Flask)
*🔹 Frontend
*HTML, CSS (calming lavender UI)
*🔹 Data Handling
*CSV-based storage
*🔹 Visualization
*Matplotlib
*🔹 AI Integration
*Local AI using Ollam
---

## ⚙️ Setup Instructions (Step-by-Step)

Follow these steps to run the project on your system:

---

### 1️⃣ Clone the Repository

```bash id="p7k7m3"
git clone https://github.com/yourusername/moodspace.git
cd moodspace
```

---

### 2️⃣ Install Required Libraries

Make sure Python is installed, then run:

```bash id="h8k2n1"
pip install flask pandas matplotlib requests
```

---

### 3️⃣ Install and Run AI (Ollama)

MoodSpace uses **local AI**, so no paid API is required.

#### 👉 Install Ollama:

Download from: https://ollama.com

#### 👉 Run the AI model:

```bash id="v2k9d4"
ollama run llama3
```

⚠️ Keep this running in the background.

---

### 4️⃣ Run the Application

```bash id="r4t6y8"
python app.py
```

---

### 5️⃣ Open in Browser

Go to:

```id="u9w3x2"
http://127.0.0.1:5000
```

---

## 🧪 How to Use

1. Open the website
2. Enter how you feel (e.g., “I feel stressed today”)
3. Click submit
4. The app will:

   * Detect your mood
   * Respond with supportive text
   * Save your entry
   * Update the mood graph

---

## 📂 Project Structure

```id="z1x2c3"
moodspace/
│
├── app.py                 # Main backend logic
├── mood_data.csv          # Stores user mood history
│
├── static/
│   ├── style.css          # UI styling
│   └── mood_graph.png     # Generated graph
│
├── templates/
│   └── index.html         # Frontend page
│
└── README.md              # Project documentation
```

---

## ⚠️ Common Errors & Fixes

### ❌ Error: `requests is not defined`

✔ Fix:

```bash id="fix1"
pip install requests
```

And add:

```python id="fix2"
import requests
```

---

### ❌ Error: `EmptyDataError`

✔ Fix: Delete or recreate `mood_data.csv` with headers:

```id="fix3"
date,text,sentiment,score
```

---

### ❌ Error: AI not responding / quota exceeded

✔ Cause: OpenAI API limit
✔ Fix: Use Ollama instead (free local AI)

---

### ❌ Graph not updating

✔ Fix:

* Ensure CSV is saving correctly
* Refresh browser (Ctrl + F5)

---

## ⚠️ Limitations

* Not a replacement for professional mental health care
* Requires local AI setup for full functionality
* Data is stored locally (not cloud-based)

---

## 🔮 Future Improvements

* User authentication (login system)
* Cloud database integration
* Voice chat support
* Mobile-friendly version
* Advanced emotional analysis
----
## 📊 **Output**
*📄 Stores emotional data in CSV
*📈 Generates dynamic mood graphs
*🤖 Displays AI responses in real-time
*🚧 Challenges Faced
*❌ API quota limitations → switched to local AI
*❌ CSV errors → fixed with proper initialization
*❌ Backend bugs → resolved via debugging
*❌ Graph issues → corrected data mapping
*❌ AI response issues → fixed dependencies
---

## 🤝 Contribution

You can contribute by:

1. Forking the repository
2. Creating a new branch
3. Making improvements
4. Submitting a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💜 Final Thought

MoodSpace is built for people who may not always have someone to talk to.

> *Sometimes, being heard is the first step to healing.*

---
