# Website visit tracking - API and panel

### Description

This is an application which can be used for very simple tracking of
visits to a static website. It consists of the following parts (services):

- Static website template (`tracked_website`): contains a sample
  consent form and - under the hood - a script which sends POST requests
  to the server (upon tab/window closing) with the information
  about each website visit and interaction type. There are three
  kinds of interactions:

  - "open": website was access,
  - "view": website was scrolled to the bottom,
  - "read": website was scrolled to the bottom and was open
    for at least 30 seconds.

- API (`backend`): a Django REST application which accepts POST requests
  with the information about type of interaction and - if permitted by
  the user - location from which the site was accessed. It also provides
  an endpoint which generates aggregated data about the visits,
  i.e. grouped by date or location. The API also provides authentication
  so that only registered users can access the data. Registration is only
  possible from command line and Django admin panel (see "Deployment"
  section below).

- Panel (`frontend`): a simple React application which allows logging in
  and viewing aggregated data provided by the API in the form of a table.

- Database (`apidb`): a PostgreSQL server.

### Deployment

The application is shipped as a `docker-compose` configuration file
containing the three services (i.e. except `tracked_website`, which
is just a set of static files).

Before deployment, you have set the environment variables
as shown in the provided `.env.example` template file.
Also make sure that in the `backend/backend/settings.py` you remove
the `CORS_ALLOW_ALL_ORIGINS` variable and substitute with a list of
allowed hosts from environment variables.

After that, you can deploy the application with:

```
docker compose up --build
```

The database initially does not contain any users. In order to create
the first user, run:

```
docker compose exec -it backend python manage.py createsuperuser
```

and follow the instructions. After that, you can access the Django admin
panel at http://localhost:8000/admin/ and edit/create users.

A bash script for stopping the services and deleting containers and images
is also provided and can be used as

```
bash teardown.sh
```

The database persists in the `apidb` folder. If you want to delete it
and start fresh, run `sudo rm -r apidb`

#### © 2023 AG
