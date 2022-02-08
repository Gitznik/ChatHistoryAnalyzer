# How to develop
Install the dependencies with `poetry install`

Then start a dev server with `poetry run uvcorn backend.main:app --reload`
This will start a dev server on `http://localhost:8000` which you can use.


# Deployment
We plan to deploy the backend using [Deta](https://www.deta.sh/?ref=fastapi) following [this documentation](https://fastapi.tiangolo.com/deployment/deta/). This is an open TODO.