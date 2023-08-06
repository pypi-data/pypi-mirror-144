all: fmt lint types

fmt:
	isort pycodesearch
	black pycodesearch

lint:
	flake8 pycodesearch

types:
	mypy --strict pycodesearch
