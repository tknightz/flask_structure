# My simple flask application structure

Overview app structure

```
.
├── app.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 191ccc807fb9_.py
├── project
│   ├── auth.py
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py
│   ├── routes
│   │   ├── admin
│   │   │   ├── templates
│   │   │   │   ├── login.html
│   │   │   │   └── register.html
│   │   │   └── views.py
│   │   └── public
│   │       ├── templates
│   │       │   └── index.html
│   │       └── views.py
│   ├── site.db
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── img
│   │   └── js
│   └── templates
│       ├── base.html
│       └── index.html
├── README.md
└── requirements.txt

13 directories, 21 files

```


### Commands

- flask run
- flask db init
- flask db migrate
- flask db upgrade
