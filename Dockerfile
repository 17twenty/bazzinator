FROM python:3

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir cgi-bin && chmod 755 cgi-bin
COPY . ./cgi-bin/
COPY . .

RUN chmod 755 ./cgi-bin/bazzinator.py
EXPOSE 80
# CMD [ "python", "./bazzinator.py" ]
CMD ["python3", "-m", "http.server", "--bind", "0.0.0.0", "--cgi" ,"80"]