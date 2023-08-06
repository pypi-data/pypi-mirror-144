## Docs will be written soon :)


## Developers:

### Testing version publishing commands:

1. Install dev dependencies
  ```python3 -m pip install --upgrade build```
2. Build the package 
  ```python3 -m build```
3. Publish to test repository
  ```python3 -m twine upload --repository testpypi dist/*```
