# Sankar K — Django Portfolio

## Project Structure
```
portfolio_project/
├── manage.py
├── requirements.txt
├── render.yaml                       ← one-click Render.com deploy
├── .gitignore
├── README.md
├── portfolio_project/                ← Django config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio_app/                    ← Portfolio app
    ├── models.py
    ├── admin.py
    ├── views.py
    ├── urls.py
    ├── fixtures/
    │   └── initial_data.json         ← pre-filled with your data
    ├── templates/portfolio_app/
    │   └── index.html                ← Django template
    └── static/portfolio_app/
        ├── css/style.css             ← all CSS
        ├── js/main.js                ← all JS
        └── images/Sankar.jpg         ← your photo
```

---

## Quick Start (Local)

```bash
# 1. Install
pip install -r requirements.txt

# 2. Migrate
python manage.py makemigrations
python manage.py migrate

# 3. Load your data
python manage.py loaddata portfolio_app/fixtures/initial_data.json

# 4. Create admin login
python manage.py createsuperuser

# 5. Collect static
python manage.py collectstatic

# 6. Run
python manage.py runserver
```

- Portfolio → http://127.0.0.1:8000/
- Admin    → http://127.0.0.1:8000/admin/

---

## Admin — What You Can Edit

| Section              | Editable From Admin                          |
|----------------------|----------------------------------------------|
| Profile              | Name, bio, email, phone, photo, resume, stats, links |
| About Highlights     | → bullet points (linked to Profile)          |
| Languages            | Language + level (linked to Profile)         |
| Certifications       | Icon, name, issuer (linked to Profile)       |
| Skill Categories     | Group names + order                          |
| Skills               | Individual skill tags + order                |
| Experience           | Each role + bullet points                    |
| Projects             | Cards, GitHub links, tags                    |
| Education            | Degree, school, CGPA                         |
| Achievements         | Icon, title, description, date               |

### Upload Photo & Resume:
Admin → Profile → Files section → Choose File → Save

---

## Deploy Free — Render.com

```bash
# Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/portfolio_project.git
git push -u origin main

# Go to render.com → New Web Service → Connect GitHub → Deploy
```
Live at: `https://sankar-portfolio.onrender.com`

## Deploy — Azure Free Tier

```bash
az login
az group create --name sankar-rg --location eastasia
az appservice plan create --name sankar-plan --resource-group sankar-rg --sku F1 --is-linux
az webapp create --resource-group sankar-rg --plan sankar-plan --name sankar-portfolio --runtime "PYTHON:3.11"
az webapp config set --resource-group sankar-rg --name sankar-portfolio --startup-file "gunicorn portfolio_project.wsgi:application"
az webapp config appsettings set --resource-group sankar-rg --name sankar-portfolio --settings SECRET_KEY="your-key" DEBUG="False" ALLOWED_HOSTS=".azurewebsites.net"
zip -r portfolio.zip . -x "*.pyc" -x "__pycache__/*"
az webapp deployment source config-zip --resource-group sankar-rg --name sankar-portfolio --src portfolio.zip
```
Live at: `https://sankar-portfolio.azurewebsites.net`
