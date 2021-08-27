from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

default_args = {"start_date": datetime(2021, 8, 8)}

with DAG(
    "parallel_dag_03",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=True,
) as dag:
    task_1 = BashOperator(task_id="task_1", bash_command="echo ${USER}")

    with TaskGroup("processing_tasks") as processing_tasks:
        task_2 = BashOperator(task_id="task_2", bash_command="echo task 2")

        with TaskGroup("jupyter_task") as jupyter_task:
            task_jup = BashOperator(task_id="task_1", bash_command="echo hello")

        task_3 = BashOperator(task_id="task_3", bash_command="echo task 3")

    task_4 = BashOperator(task_id="task_4", bash_command="firefox gmail.com")

    task_5 = BashOperator(
        task_id="task_5",
        bash_command="echo hello from airflow > ~/Documents/hello_airflow.txt",
    )

    task_1 >> processing_tasks >> task_4 >> task_5
