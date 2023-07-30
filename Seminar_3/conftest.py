import pytest
from checkout import checkout
import random, string
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data["FOLDER_TST"]
FOLDER_OUT = data["FOLDER_OUT"]
FOLDER_folder1 = data["FOLDER_folder1"]

@pytest.fixture()
def make_folders():
    return checkout(f"mkdir {FOLDER_TST} {FOLDER_OUT} {FOLDER_folder1}", "")

@pytest.fixture()
def make_files():
    list_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits))
        if checkout(f"cd {FOLDER_TST}; dd if=/dev/urandom of={filename} bs={data['size1']} count={data['count']} iflag=fullblock", ""):
            list_files.append(filename)
    return list_files

@pytest.fixture()
def clear_dir():
    return checkout(f"rm -rf {FOLDER_OUT}/* {FOLDER_TST}/* {FOLDER_folder1}/*", "")

# @pytest.fixture()
# def make_subfolder():
#     testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#     subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#     if not checkout("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
#         return None, None
#     if not checkout("cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], subfoldername, testfilename), ""):
#         return subfoldername, None
#     else:
#         return subfoldername, testfilename
#
#
#
# @pytest.fixture(autouse=True)
# def print_time():
#     print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
#     yield
#     print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))

