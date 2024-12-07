pip install pytest pytest-asyncio build setuptools twine
pytest -vv
python -m build
rm -r ezneis.egg-info
rm dist/ezneis-*.tar.gz
twine upload dist/ezneis-*.whl
