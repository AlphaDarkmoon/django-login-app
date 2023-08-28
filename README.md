<h1 align="left">Django Login System app</h1>

###
<div align="center">
  <img height="500" src="https://i.ibb.co/YfVY7qB/django-app.png"  />
</div>

###

<p align="left">An abstract base user model that lets users add a login app to already-built Django projects.</p>
contains a simple login and registration UI; make changes as per your needs.

###

<p align="left">Follow the steps below and install the app in your projects.</p>


## Table of Contents

- Installation steps
- Coded with
- Contributions

<h2 align="left">Installation steps</h2>

###

<h4 align="left">Clone the project on your computer</h4>

1. Clone the repository: `git clone https://github.com/yourusername/yourproject.git`
4. go to `settings.py` of your django project
2. Register the app `users`
6. add the following in `settings.py`

```
#settings.py

AUTH_USER_MODEL = "users.CustomUser"

LOGIN_REDIRECT_URL = "testmain_app:home"
LOGOUT_REDIRECT_URL = "testmain_app:home"
```
- replace `testmain_app` with your main app that will serve your home page
and replace `home` with your `index.html` views refrence.

```
#views.py

def home(request):
    # Render the 'index.html' template
    return render(request, 'index.html')
```

7. add app name in main app's `urls.py`
```
#urls.py

app_name = 'unique app name'
```

8. Make migrations in your project
```
python3 manage.py makemigrations
```

9. Migrate project
```
python3 manage.py migrate
```

10. Create superuser
```
python3 manage.py createsuperuser
```

11. Run the project
```
python3 manage.py runserver
```

that's all.
###

<h2 align="left">Coded with</h2>

###

<div align="left">
  <img src="https://skillicons.dev/icons?i=django" height="40" alt="django logo"  />
  <img width="12" />
  <img src="https://cdn.simpleicons.org/python/3776AB" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=html" height="40" alt="html5 logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=css" height="40" alt="css3 logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=js" height="40" alt="javascript logo"  />
</div>

###
---


<h2 align="left">Please Put a comment or issue for which you are going to contribute.</h2>

###

<h2 align="left">Contribution</h2>

###

<h4 align="left">Open a pull request:</h4>

###

- Go to the Pull Requests section of this repository.
- Click on the "New Pull Request" button.
- Select the base branch (usually main) and your feature branch.
- Provide a descriptive title and details about your changes.
- Click "Create Pull Request".

###

<h4 align="left">Code Style:</h4>

###

<p align="left">Please follow our coding conventions and style guidelines. For example:</p>

###

- Use consistent indentation (spaces or tabs).
- Write clear and descriptive variable and function names.
- Add comments to explain complex parts of the code.

###


###
