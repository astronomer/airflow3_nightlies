# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-celery",
        "name": "Celery",
        "description": "`Celery <https://docs.celeryq.dev/en/stable/>`__\n",
        "state": "ready",
        "source-date-epoch": 1743477793,
        "versions": [
            "3.10.5.dev202504030001",
            "3.10.3",
            "3.10.2",
            "3.10.0",
            "3.9.0",
            "3.8.5",
            "3.8.4",
            "3.8.3",
            "3.8.2",
            "3.8.1",
            "3.8.0",
            "3.7.3",
            "3.7.2",
            "3.7.1",
            "3.7.0",
            "3.6.2",
            "3.6.1",
            "3.6.0",
            "3.5.2",
            "3.5.1",
            "3.5.0",
            "3.4.1",
            "3.4.0",
            "3.3.4",
            "3.3.3",
            "3.3.2",
            "3.3.1",
            "3.3.0",
            "3.2.1",
            "3.2.0",
            "3.1.0",
            "3.0.0",
            "2.1.4",
            "2.1.3",
            "2.1.2",
            "2.1.1",
            "2.1.0",
            "2.0.0",
            "1.0.1",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Celery",
                "external-doc-url": "https://docs.celeryq.dev/en/stable/",
                "logo": "/docs/integration-logos/Celery.png",
                "tags": ["software"],
            }
        ],
        "sensors": [
            {
                "integration-name": "Celery",
                "python-modules": ["airflow.providers.celery.sensors.celery_queue"],
            }
        ],
        "executors": [
            "airflow.providers.celery.executors.celery_executor.CeleryExecutor",
            "airflow.providers.celery.executors.celery_kubernetes_executor.CeleryKubernetesExecutor",
        ],
        "config": {
            "celery_kubernetes_executor": {
                "description": "This section only applies if you are using the ``CeleryKubernetesExecutor`` in\n``[core]`` section above\n",
                "options": {
                    "kubernetes_queue": {
                        "description": "Define when to send a task to ``KubernetesExecutor`` when using ``CeleryKubernetesExecutor``.\nWhen the queue of a task is the value of ``kubernetes_queue`` (default ``kubernetes``),\nthe task is executed via ``KubernetesExecutor``,\notherwise via ``CeleryExecutor``\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "kubernetes",
                    }
                },
            },
            "celery": {
                "description": "This section only applies if you are using the CeleryExecutor in\n``[core]`` section above\n",
                "options": {
                    "celery_app_name": {
                        "description": "The app name that will be used by celery\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "airflow.providers.celery.executors.celery_executor",
                    },
                    "worker_concurrency": {
                        "description": "The concurrency that will be used when starting workers with the\n``airflow celery worker`` command. This defines the number of task instances that\na worker will take, so size up your workers based on the resources on\nyour worker box and the nature of your tasks\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "16",
                    },
                    "worker_autoscale": {
                        "description": "The maximum and minimum number of pool processes that will be used to dynamically resize\nthe pool based on load.Enable autoscaling by providing max_concurrency,min_concurrency\nwith the ``airflow celery worker`` command (always keep minimum processes,\nbut grow to maximum if necessary).\nPick these numbers based on resources on worker box and the nature of the task.\nIf autoscale option is available, worker_concurrency will be ignored.\nhttps://docs.celeryq.dev/en/latest/reference/celery.bin.worker.html#cmdoption-celery-worker-autoscale\n",
                        "version_added": None,
                        "type": "string",
                        "example": "16,12",
                        "default": None,
                    },
                    "worker_prefetch_multiplier": {
                        "description": "Used to increase the number of tasks that a worker prefetches which can improve performance.\nThe number of processes multiplied by worker_prefetch_multiplier is the number of tasks\nthat are prefetched by a worker. A value greater than 1 can result in tasks being unnecessarily\nblocked if there are multiple workers and one worker prefetches tasks that sit behind long\nrunning tasks while another worker has unutilized processes that are unable to process the already\nclaimed blocked tasks.\nhttps://docs.celeryq.dev/en/stable/userguide/optimizing.html#prefetch-limits\n",
                        "version_added": None,
                        "type": "integer",
                        "example": None,
                        "default": "1",
                    },
                    "worker_enable_remote_control": {
                        "description": "Specify if remote control of the workers is enabled.\nIn some cases when the broker does not support remote control, Celery creates lots of\n``.*reply-celery-pidbox`` queues. You can prevent this by setting this to false.\nHowever, with this disabled Flower won't work.\nhttps://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#broker-overview\n",
                        "version_added": None,
                        "type": "boolean",
                        "example": None,
                        "default": "true",
                    },
                    "broker_url": {
                        "description": "The Celery broker URL. Celery supports RabbitMQ, Redis and experimentally\na sqlalchemy database. Refer to the Celery documentation for more information.\n",
                        "version_added": None,
                        "type": "string",
                        "sensitive": True,
                        "example": None,
                        "default": "redis://redis:6379/0",
                    },
                    "result_backend": {
                        "description": "The Celery result_backend. When a job finishes, it needs to update the\nmetadata of the job. Therefore it will post a message on a message bus,\nor insert it into a database (depending of the backend)\nThis status is used by the scheduler to update the state of the task\nThe use of a database is highly recommended\nWhen not specified, sql_alchemy_conn with a db+ scheme prefix will be used\nhttps://docs.celeryq.dev/en/latest/userguide/configuration.html#task-result-backend-settings\n",
                        "version_added": None,
                        "type": "string",
                        "sensitive": True,
                        "example": "db+postgresql://postgres:airflow@postgres/airflow",
                        "default": None,
                    },
                    "result_backend_sqlalchemy_engine_options": {
                        "description": "Optional configuration dictionary to pass to the Celery result backend SQLAlchemy engine.\n",
                        "version_added": None,
                        "type": "string",
                        "example": '{"pool_recycle": 1800}',
                        "default": "",
                    },
                    "flower_host": {
                        "description": "Celery Flower is a sweet UI for Celery. Airflow has a shortcut to start\nit ``airflow celery flower``. This defines the IP that Celery Flower runs on\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "0.0.0.0",
                    },
                    "flower_url_prefix": {
                        "description": "The root URL for Flower\n",
                        "version_added": None,
                        "type": "string",
                        "example": "/flower",
                        "default": "",
                    },
                    "flower_port": {
                        "description": "This defines the port that Celery Flower runs on\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "5555",
                    },
                    "flower_basic_auth": {
                        "description": "Securing Flower with Basic Authentication\nAccepts user:password pairs separated by a comma\n",
                        "version_added": None,
                        "type": "string",
                        "sensitive": True,
                        "example": "user1:password1,user2:password2",
                        "default": "",
                    },
                    "sync_parallelism": {
                        "description": "How many processes CeleryExecutor uses to sync task state.\n0 means to use max(1, number of cores - 1) processes.\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "0",
                    },
                    "celery_config_options": {
                        "description": "Import path for celery configuration options\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "airflow.providers.celery.executors.default_celery.DEFAULT_CELERY_CONFIG",
                    },
                    "ssl_active": {
                        "description": None,
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "False",
                    },
                    "ssl_key": {
                        "description": "Path to the client key.\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "",
                    },
                    "ssl_cert": {
                        "description": "Path to the client certificate.\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "",
                    },
                    "ssl_cacert": {
                        "description": "Path to the CA certificate.\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "",
                    },
                    "pool": {
                        "description": "Celery Pool implementation.\nChoices include: ``prefork`` (default), ``eventlet``, ``gevent`` or ``solo``.\nSee:\nhttps://docs.celeryq.dev/en/latest/userguide/workers.html#concurrency\nhttps://docs.celeryq.dev/en/latest/userguide/concurrency/eventlet.html\n",
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "prefork",
                    },
                    "operation_timeout": {
                        "description": "The number of seconds to wait before timing out ``send_task_to_executor`` or\n``fetch_celery_task_state`` operations.\n",
                        "version_added": None,
                        "type": "float",
                        "example": None,
                        "default": "1.0",
                    },
                    "task_acks_late": {
                        "description": "If an Airflow task's execution time exceeds the visibility_timeout, Celery will re-assign the\ntask to a Celery worker, even if the original task is still running successfully. The new task\ninstance then runs concurrently with the original task and the Airflow UI and logs only show an\nerror message:\n'Task Instance Not Running' FAILED: Task is in the running state'\nSetting task_acks_late to True will force Celery to wait until a task is finished before a\nnew task instance is assigned. This effectively overrides the visibility timeout.\nSee also:\nhttps://docs.celeryq.dev/en/stable/reference/celery.app.task.html#celery.app.task.Task.acks_late\n",
                        "version_added": "3.6.0",
                        "type": "boolean",
                        "example": "True",
                        "default": "True",
                    },
                    "task_track_started": {
                        "description": "Celery task will report its status as 'started' when the task is executed by a worker.\nThis is used in Airflow to keep track of the running tasks and if a Scheduler is restarted\nor run in HA mode, it can adopt the orphan tasks launched by previous SchedulerJob.\n",
                        "version_added": None,
                        "type": "boolean",
                        "example": None,
                        "default": "True",
                    },
                    "task_publish_max_retries": {
                        "description": "The Maximum number of retries for publishing task messages to the broker when failing\ndue to ``AirflowTaskTimeout`` error before giving up and marking Task as failed.\n",
                        "version_added": None,
                        "type": "integer",
                        "example": None,
                        "default": "3",
                    },
                    "extra_celery_config": {
                        "description": 'Extra celery configs to include in the celery worker.\nAny of the celery config can be added to this config and it\nwill be applied while starting the celery worker. e.g. {"worker_max_tasks_per_child": 10}\nSee also:\nhttps://docs.celeryq.dev/en/stable/userguide/configuration.html#configuration-and-defaults\n',
                        "version_added": None,
                        "type": "string",
                        "example": None,
                        "default": "{{}}",
                    },
                },
            },
            "celery_broker_transport_options": {
                "description": "This section is for specifying options which can be passed to the\nunderlying celery broker transport. See:\nhttps://docs.celeryq.dev/en/latest/userguide/configuration.html#std:setting-broker_transport_options\n",
                "options": {
                    "visibility_timeout": {
                        "description": "The visibility timeout defines the number of seconds to wait for the worker\nto acknowledge the task before the message is redelivered to another worker.\nMake sure to increase the visibility timeout to match the time of the longest\nETA you're planning to use.\nvisibility_timeout is only supported for Redis and SQS celery brokers.\nSee:\nhttps://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#visibility-timeout\n",
                        "version_added": None,
                        "type": "string",
                        "example": "21600",
                        "default": None,
                    },
                    "sentinel_kwargs": {
                        "description": "The sentinel_kwargs parameter allows passing additional options to the Sentinel client.\nIn a typical scenario where Redis Sentinel is used as the broker and Redis servers are\npassword-protected, the password needs to be passed through this parameter. Although its\ntype is string, it is required to pass a string that conforms to the dictionary format.\nSee:\nhttps://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#configuration\n",
                        "version_added": None,
                        "type": "string",
                        "sensitive": True,
                        "example": '{"password": "password_for_redis_server"}',
                        "default": None,
                    },
                },
            },
        },
        "dependencies": ["apache-airflow>=2.9.0", "celery[redis]>=5.5.0,<6", "flower>=1.0.0"],
        "optional-dependencies": {"cncf.kubernetes": ["apache-airflow-providers-cncf-kubernetes>=7.4.0"]},
        "devel-dependencies": [],
    }
