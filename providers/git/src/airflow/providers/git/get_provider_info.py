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
        "package-name": "apache-airflow-providers-git",
        "name": "GIT",
        "description": "`Distributed version control system (GIT) <https://git-scm.com/>`__\n",
        "state": "not-ready",
        "source-date-epoch": 1742823216,
        "versions": ["0.0.2.dev202504020002"],
        "integrations": [
            {
                "integration-name": "GIT (Git)",
                "external-doc-url": "https://git-scm.com/",
                "tags": ["software"],
            }
        ],
        "hooks": [{"integration-name": "GIT", "python-modules": ["airflow.providers.git.hooks.git"]}],
        "bundles": [{"integration-name": "GIT", "python-modules": ["airflow.providers.git.bundles.git"]}],
        "connection-types": [
            {"hook-class-name": "airflow.providers.git.hooks.git.GitHook", "connection-type": "git"}
        ],
        "dependencies": ["apache-airflow>=3.0.0.dev0", "GitPython>=3.1.44"],
        "devel-dependencies": [],
    }
