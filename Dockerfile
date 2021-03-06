FROM python:3.8.3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install pymongo[srv]
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 