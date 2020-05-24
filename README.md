# Junari Technical Interview App

Welcome to Junari CRM Lite! This is a simple web application used in Junari
Technical interviews. It implements a basic CRM system that allows users to
edit contacts.

![Junari CRM Lite Screenshots](screenshots.png)

This application consists of a [Flask](https://github.com/pallets/flask) web
server with a JSON API, and a JavaScript front-end that uses the
[Odoo Web Library (OWL)](https://github.com/odoo/owl)
framework - a modern React/Vue-like framework.

## Requirements

* Python 3.7 or above
* A modern web browser (Chrome or Firefox recommended).
  The app uses JS modules and async functions.

## Set up

First, check-out the repository onto your local machine

```bash
git clone git@github.com:junariltd/interview_app.git
cd interview_app
```

Now you can run the provided `init` script, which creates a Virtual Environment,
installs dependencies, and initialises the SQLite database.

```
# Mac/Linux
./init.sh

# Windows
init.bat
```

## Running for development

To start the development server, use the `run` script:

```
# Mac/Linux
./run.sh

# Windows
run.bat
```

Once started, the app can be accessed at http://localhost:5000/

The default user is **user1**, password: **letmein**

## Front-end code

The JavaScript front-end uses modern JavaScript and JS modules in the browser
and **does not require a build step**. The front-end code can be found in the
`jcrm_lite/static/js/` directory.

## Useful References

* [Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial)
* [Odoo Web Library Docs](https://github.com/odoo/owl/blob/master/doc/readme.md)
* [QWeb Template Language Docs](https://github.com/odoo/owl/blob/master/doc/reference/qweb_templating_language.md)
* [Odoo Web Library Playground](https://odoo.github.io/owl/playground/)
