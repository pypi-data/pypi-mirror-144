# created with `cookiecutter https://github.com/ondraz/cookiecutter-pypackage`

install:
	poetry update
	poetry install

install-dev: install
	poetry install -E dev -E test -E doc
	poetry run ipython kernel install --user --name={{ cookiecutter.project_slug }}
	poetry run pre-commit install

check:
	tox

clean:
	rm -rf build site .eggs book/_build dist .tox {{ cookiecutter.project_slug }}/__pycache__
	rm -rf {{ cookiecutter.project_slug }}/plotly_theme/__pycache__ tests/__pycache__
