from airflow.models import DAG

from datetime import datetime

default_args = {"start_date": datetime(2020, 1, 1)}
#
# with DAG(
#         "user_processing",
#         schedule_interval="@daily",
#         start_date=datetime(2020, 1, 1),
#         catchup=False,
#         default_args=default_args
# ) as dag:
#
