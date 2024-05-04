# streaming-project

Kafka
mongodb and postgresql for data storage
FastAPI endpoints to interact with storage

## Data Architecture
<img src="imgs/data_architecture.png" alt="Data Architecture" width="500">

## Source Services
<img src="imgs/source_services.png" alt="Source Services" width="500">

## Data Warehouse Services
<img src="imgs/data_warehouse_services.png" alt="Data Warehouse Services" width="500">

## Consumer Services
<img src="imgs/consumer_services.png" alt="Consumer Services" width="500">

## Docker Images
<img src="imgs/docker_images.png" alt="Docker Images" width="500">


## Repositories

* [Core services: Kafka, Data Warehouse](https://github.com/josecegra/core-services-streaming)
* [Data Source service](https://github.com/josecegra/data-source-streaming)
* [Data Consumer service](https://github.com/josecegra/data-warehouse-streaming)


## Creating the diagrams

```shell
docker compose up -d --build
```
