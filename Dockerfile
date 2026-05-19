FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

"""
                                 A Small Best-Practice Pro-Tip

While your current boilerplate works perfectly, there is one trick developers use to make Docker builds
10x faster when updating code.Right now, if you change even one line of text in your HTML, Docker has to
re-install all your Python libraries from scratch. By copying the requirements.txt file before copying the
rest of your code, Docker can cache your libraries:
    
"""
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "app.py"]