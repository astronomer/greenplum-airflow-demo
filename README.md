# greenplum-airflow-demo
This repo contains an Astronomer project with two DAGs used to demonstrate how Airflow can be used with Greenplum. 

## Getting Started
The easiest way to run these example DAGs is to use the Astronomer CLI to get an Airflow instance up and running locally:

 1. [Install the Astronomer CLI](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart)
 2. Clone this repo somewhere locally and navigate to it in your terminal
 3. Initialize an Astronomer project by running `astro dev init`
 4. Start Airflow locally by running `astro dev start`
 5. Navigate to localhost:8080 in your browser and you should see the tutorial DAGs there
 
## DAG Overview
This repo contains two example DAGs that are described here.

 - 'greenplum-dag': a simple DAG with a single Postgres Operator that runs a query against a Greenplum db
 - 'greenplum-advanced': a DAG that runs multiple, parameterized dynamic queries against a Greenplum db based on a list of provided states using the PostgresOperator, and then sends an email upon successful completion using the EmailOperator.
 
To run either DAG successfully you will need to add an Airflow connection of type 'Postgres' to connect to your Greenplum db. To run the advanced DAG you will also need to configure SMTP for the EmailOperator to succeed. 
