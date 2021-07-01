# Implement the search feature using Django, Elasticsearch, and Vue.js 

This is an initial proof of concept app of how to implement a search feature using Elasticsearch with Django and Vue.js.

Content:
1. [Overview](#1-overview)
2. [Set up the working environment](#2-set-up-the-working-environment)
3. [Set up Elasticsearch & Kibana servers using Docker](#3-set-up-elasticsearch--kibana-servers-using-docker)
4. [Run Django server](#4-run-django-server)


## 1. Overview

In this web application users can add new articles by providing a title and the content of the 
article, and some tags if they want. They can also search for articles from the “Articles list”.

## 2. Set up the working environment

2.1 Clone the project repository in your machine and change the current working directory to that of the cloned project as follows:

```commandline
git clone https://github.com/fatse/django-elasticsearch-vuejs.git
cd django-elasticsearch-vuejs
```

2.2 Install dependencies into an isolated environment:

```commandline
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## 3. Set up Elasticsearch & Kibana servers using Docker

From your terminal run this command:

```commandline
docker-compose up -d 
```

After running the command above the output should look like below:

```commandline
Starting elasticsearch ... done
Starting kibana        ... done
```

> Note: The command `docker-compose up -d` should be run from the root directory because that's where 
> docker-compose script lives.

## 4. Run Django server

From your terminal run this command to start a local web server: 

```commandline
python manage.py runserver
```

And in your terminal you will see an output similar to the one below:

```commandline
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 01, 2021 - 21:06:12
Django version 3.2.3, using settings 'django_elasticsearch.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

You can copy the url `http://127.0.0.1:8000/` from the output and paste it directly to your browser's search bar.

Alternatively, you can click at the link `http://127.0.0.1:8000/` from the output while pressing the `Command ⌘` key, and it
will open a new browser tab for the web application.

![django-elasticsearch-vuejs](img/demo.gif "django-elasticsearch-vuejs")


