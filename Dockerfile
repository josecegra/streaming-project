FROM python:3.9
WORKDIR /app
RUN pip install diagrams
RUN apt-get update && apt-get install -y graphviz
COPY ./ /app
CMD [ "python","plot-diagrams.py" ]