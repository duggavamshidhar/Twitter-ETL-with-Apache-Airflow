# Twitter ETL with Apache Airflow

## Overview
This repository encompasses a comprehensive ETL (Extract, Transform, Load) pipeline for harvesting, refining, and managing Twitter data using Tweepy and Apache Airflow. The primary objective of this project is to seamlessly acquire, process, and store relevant Twitter data, with a focus on modularity, extensibility, and ease of integration.

## Project Structure

### `twitter_etl.py`
The core of the ETL process resides in `twitter_etl.py`. This script orchestrates the interaction with the Twitter API, retrieves tweets, and refines the data. Importantly, it does not dictate a specific storage format, offering flexibility for users to choose the most suitable method based on their requirements.

### `twitter_dag.py`
The configuration of the Apache Airflow Directed Acyclic Graph (DAG) is defined in `twitter_dag.py`. This DAG schedules the ETL process to execute daily and leverages the `PythonOperator` to call the functions defined in `twitter_etl.py`. It serves as the orchestrator of the entire workflow.

### `required_commands.sh`
To streamline the environment setup process, `required_commands.sh` encapsulates essential commands for updating the system, installing necessary Python dependencies (including Apache Airflow, pandas, s3fs, and tweepy), and ensuring the environment is conducive to successful execution.

## Prerequisites
Prior to launching the Twitter ETL process, please ensure you possess the following prerequisites:

- **Twitter Developer API Keys:** Obtain the necessary access key, access secret key, consumer key, and consumer secret key from [Twitter Developer Portal](https://developer.twitter.com/en/docs/twitter-api).

## Installation Steps
Follow these meticulous steps to configure and execute the Twitter ETL process:

1. Execute the commands within `required_commands.sh` to install essential dependencies.

    ```bash
    sudo sh required_commands.sh
    ```

2. Replace placeholder values (`"YOUR_ACCESS_KEY"`, `"YOUR_ACCESS_SECRET_KEY"`, `"YOUR_CONSUMER_KEY"`, `"YOUR_CONSUMER_SECRET_KEY"`) in `twitter_etl.py` with your actual Twitter API keys.

3. Customize any other configuration parameters within `twitter_dag.py` according to your specific preferences and requirements.

## Usage
Commence the Twitter ETL process by triggering the Airflow DAG:

```bash
airflow dags trigger twitter_dag
```

This initiation will commence the ETL process, fetching tweets from the designated Twitter account (e.g., `@elonmusk`), refining the data, and presenting the refined data for further processing and storage in a format of your choosing.

## Additional Notes
Ensure to meticulously review and comply with Twitter API usage policies and guidelines during the utilization of this script.

Feel empowered to adapt and customize the scripts to align with your distinct requirements or integrate supplementary functionalities as necessary. The modularity of the design allows for seamless extensibility and adaptability to diverse use cases.