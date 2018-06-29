clean:
	@ find . -name '*.py[co]' -delete
	@ find . -name '__pycache__' -delete
	@ rm -rf *.egg-info dist build .tox

publish:
	@ python setup.py sdist bdist_wheel
	@ pip install twine
	@ twine upload dist/*
	@ pip uninstall twine -y
	@ rm -rf ./dist

test_publish:
	@ python setup.py sdist bdist_wheel
	@ pip install twine
	@ twine upload --repository=pypitest dist/*
	@ pip uninstall twine -y
	@ rm -rf ./dist
