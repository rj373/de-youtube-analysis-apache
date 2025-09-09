pip install apache-airflow google-api-python-client pandas s3fs

#This command installed everything needed for your entire project in a single step, ensuring all dependencies were met. 
#s3fs was the key library that allowed pandas to save your data directly to S3.

'''To install Apache Airflow, I followed a three-step process to ensure it was set up correctly within an isolated environment. I did not install the Apache HTTP Server.

System-Level Packages: I first used apt to install the necessary base Python tools on your Ubuntu system.

sudo apt install python3-pip python3.12-venv

Virtual Environment: I then created and activated a virtual environment. This was the most crucial step, as it isolated Airflow and its dependencies from your systems core Python packages.

python3 -m venv airflow_env

source airflow_env/bin/activate

Airflow and Dependencies: Finally, we used pip to install the apache-airflow package and all the other necessary libraries (such as google-api-python-client, pandas, and s3fs) directly into that isolated environment.

pip install apache-airflow google-api-python-client pandas s3fs'''
