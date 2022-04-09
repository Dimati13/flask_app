FROM python
RUN pip install flask
ADD . /src
WORKDIR /src