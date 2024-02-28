FROM python:3

COPY requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ADD . .

ENTRYPOINT ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]
