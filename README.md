## Lab: 33 - Authentication & Production Server

**Feature Tasks and Requirements**

**Features - Django**

- [x] Add JWT Authentication to your API.
- [x] Install needed libraries in project configuration and/or site settings.
- [x] Keep any pre-existing authentication so DRF Browsable API still usable.
- [x] Install needed libraries in project configuration and/or site settings

**Features - Docker**

- [x] Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.

E.g. as a VS Code snippet, or a gist.

- [x] Switch to using Gunicorn instead of Django’s built in development server.

mind the number of workers to avoid sluggishness

- [x] Warning You will run into styling issues when you switch over to Gunicorn.

On Django side you’ll need to properly handle static files using Whitenoise

**Storage Options**

- [x]Your choice of SQLite or PostgreSQL
- [x]Adjust docker-compose.yml so that data is persisted in a volume outside of container.
- [x]These steps are different depending on whether SQLite or PostgreSQL is being used.

**Implementation Notes**

**User Acceptance Tests**

- [x] Include steps to manually test using httpie or Postman.
- [x] No unit tests required.

**Configuration**

- [x] Create new drf-auth repository.
- [x] Use poetry to initialize drf-auth project.
- [x] $ cd drf-auth
- [x] $ poetry init -n
- [x] Use the folder drf-auth as the root of your project’s git repository.

**Developer**

Faisal Kushha

**Pull Request**

https://github.com/Faisal-Kushha/drf-auth/pull/1
