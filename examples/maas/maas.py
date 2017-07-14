# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Managing maas

"""


def overwrite_agent(conn):
    agent_dict = {
        'ip': "255.255.255.255",
        'port': "8080",
        'agent_name': "agent_name",
    }
    print(conn.maas.overwrite_agent(**agent_dict))


def delete_agent(conn):
    conn.maas.delete_agent("255.255.255.0")


def agents(conn):
    print("list all agents")
    for a in conn.maas.agents():
        print(a)


def create_task(conn):
    task_dict = {
        "src_node":
        {
            "region": "source_region",
            "ak": "source_ak",
            "sk": "source_sk",
            "object_key":
            {
                "path": "log/",
                "keys": ["object1", "object2"]
            },
            "bucket": "source_bucket"
        },
        "thread_num": 5,
        "enableKMS": True,
        "enable_tas": False,
        "dst_node":
        {
            "region": "target_region",
            "ak": "target_ak",
            "sk": "target_sk",
            "object_key": "targetkey",
            "bucket": "targetbucket"
        },
    }

    task = conn.maas.create_task(**task_dict)
    print(task)


def tasks(conn):
    query = {
        'start': '0',
        'limit': '10'}
    for t in conn.maas.tasks(**query):
        print(t)


def task_count(conn):
    print(conn.maas.task_count('0'))
