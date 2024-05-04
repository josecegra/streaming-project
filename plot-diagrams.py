import os

from diagrams import Diagram, Cluster
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import MongoDB
from diagrams.onprem.container import Docker
from diagrams.programming.framework import FastAPI
from diagrams.generic.blank import Blank
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python

OUTPUT_DIR = "/app/imgs/"

def data_architecture(
    filename = "data_architecture", 
    diagram_name = "Data Architecture",
    ):

    filename = os.path.join(OUTPUT_DIR,filename)

    with Diagram(
        diagram_name, 
        show=False, 
        direction="TB", 
        filename=filename, 
        outformat="png",
        ):

        with Cluster("Source 1"):
            source_1 = Storage("Source 1")
        with Cluster("Source 2"):
            source_2 = Storage("Source 2")
        with Cluster("Kafka"):
            kafka = Kafka("Kafka")
        with Cluster("Data Warehouse"):
            mongo = MongoDB("MongoDB")
        with Cluster("Consumer 1"):
            consumer_1 = PostgreSQL("PostgreSQL 1")
        with Cluster("Consumer 2"):
            consumer_2 = PostgreSQL("PostgreSQL 2")

        source_1 >> kafka >> mongo
        source_2 >> kafka >> mongo
        mongo >> kafka
        kafka >> consumer_1
        kafka >> consumer_2


def docker_images(
    filename = "docker_images", 
    diagram_name = "Docker Images",
    ):

    filename = os.path.join(OUTPUT_DIR,filename)

    with Diagram(
        diagram_name, 
        show=False, 
        direction="TB", 
        filename=filename, 
        outformat="png",
        ):

        with Cluster("Kafka"):
            kafka = Docker("kafka:latest")
            zookeeper = Docker("zookeeper:latest")

        with Cluster("Source"):
            source = Docker("data-source")
            data_producer = Docker("data-producer")

        with Cluster("Data Warehouse"):
            mongo = Docker("mongo:latest")
            data_consumer = Docker("data-consumer")
            postgres_producer = Docker("posgres-producer")
            mongo_api = Docker("mongo-api")

        with Cluster("Consumer"):
            postgres = Docker("postgres:latest")
            postgres_api = Docker("postgres-api")
            postgres_consumer = Docker("postgres-consumer")


        data_producer >> kafka >> mongo
        mongo >> kafka
        kafka >> postgres_consumer

     
def source_services(
    filename = "source_services", 
    diagram_name = "Source Services",
    ):

    filename = os.path.join(OUTPUT_DIR,filename)

    with Diagram(
        diagram_name, 
        show=False, 
        direction="LR", 
        filename=filename, 
        outformat="png",
        ):

        with Cluster("Source Container"):
            logs = Storage("Logs")

        with Cluster("Producer"):
            producer = Python()

        with Cluster("Kafka"):
            kafka = Kafka()

        logs >> producer >> kafka

def data_warehouse_services(
    filename = "data_warehouse_services", 
    diagram_name = "Data Warehouse Services",
    ):

    filename = os.path.join(OUTPUT_DIR,filename)

    with Diagram(
        diagram_name, 
        show=False, 
        direction="BT", 
        filename=filename, 
        outformat="png",
        ):

        with Cluster("MongoDB"):
            db = MongoDB()

        with Cluster("FastAPI"):
            api = FastAPI()

        with Cluster(" "):
            producer = Python("Producer")
            consumer = Python("Consumer")

        with Cluster("Kafka"):
            kafka = Kafka()

        db >> api >> producer
        api >> db
        producer >> kafka >> consumer
        consumer >> api

def consumer_services(
    filename = "consumer_services", 
    diagram_name = "Consumer Services",
    ):

    filename = os.path.join(OUTPUT_DIR,filename)

    with Diagram(
        diagram_name, 
        show=False, 
        direction="LR", 
        filename=filename, 
        outformat="png",
        ):

        with Cluster("PostgreSQL"):
            db = PostgreSQL("")

        with Cluster("FastAPI"):
            api = FastAPI("")

        with Cluster("Consumer"):
            consumer = Python("")

        with Cluster("Kafka"):
            kafka = Kafka()

        kafka >> consumer >> api >> db
        api << db


if __name__ == "__main__":
    data_architecture()
    docker_images()
    source_services()
    data_warehouse_services()
    consumer_services()

