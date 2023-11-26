# AlejandraLLI/Cloud_Engineering_Project 

## Overview

The Cloud Engineering Final Project focuses on predicting airline prices using a pipeline. The project utilizes various tools and technologies such as Flask, Streamlit, Docker, pandas, scikit-learn, xgboost, AWS S3, and AWS EC2. The pipeline consists of steps like data ingestion, data cleaning, feature generation, model training, and evaluation. The Flask application serves a trained model as a RESTful API, while Streamlit provides the app interface. The project also includes configuration files for logging and web application settings, as well as Dockerfiles for building containers. The pipeline can be run locally or in AWS, with artifacts stored in an S3 bucket. Overall, the project aims to provide a solution for predicting airline prices using a well-defined pipeline and user-friendly app interface.

## Repo Structure

```
.
├── .github
│   └── workflows
│       └── main.yaml
├── .gitignore
├── 00_Administrative
│   └── Meeting_Minutes.md
├── 00_Archive
│   ├── Generate_Raw_Data.ipynb
│   └── emptyfile
├── 01_Literature
├── 02_Data
│   ├── clean_data.csv
│   ├── clean_data.zip
│   ├── emptyfile
│   └── source_data.zip
├── 03_Img
│   └── ArchitectureDiagram.png
├── 04_Implementation
│   ├── app
│   │   ├── README.md
│   │   ├── config
│   │   │   ├── logging
│   │   │   │   └── webapp_log.yaml
│   │   │   └── webapp.yaml
│   │   ├── dockerfiles
│   │   │   └── Dockerfile
│   │   ├── plane.jpg
│   │   ├── requirements.txt
│   │   └── src
│   │       ├── aggregate_data.py
│   │       ├── predict_api.py
│   │       ├── webapp.py
│   │       └── test.py
│   └── pipeline
│       ├── README.md
│       ├── config
│       │   ├── default-config.yaml
│       │   └── logging
│       │       └── local.conf
│       ├── dockerfiles
│       │   ├── Dockerfile.pipeline_main
│       │   └── Dockerfile.tests
│       ├── notebooks
│       │   ├── Clean_Data.ipynb
│       │   ├── EDA.ipynb
│       │   └── Modeling.ipynb
│       ├── pipeline.py
│       ├── requirements_main.txt
│       ├── requirements_tests.txt
│       └── src
│           ├── __init__.py
│           ├── aws_utils.py
│           ├── clean_data.py
│           ├── generate_features.py
│           ├── raw_data.py
│           └── train_model.py
│               ├── tests
│               │   ├── __init__.py
│               │   ├── test_clean_data.py
│               │   ├── test_generate_features.py
│               │   └── test_train_model.py
└── 05_Deliverables
    ├── AppDemo.mp4
    └── Final Presentation.pptx

```

## Getting started

To clone the repository and install dependencies for the Cloud_Engineering_Project, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to clone the repository. For example, if you want to clone it to your desktop, run the following command:
   ```
   cd Desktop
   ```

3. Clone the repository by running the following command:
   ```
   git clone https://github.com/AlejandraLLI/Cloud_Engineering_Project.git
   ```

4. Once the cloning process is complete, navigate into the cloned repository by running the following command:
   ```
   cd Cloud_Engineering_Project
   ```

5. Install the dependencies by running the following command:
   ```
   pip install -r 04_Implementation/app/requirements.txt
   ```

6. NOTE: The Github repo is too long to give more detailed instructions. Parsing of code is not implemented yet.

Please let me know if you have any further questions or issues.

## File descriptions 

**NOTE:** Code parsing is not implemented yet. Files with extentions *".DS_Store", ".pdf", ".ipynb", ".csv", ".zip", ".pptx", ".jpg", ".jpeg",".png"* will be ommited.

**00_Administrative/Meeting_Minutes.md** 

- The meeting on May 25th, 2023 discussed updating the API to the final version and changing the pipeline to save 3 models to S3 directly. It was also mentioned that images of the architecture and cost are needed for the draft of the ppt. Tasks for the following Saturday include saving the 3 models to S3 bucket, ensuring containers work with changes, drafting the ppt, and reviewing project requirements.
- The meeting on May 18th, 2023 discussed uploading artifacts to the S3 bucket, the readiness of containers for the pipeline and tests, and the need to improve tests and the API. Tasks for the following week include fixing AWS readings, adding more tests for feature generation, saving more models, adding a drop-down for model prediction in the API, adding more models to the endpoint, starting the drafting of the presentation, and trying to deploy the API in AWS.
- The meeting on May 11th, 2023 discussed updating raw_data and clean_data to read data from and upload to S3 bucket, adding tests for the clean_data module, and the readiness of modules for generating features and modeling. Tasks for the following week include removing the profile_name option in AWS functions, completing the development of features and training, cost estimation, updating the API, showing progress to Ashish, building a Docker container for the pipeline, and starting the report and presentation.
- The meeting on May 4th, 2023 discussed the correctness of the diagram, the need to fix zip downloading, the evaluation of models, and the development of the API in Flask. Tasks for the following week include building a function to upload to S3, building source modules for generating features and modeling, cost estimation, building the app interface, setting up API endpoint on EC2.
- The meeting on April 26th, 2023 discussed data cleaning, the diagram, and various questions related to the project. Tasks for the following week include converting cleaning to a Python script, creating a second version of the diagram, uploading clean data to the S3 bucket, building ML models, and starting to build the API.
- The meeting on April 19th, 2023 discussed reviewing EDA and tasks for the following week include getting a raw and clean version of the original data set, creating an architecture diagram, creating AWS accounts and profiles, and learning about pipe implementation and automation in AWS.
- The meeting on April 13th, 2023 discussed project options and decided to use the flight prices problem. Tasks for the following week include drafting the cloud architecture and starting code for data ingestion and cleaning.
- The meeting on April 6th, 2023 discussed various data options for the project. The tasks for the following week include checking the 4 data set options for Cloud Engineering.

**00_Archive/emptyfile** 

The file 00_Archive/emptyfile is empty.

**01_Literature/emptyfile** 

This file is empty.

**02_Data/emptyfile** 

This file is empty.

**04_Implementation/app/README.md** 

This README file provides an overview of the Cloud_Engineering Final Project, which is focused on predicting airline prices using a pipeline. It includes information about the project's description, cloning the repository, running the application locally, and running the Docker container. The project utilizes a Flask application to serve a trained model as a RESTful API and uses Streamlit for the app interface. Instructions are provided for cloning the repository, running the application locally, and running the Docker container.

**04_Implementation/app/config/logging/webapp_log.yaml** 

This file is a YAML configuration file for logging in a web application. It specifies the version, handlers, formatters, loggers, and root level settings for logging. The handlers section defines a stream handler that logs to the standard output. The formatters section defines a formatter with a specific format and date format. The loggers section defines two loggers, one for the webapp with a debug level and the other for aggregate data with a debug level. The propagate setting is set to False for both loggers. The root section sets the debug level and uses the stream handler for logging.

**04_Implementation/app/config/webapp.yaml** 

This file contains the configuration settings for a web application. It includes the image path, flask URL, message header, and various input options such as airline, departure time, origin, and destination. It also includes AWS settings for a bucket name and prefix.

**04_Implementation/app/dockerfiles/Dockerfile** 

This Dockerfile sets up a Python 3.10.9-slim environment and installs the required dependencies listed in requirements.txt. It also copies the config, src, and plane.jpg files into the /app directory. The application is exposed on port 80 and the command "streamlit run --server.port=80 --server.fileWatcherType=none src/webapp.py" is executed when the container is run.

**04_Implementation/app/requirements.txt** 

This file contains the list of dependencies required for the application. The dependencies include libraries such as Flask, pandas, scikit-learn, and xgboost, among others.

**04_Implementation/app/src/aggregate_data.py** 

This file contains functions to aggregate data from a pandas dataframe. The functions include retrieving flight numbers for a given airline, finding the average duration of a flight for a given airline, origin, and destination, and finding the most likely arrival time for a given airline, origin, destination, and departure time. The functions also include error handling for invalid input values.

**04_Implementation/app/src/predict_api.py** 

This file provides an API endpoint for making predictions using a trained model. It loads models into memory when the Flask app starts and includes a route for making predictions.

**04_Implementation/app/src/webapp.py** 

This file is a Python script that contains the code for a web application. It imports various libraries and modules, sets up the page configuration, and defines functions for user inputs and predictions. The file also connects to AWS S3, loads a configuration file, and retrieves data from the S3 bucket. Finally, it makes requests to a Flask API to get predictions for flight prices based on user inputs.

**04_Implementation/app/test.py** 

This file contains a Python script that makes a POST request to an API endpoint and receives a JSON response. It defines the API endpoint URL and sample input data. It then sends a POST request using the requests library and checks if the request was successful. It retrieves the predicted price from the JSON response and prints it. It also handles exceptions for invalid JSON response and missing key in the response. Finally, it handles exceptions for a failed request.

**04_Implementation/pipeline/README.md** 

This README file provides an overview of the Cloud Engineering Final Project, which focuses on predicting airline prices using a pipeline. The project is developed by Alejandra Lelo de Larrea Ibarra, Bannasorn Paspanthong, Ruben Nakano, and Samuel Swain. The pipeline consists of several steps, including reading and concatenating multiple CSV files, cleaning and normalizing the data, generating features, and training different machine learning models. The parameters for running the pipeline are set in the default-config.yaml file, and artifacts and logs are saved to the artifacts and logging folders, respectively. The README also includes instructions for cloning the repository, running the pipeline locally, and running the pipeline using Docker containers. Finally, the AWS implementation of the pipeline is discussed, with artifacts stored in an S3 bucket.

**04_Implementation/pipeline/config/default-config.yaml** 

This file contains the default configuration for the airline price prediction pipeline in AWS. It includes information such as the name, author, version, description, dependencies, data source, and output location. It also specifies the AWS configuration for uploading data, the raw data file keys, the clean data configuration, the feature generation configuration, and the model training configuration.

**04_Implementation/pipeline/config/logging/local.conf** 

This file contains the configuration for logging in the pipeline. It defines loggers, handlers, and formatters. The loggers specify the level and handlers for each logger. The handlers specify the class, level, formatter, and arguments for each handler. The formatter specifies the format and date format for the log messages.

**04_Implementation/pipeline/dockerfiles/Dockerfile.pipeline_main** 

This Dockerfile sets up a Python 3.9-slim base image and creates a working directory in the container. It copies the requirements_main.txt file and installs the required libraries. It then copies the config, src, and pipeline.py files to run the pipeline. The command to run when running the Docker container is "python pipeline.py".

**04_Implementation/pipeline/dockerfiles/Dockerfile.tests Summary: This Dockerfile is used to build a Docker container for running tests in a pipeline. It sets the base image to python:3.9-slim and creates a working directory in the container. The requirements_tests.txt file is copied to the working directory and the libraries specified in the file are installed. The necessary folders and files for running the pipeline, including clean_data.py, generate_features.py, aws_utils.py, train_model.py, and the tests folder, are also copied. Finally, the command "pytest tests" is set to run when the Docker container is started.** 



**04_Implementation/pipeline/pipeline.py** 

This script orchestrates the entire pipeline for an airline price prediction project. It calls modules that perform the following steps: download raw data from S3 and save it locally, clean the raw data and save it locally, generate features from the cleaned data, train models using the generated features, evaluate the trained models and save the results locally, and upload all artifacts to S3. The pipeline can be configured using the file called 'default-config.yaml'.

**04_Implementation/pipeline/requirements_main.txt** 

This file contains a list of Python packages with their respective versions that are required for the pipeline. The packages include joblib, numpy, pandas, pandas-stubs, scikit-learn, scipy, boto3, matplotlib, PyYAML, Requests, types-requests, typing_extensions, xgboost, pytest, and pytest-cov. These packages have specific version requirements that are compatible with Python versions between 3.9 and 4.0.

**04_Implementation/pipeline/requirements_tests.txt** 

This file contains a list of required packages and their versions for testing the pipeline implementation. The packages include joblib, numpy, pandas, pandas-stubs, scikit-learn, scipy, boto3, matplotlib, PyYAML, Requests, types-requests, typing_extensions, xgboost, pytest-cov, pytest, pytest-mock, and mock.

**04_Implementation/pipeline/src/__init__.py** 

This file is an initialization file for the pipeline module.

**04_Implementation/pipeline/src/aws_utils.py** 

This file contains functions for uploading and retrieving files from an AWS S3 bucket. The functions include get_data_s3(), which retrieves a file from an S3 bucket, upload_artifacts(), which uploads all artifacts in a specified directory to an S3 bucket, and write_list_files(), which writes a list of S3 URIs of uploaded files to a local file.

**04_Implementation/pipeline/src/clean_data.py** 

This file contains functions for cleaning raw data by applying different transformations. It includes functions to extract the duration of an event in hours from a given string, extract the number of stops from a string using a regular expression pattern, map a given time to a specific hour bucket, clean and transform a raw data pandas DataFrame according to a provided configuration, and convert prices to numeric. The file also includes a function to create a cleaned pandas DataFrame.

**04_Implementation/pipeline/src/generate_features.py** 

This module provides functions for generating features from the cleaned data set.

**04_Implementation/pipeline/src/raw_data.py** 

This file provides functions for reading the original data sources and creating a raw data frame. It includes a function for reading multiple csv files from a zip file stored in an AWS S3 bucket, concatenating them into a single DataFrame, and returning it. It also includes a function for saving a dataframe as a csv file to a specified path.

**04_Implementation/pipeline/src/train_model.py** 

This module provides functions for training and evaluating models.

**04_Implementation/pipeline/tests/__init__.py** 

This file is an initialization file for the tests directory in the pipeline module.

**04_Implementation/pipeline/tests/test_clean_data.py** 

This file contains test cases for the clean_data module. It includes happy path tests and unhappy path tests for functions such as get_duration, get_stops, and bucket_hours.

**04_Implementation/pipeline/tests/test_generate_features.py** 

This file contains test cases for the functions log_transform, drop_columns, and filter_airlines in the src.generate_features module. The log_transform function is tested with both happy and unhappy paths, checking if the columns 'A' and 'B' are correctly transformed using the np.log function. The drop_columns function is also tested with happy and unhappy paths, checking if the 'A' column is dropped and if the 'B' column is still present. The filter_airlines function is tested with happy and unhappy paths, checking if the 'B' airline is correctly filtered out and if an empty DataFrame is returned. Additionally, an unhappy path test is included for the case where the 'airline' column is missing in the DataFrame.

**04_Implementation/pipeline/tests/test_train_model.py** 

This file contains test functions for the train_model module. It imports various libraries for testing, defines sample test data and configuration, and includes test functions for defining a preprocessor, training a model, and calculating metrics.

**05_Deliverables/AppDemo.mp4** 

The file contains a demonstration video of the application.

**README.md** 

This file provides an overview of the Cloud Engineering Final Project, which focuses on predicting airline prices. It includes information on the business problem, data description, data science project, pipeline, web application, and project structure.

