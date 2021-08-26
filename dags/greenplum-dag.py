from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta


with DAG(
    'greenplum_dag',
    start_date=datetime(2021, 1, 1),
    max_active_runs=3,
    schedule_interval='@daily',
    default_args={
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 0,
    },
    catchup=False
) as dag:

    opr_test_query = PostgresOperator(
        task_id='test_query',
        postgres_conn_id='gpdb',
        sql='SELECT * FROM covid_state_data'
    )
