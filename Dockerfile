FROM python:3
WORKDIR src
RUN pip install --upgrade pip
RUN pip install lxml numpy Cython
RUN pip install dragnet flask
COPY server.py server.py
EXPOSE 5000
ENTRYPOINT ["python", "server.py"]
CMD []
