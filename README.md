# Theme API - Django REST Framework Project

Welcome to **Theme API**, a backend project built with **Django REST Framework** that manages categories, themes, and stories. This API is designed to provide data for apps, websites, or other services that need organized theme and story content.

---

## 🌟 Features

- **Categories**: Organize themes and stories into groups like "Special" or "Hot".  
- **Themes**: Each theme has properties like name, colors, background images, premium status, and download counts.  
- **Stories**: Visual content (images) linked to categories.  
- **Authentication**: Secure access using **Token Authentication**. Only registered users can access certain data.  
- **Database**: Stores all information in **PostgreSQL** for reliability and scalability.  

---

## 🖥️ How It Works (Layman’s Terms)

1. Think of this project as a **digital library of themes and stories**.  
2. Each category is like a shelf in the library (`Special`, `Hot`).  
3. Themes are like books on the shelf – they have details such as color, images, and whether they are premium.  
4. Stories are like posters or visuals linked to categories.  
5. The API allows apps or websites to **fetch this data**, like asking the library for all books in a certain shelf.  

---

## ⚙️ Tech Stack

- **Backend**: Python, Django, Django REST Framework  
- **Database**: PostgreSQL  
- **Authentication**: Token Authentication (for secure API access)  
- **Deployment**: Can be deployed on any server supporting Python/Django  

---

## 🧰 Installation (Developer Guide)

1. Clone the repository:

```bash
git clone https://github.com/tayyabsaeed11/theme_api.git
cd theme_api

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

DEBUG=True
SECRET_KEY=<your-secret-key>
DB_NAME=db_theme
DB_USER=dev_theme
DB_PASSWORD=dev@123
DB_HOST=localhost
DB_PORT=5432

python manage.py migrate
python manage.py runserver

/api/categories/    → List all categories
/api/themes/        → List all themes
/api/stories/       → List all stories

http://127.0.0.1:8000/admin/
