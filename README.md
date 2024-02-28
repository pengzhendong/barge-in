## Barge-in

```bash
$ uvicorn src.main:app --reload
```

### Docker

```bash
$ docker build -t barge-in .
$ docker run --restart=always -p 8000:8000 --name barge-in barge-in
```
