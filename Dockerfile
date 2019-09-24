

FROM continuumio/anaconda3

COPY ./project /root

RUN pip install --upgrade pip \
    && pip install -r /root/requirements.txt

ENTRYPOINT ["python", "/root/startApp.py"]

