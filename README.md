# 📜 Text Summarization App using BART (Streamlit)

This project is a **Text Summarization Web App** built with
**Streamlit** and **HuggingFace Transformers**.\
It uses the **BART Large CNN model** to generate concise and
high‑quality summaries of long text inputs.

------------------------------------------------------------------------

## 🚀 Features

-   🧠 **AI-powered summarization** using `facebook/bart-large-cnn`
-   🎨 **Beautiful UI** with a custom background image
-   ⚡ Fast inference with `@st.cache_resource`
-   📝 Accepts long text input and produces a clean summary
-   🌐 Runs in browser using Streamlit

------------------------------------------------------------------------

## 📂 Project Structure

    │── app.py
    │── requirements.txt
    │── README.md

------------------------------------------------------------------------

## 🛠️ Installation & Setup

### **1. Clone the repository**

``` bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
```

### **2. Create a virtual environment (optional)**

``` bash
python -m venv venv
venv\Scriptsctivate   # On Windows
```

### **3. Install dependencies**

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the Streamlit App

``` bash
streamlit run app.py
```

The app will open in your browser automatically.

------------------------------------------------------------------------

## 🧠 Model Used

This project uses:

-   **facebook/bart-large-cnn**\
    A pre-trained transformer model fine‑tuned specifically for
    **abstractive summarization**.

------------------------------------------------------------------------

## 📦 Requirements

Use this `requirements.txt`:

    streamlit
    transformers
    torch

------------------------------------------------------------------------

## 🖼️ App Preview

The app features:

-   Sea-themed background\
-   Stylish text input\
-   Clean summarization output

------------------------------------------------------------------------

## ✨ Code Overview

### **Main components:**

-   `pipeline("summarization")` → Loads BART model\
-   `streamlit` UI with text area\
-   Custom CSS for background styling

------------------------------------------------------------------------

## 📜 License

This project is open-source under the **MIT License**.

------------------------------------------------------------------------

## 💡 Future Improvements

-   Add voice-to-text summarization
-   Add PDF summarization
-   Add multi-language support
-   Add extractive + abstractive options

------------------------------------------------------------------------

## 🤝 Contributing

Feel free to submit pull requests or open issues.

------------------------------------------------------------------------

## 🧑‍💻 Author

**Amit Yadav**

------------------------------------------------------------------------

Happy Coding! 🚀
