# How to develop
Install the dependencies with `poetry install`

We also suggest running `pre-commit install` so things like auto-formatting happen when you commit. This can save you from facing failing CI pipelines.

Then start a dev server with `poetry run uvcorn backend.main:app --reload`
This will start a dev server on `http://localhost:8000` which you can use.


# Deployment
We plan to deploy the backend using [Deta](https://www.deta.sh/?ref=fastapi) following [this documentation](https://fastapi.tiangolo.com/deployment/deta/). This is an open TODO.
