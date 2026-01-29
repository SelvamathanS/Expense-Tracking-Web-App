# Expense Tracking Web App

A web application to manage personal finances by tracking expenses and visualizing spending and balance. Users can add, edit, and view expense records via a UI with password protected.

## 🧠 Features

* Record daily expenses with category and amount
* View history of past expenses
* Simple dashboard to summarize financial data
* Lightweight web interface for quick expense tracking
* Privacy for passwords(Hash passwords)

## 📦 Tech Stack

* **Backend:** Python (Flask), neon db cloud for database(online)
* **Frontend:** HTML, CSS, JavaScript
* **Templates:** Jinja2 (Flask)
* **Dependencies:** Listed in `requirements.txt`
* Optional deployment tools: `Dockerfile`, `Procfile` for hosting setups

## 🛠️ Setup & Installation

1. **Clone the Repo**

   ```bash
   git clone https://github.com/SelvamathanS/Expense-Tracking-Web-App
   cd Expense-Tracking-Web-App
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**

   * Create or update a `.env` file to store config (secret keys, DB URL if needed).

5. **Run the App**

   ```bash
   python app.py
   ```

   Open your browser and visit `http://localhost:5000`

## 🛡️ Notes

* Add proper authentication before production use
* Secure configuration/secret keys in `.env`
