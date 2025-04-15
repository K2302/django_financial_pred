# 📊 Marketing ROI Analyzer



A clean and beginner-friendly Django web app to track marketing spend, calculate campaign ROI, and gain actionable insights through visualizations.

---

## 📸 Screenshot

![Dashboard UI](https://github.com/K2302/django_financial_pred/blob/main/a.png)

---

## 🚀 Features

- 📥 **Enter Campaigns** – Input marketing channel, budget, conversions, and revenue
- 📊 **ROI Calculation** – See return on investment auto-calculated per channel
- 📈 **Charts** – Spend vs ROI (bar + line), Campaign Share (pie)
- 🏆 **Insights** – Highlights best-performing and costliest campaigns
- 🧑‍💻 **Admin Panel** – Manage all campaigns with Django Admin

---

## 🛠 Tech Stack

| Component       | Tool                    |
|----------------|-------------------------|
| Backend         | Django (Python)         |
| Frontend        | HTML, Tailwind CSS      |
| Visualization   | Chart.js                |
| Database        | SQLite (default)        |

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/K2302/django_financial_pred.git
cd django_financial_pred
```

### 2. Create Virtual Environment (optional)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Linux/macOS
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Start Server

```bash
python manage.py runserver
```

Access at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Admin Access

- URL: `http://127.0.0.1:8000/admin/`
- Use superuser credentials you created

---

## 📂 Project Structure

```
marketing_roi_analyzer/
├── dashboard/
│   ├── templates/dashboard/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── marketing_roi_analyzer/
│   └── settings.py
├── static/
├── manage.py
```

---

## 💡 Future Enhancements

- ⬇ Export reports as PDF or CSV
- 📲 API integration with real ad platforms (Google Ads, Meta)
- 👥 Multi-user support with login-specific dashboards
- 🧠 AI-based ROI prediction (bonus idea!)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

> 💬 Got feedback or ideas? [Open an issue](https://github.com/K2302/django_financial_pred.git) or fork and contribute!
