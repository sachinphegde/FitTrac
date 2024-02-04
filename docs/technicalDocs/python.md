# Python setup

1. Install the latest python
2. install latest pip version 


To update all python packages at once -->

``` python
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```

To get the requirements.txt file

```
pip freeze > requirements.txt
```

To install and use the requirements.txt

```
pip install -r requirements.txt
```

## Documentation setup
mkdocs is used to create the documentation of the project and also to host it in GitHub pages

1. pip install mkdocs
