import pytest
from checkout import checkout
import random
import string
import yaml
from checkout import get_out
from datetime import datetime

with open('config.yml') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data["FOLDER_TST"]
FOLDER_OUT = data["FOLDER_OUT"]
FOLDER_folder1 = data["FOLDER_folder1"]
count = data["count"]
size1 = data["size1"]


@pytest.fixture()
def get_dir():
    return checkout(f"mkdir {FOLDER_TST} {FOLDER_OUT} {FOLDER_folder1}", "")


@pytest.fixture()
def make_files():
    list_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout(f"cd {FOLDER_TST}; dd if=/dev/urandom of={filename} bs={data['size1']} count={data['count']} iflag=fullblock", ""):
            list_files.append(filename)
    return list_files


@pytest.fixture()
def clear_dir():
    return checkout(f"rm -rf {FOLDER_OUT}/* {FOLDER_TST}/* {FOLDER_folder1}/*", "")


@pytest.fixture()
def get_list():
    return get_out(f'ls {FOLDER_TST}')[0]


@pytest.fixture()
def get_bad_file():
    checkout(f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx_bad", "Everything is Ok")
    checkout(f"truncate -s {FOLDER_OUT}/arx_bad.7z")
    yield "arx_bad"
    checkout(f"rm -rf {FOLDER_OUT}/arx_bad")


@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@pytest.fixture()
def make_stat(start_time):
    name = "stat.txt"
    with open(name, "a", encoding="utf-8") as f:
        f.write(''.join(get_out(f"echo 'время: {start_time}, количество файлов: {count}, размер файла: {size1}\n'; cat /proc/loadavg >> {name}")[0]))




