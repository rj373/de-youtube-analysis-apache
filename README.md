# YouTube Comments ETL Pipeline with Apache Airflow

## Project Description

This project demonstrates a robust, end-to-end data pipeline to extract, transform, and load (ETL) comments from a YouTube video. The pipeline is orchestrated using **Apache Airflow** and runs on an **Ubuntu** server hosted on **AWS EC2**. The data is fetched from the **YouTube Data API v3**, processed with **Pandas**, and loaded into an **S3 bucket** for storage.

The project is designed to be a clear, practical example of a modern data engineering workflow.

## Prerequisites

- An **AWS Account** with an active billing setup.
- A **Google Cloud Account** with a valid API key for the YouTube Data API.
- An **SSH Client** (e.g., Terminal on Mac/Linux, or PuTTY/WSL on Windows).

## Project Setup

### Step 1: Set Up AWS & Google Cloud

1.  **Get a Google API Key**:
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project.
    - Navigate to the **APIs & Services Library**, search for `YouTube Data API v3`, and click **Enable**.
    - Go to **Credentials** and create a new **API Key**. Save this key.

2.  **Launch an EC2 Instance**:
    - In the AWS Management Console, launch a new EC2 instance.
    - Choose an Ubuntu Server AMI.
    - For the instance type, select a machine with at least **4 GB of RAM** (e.g., `t3.medium` or `c7i-flex.large`) to ensure Airflow runs smoothly.
    - Configure a security group to allow inbound traffic on **port 22 (SSH)** and **port 8080 (Airflow UI)** from your IP address.
    - Launch the instance and download the private key file (`.pem`).

3.  **Create an IAM Role**:
    - In the IAM Console, create a new **IAM Role** with **EC2** as the trusted entity.
    - Attach the managed policy **`AmazonS3FullAccess`** to this role.
    - Name the role `ec2-s3-airflow-role`.

4.  **Attach the IAM Role to EC2**:
    - Go back to the EC2 Dashboard, select your instance, and go to **Actions > Security > Modify IAM role**.
    - Attach the `ec2-s3-airflow-role`.

### Step 2: Prepare the EC2 Instance

1.  **Connect via SSH**:
    ```bash
    ssh -i /path/to/your-key.pem ubuntu@<your-instance-ip>
    ```
2.  **Install Python Tools**:
    - Once connected, install `pip` and the `venv` package.
    ```bash
    sudo apt update
    sudo apt install python3-pip python3.12-venv
    ```
3.  **Create Project Directory and Virtual Environment**:
    ```bash
    mkdir ~/airflow
    cd ~/airflow
    python3 -m venv airflow_env
    ```
4.  **Activate the Environment**:
    ```bash
    source airflow_env/bin/activate
    ```
    Your terminal prompt should now show `(airflow_env)`.
5.  **Install All Libraries**:
    ```bash
    pip install apache-airflow google-api-python-client pandas s3fs
    ```
6.  **Initialize Airflow**:
    ```bash
    export AIRFLOW_HOME=~/airflow
    airflow db migrate
    ```

### Step 3: Create Project Files

1.  **Create DAGs Folder**:
    ```bash
    mkdir ~/airflow/dags
    ```
2.  **Create `youtube_etl.py`**:
    - In the `~/airflow/dags` folder, create a new file named `youtube_etl.py` and paste the provided Python code into it.
    - **Remember to replace `"YOUR_API_KEY"`** with your actual Google API key.
3.  **Create `youtube_dag.py`**:
    - In the same `~/airflow/dags` folder, create a new file named `youtube_dag.py` and paste the provided DAG code.

### Step 4: Run and Trigger the DAG

1.  **Start Airflow**:
    - From your `~/airflow` directory, run the `airflow standalone` command.
    ```bash
    airflow standalone
    ```
2.  **Access the UI**:
    - In your web browser, navigate to `http://<your-instance-ip>:8080`.
3.  **Trigger the DAG**:
    - On the Airflow UI, find your `youtube_dag`. Turn it on, and then trigger it manually to start the ETL process.

## Project Structure
<img width="1211" height="542" alt="image" src="https://github.com/user-attachments/assets/2a2c5939-1b81-4b03-a447-52ac0b072ea2" />
