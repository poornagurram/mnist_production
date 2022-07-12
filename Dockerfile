FROM python:3.8
WORKDIR /code
ENV FLASK_APP=code/app.py
ENV FLASK_RUN_HOST=0.0.0.0
#rf knn lr dt are available as models
ENV MODEL="rf"
COPY . .
RUN pip install --upgrade pip
RUN pip install -r code/requirements.txt
EXPOSE 5000
CMD ["flask", "run"]

