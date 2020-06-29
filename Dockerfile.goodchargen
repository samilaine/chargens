FROM python:3.8

COPY goodchargen.py /

RUN sed -i 's/localhost/0.0.0.0/' /goodchargen.py

ENTRYPOINT [ "python", "/goodchargen.py" ] 
