FROM python:3

WORKDIR /usr/src/app

RUN mkdir cgi-bin && chmod 755 cgi-bin
COPY . ./cgi-bin/
COPY . .

RUN chmod 755 ./cgi-bin/bazzinator.py
EXPOSE 80
CMD ["python3", "-m", "http.server", "--bind", "0.0.0.0", "--cgi" ,"80"]