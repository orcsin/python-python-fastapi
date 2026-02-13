# fastapi

FastAPI baseline application.

## Local development

```bash
pip install -e ".[test]"
pytest
```

## Docker

```bash
docker build -t myimage .
docker run --rm -it -p 8080:8080 myimage
```
