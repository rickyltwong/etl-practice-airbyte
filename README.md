# Data Engineering Project

This is an end-to-end  data engineering project involving the use of FastAPI, Airbyte, MinIO, and other tools to work with data.

Data currently used: fighting powers of characters in Dragon Ball (in .csv from Kaggle)

## Tools:

- FastAPI: A modern, fast, web framework for building APIs with Python. In this project, a FastAPI server will be set up in a Linux environment to serve data related to the chosen hobby.
- Airbyte: An open-source data integration platform that helps to move and consolidate data from different sources to destinations. In this project, Airbyte will be deployed onto the Linux environment and connected to the FastAPI server using a REST API connector.
- MinIO: A high-performance, distributed object storage server that is compatible with Amazon S3. In this project, Minio will be used as an S3 destination for storing the data. 
- (To be implemented) Octavia CLI: Managing Airbyte resources and destination with YAML config files.
- (To be implemented) Dagster: A data orchestration framework for building, testing, and deploying data pipelines. In this project, Dagster will be used to connect Airbyte to the data pipelines, set up a schedule for data syncing, and orchestrate all the components.
- (To be implemented) DuckDB: An embeddable SQL database management system. In this project, DuckDB will be installed on the Linux environment for storing and querying the data.
- (To be implemented) dbt (data build tool): A tool for transforming data stored in data warehouses by writing, testing, and maintaining SQL-based data models. In this project, a dbt model will be set up to build a data model for the hobby-related data.
- (To be implemented) DBeaver: A multi-platform database tool that supports various database management systems. In this project, DBeaver will be used to connect to the DuckDB data model.
