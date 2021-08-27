from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator

from subdags import subdag_parallel_processing


default_args = {"start_date": datetime(2021, 8, 10)}

with DAG(
    "parallel_dag_02", schedule_interval="@daily", default_args=default_args
) as dag:
    task_1 = BashOperator(task_id="task_1", bash_command="echo task 1")
    processing = SubDagOperator(
        task_id="processing_tasks",
        subdag=subdag_parallel_processing.subdag_parallel_dag(
            "parallel_dag_02", "processing_tasks", default_args
        ),
    )
    task_4 = BashOperator(task_id="task_4", bash_command="ls ~/Documents")

    task_1 >> processing >> task_4
