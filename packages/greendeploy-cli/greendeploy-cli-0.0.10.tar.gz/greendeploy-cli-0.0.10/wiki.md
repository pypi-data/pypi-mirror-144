## How to update PyPi

```
python setup.py sdist bdist_wheel
twine check dist/*
rm dist/package-name-slug-<previous-tag>*
rm dist/snake_package_name-<previous-tag>*
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*

twine upload --skip-existing dist/*
```

```
cd {{ cookiecutter.full_path_to_your_project }}{{ cookiecutter.project_slug }}

{{ cookiecutter.full_path_to_pyenv }}/versions/3.8.12/bin/python3.8 -m venv {{ cookiecutter.full_path_to_venv }}{{ cookiecutter.project_slug }}-py3812

source {{ cookiecutter.full_path_to_venv }}{{ cookiecutter.project_slug }}-py3812/bin/activate

python -m pip install --upgrade "{{ cookiecutter.pip_version }}"

pip install pip-tools "{{ cookiecutter.pip_tools_version }}"

git init .

git add .
git commit -m '🎉 Initial commit'
git tag -a v0.0.0 -m '🔖 First tag v0.0.0'

pip-compile

pip-sync

pip install -e .
```

Now run

```
python -m {{ cookiecutter.project_slug }}
```