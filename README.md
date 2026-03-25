# 🎓 Student Manager (Django Web App)

A full-featured Django web application to manage student records with authentication, CRUD operations, and a clean Bootstrap UI.

---

## 🚀 Features

* 🔐 User Authentication (Login, Register, Logout)
* ➕ Add Students
* 📄 View Student List
* ✏️ Update Student Information
* ❌ Delete Students (with confirmation)
* 🎨 Responsive UI using Bootstrap
* 💬 Success & Error Messages
* 🔒 Protected Routes (Login Required)

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap 5
* **Database:** SQLite
* **Authentication:** Django Built-in Auth System

---

## 📸 Screenshots

### 🏠 Home Page

Shows a list of students with options to edit or delete.

*(Add your screenshot here if you want)*

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/django-student-manager.git
cd django-student-manager
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication Routes

| Feature  | URL                 |
| -------- | ------------------- |
| Login    | /accounts/login/    |
| Register | /accounts/register/ |
| Logout   | /accounts/logout/   |

---

## 📂 Project Structure

```
django-student-manager/
│
├── students/        # Student CRUD app
├── accounts/        # Authentication app
├── templates/       # HTML templates
├── manage.py
└── db.sqlite3
```

---

## 🌐 Deployment

This project can be deployed using:

* Render
* PythonAnywhere
* Railway

---

## 👨‍💻 Author

**Harris Pervez**

* GitHub: https://github.com/Harris-Pervez
💼 LinkedIn: https://www.linkedin.com/in/harris-pervez
📧 Email: harrykhan0910@gmail.com
---

## 💡 Future Improvements

* 🔍 Search functionality
* 📊 Dashboard with analytics
* 📁 Profile management
* 🌍 REST API (Django REST Framework)

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

---
