FROM python:3.10-slim

WORKDIR /app

COPY ./ /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn transformers torch torchvision

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "7860"]