from checkout import checkout
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data["FOLDER_TST"]
FOLDER_OUT = data["FOLDER_OUT"]
FOLDER_folder1 = data["FOLDER_folder1"]


def test_step1(clear_dir, get_dir, make_file):
    res1 = checkout(f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_OUT}", "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    res1 = checkout(f"cd {FOLDER_OUT}; 7z e arx2.7z -o{FOLDER_folder1} -y", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_folder1}", "test1.txt")
    assert res1 and res2, "test2 FAIL"


def test_step3():
    assert checkout(f"cd {FOLDER_OUT}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    assert checkout(f"cd {FOLDER_OUT}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    assert checkout(f"cd {FOLDER_OUT}; 7z u arx2.7z", "Everything is Ok"), "test5 FAIL"