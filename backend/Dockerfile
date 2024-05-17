#Python resmi imajini cektik. Python ve pip yüklü
FROM python:3.9
#Container ici app dizini
WORKDIR /app
#Requirements.txt dosyasindaki bagimliliklari yüklemek icin.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
