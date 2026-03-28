# 💜 **MoodSpace**

> *An AI-powered emotional companion designed to listen, understand, and support users while tracking their mental well-being.*

---

## 🌍 **Introduction**

MoodSpace is a web-based application that provides a **safe, private, and judgment-free space** for users to express their emotions. It combines **AI conversation**, **mood tracking**, and **data visualization** to create a meaningful mental wellness experience.

This project is built with a simple idea:

> *Everyone deserves someone to listen.*

---

## 🧠 **Problem**

Many individuals, especially students:

* Feel emotionally overwhelmed
* Do not have someone to talk to
* Cannot afford therapy
* Struggle to track their mental health

Most existing tools:

* Provide generic responses
* Lack emotional depth
* Do not show meaningful progress

---

## 💡 Solution

MoodSpace provides:

* 💬 Real-time AI conversation
* 📊 Mood tracking over time
* 📈 Visual emotional insights
* 💜 A calming and premium user experience

---

## ✨ Features

### 💬 AI Chat

* Human-like responses
* Emotion-aware interaction
* Works in real-time (via Ollama / local AI)

---

### 📊 Mood Tracking

* Stores user input with date
* Detects emotions (Happy, Sad, Angry, Depressed, etc.)
* Maintains a history of entries

---

### 📈 Mood Graph

* Visual representation of emotional trends
* Tracks progress over time
* Color-coded for clarity

---

### 🧠 Smart Insights

* Identifies emotional patterns
* Highlights trends like:

  * Frequent sadness
  * Mood improvement
  * Emotional fluctuations

---

### 🎨 Premium UI

* Soft lavender theme
* Clean, modern layout
* Designed for comfort and usability

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **Data Handling:** Pandas
* **Graphing:** Matplotlib
* **AI Engine:** Ollama (LLaMA 3)
* **API Handling:** Requests

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/moodspace.git
cd moodspace
```

---

### 2. Install Dependencies

```bash
pip install flask pandas matplotlib requests
```

---

### 3. Install & Run AI (Ollama)

Download Ollama from: https://ollama.com

Then run:

```bash
ollama run llama3
```

---

### 4. Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
moodspace/
│
├── app.py
├── mood_data.csv
├── static/
│   ├── style.css
│   └── mood_graph.png
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## 🔍 How It Works

1. User enters their thoughts
2. Sentiment analysis detects mood
3. AI generates a response
4. Data is stored in CSV
5. Graph updates automatically
6. Insights are generated

---

## 📊 Example

**Input:**

> I feel really stressed today

**Output:**

* Emotion detected: *Stress / Negative*
* AI responds with support
* Entry saved
* Graph updated

---

## ⚠️ Limitations

* Not a substitute for professional therapy
* Requires local AI setup for full functionality
* CSV storage is not scalable

---

## 🔮 Future Improvements

* User login system
* Cloud database integration
* Voice-based interaction
* Mobile app version
* Emergency mental health support

---

## 🤝 Contribution

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 💜 Final Note

MoodSpace is built with empathy at its core.

> *Technology should not just be smart — it should be kind.*

---
