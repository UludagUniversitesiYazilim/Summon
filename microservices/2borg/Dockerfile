FROM python:3
EXPOSE 9795
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r req.txt
CMD ["python3", "main.py"]
