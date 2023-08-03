from checkout import checkout
import yaml

with open('config.yml') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data["FOLDER_TST"]
FOLDER_OUT = data["FOLDER_OUT"]
FOLDER_folder1 = data["FOLDER_folder1"]


def test_step1(get_bad_file):
    assert checkout(f"cd {FOLDER_OUT}; 7z e arx_bad.7z -o{FOLDER_folder1} -y", "Is not archive"), "test1 FAIL"


def test_step2(get_bad_file):
    assert checkout(f"cd {FOLDER_OUT}; 7z t arx_bad.7z", "Is not archive"), "test3 FAIL"