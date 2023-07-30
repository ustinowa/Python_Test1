from checkout import checkout, FOLDER_OUT, FOLDER_TST, FOLDER_folder1


def test_step1():
    assert checkout(f"cd {FOLDER_OUT}; 7z e bad.7z -o{FOLDER_folder1} -y", "Is not archive"), "test1 FAIL"


def test_step2():
    assert checkout(f"cd {FOLDER_OUT}; 7z t bad.7z", "Is not archive"), "test3 FAIL"