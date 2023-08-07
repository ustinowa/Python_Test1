from checkout import *
from sshcheckers import *
import yaml

with open('config.yml') as f:
    data = yaml.safe_load(f)
FOLDER_TST = "/home/user2/tst"
FOLDER_OUT = "/home/user2/out"
FOLDER_folder1 = "/home/user2/folder1"


def safe_log(start_time, name):
    with open(name, "w", encoding="utf-8") as f:
        f.write(''.join(get_out(f"journalctl --since '{start_time}'")[0]))


def test_1(start_time, make_stat):
    res = []
    upload_files("0.0.0.0", "user2", "12345", "p7zip-full.deb",
                 "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", "echo '12345' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", "echo '12345' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    safe_log(start_time, "log_test1")
    assert all(res), "test1 FAIL"


def test_step1(clear_dir, get_dir, start_time, make_stat):
    res = []
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2", "Everything is Ok"))
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", f"ls {FOLDER_OUT}", "arx2.7z"))
    safe_log(start_time, "log_test2")
    assert all(res), "test1 FAIL"


def test_step2(clear_dir, get_dir, make_files, start_time, make_stat):
    res = []
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", f"cd {FOLDER_TST}; "
                                                         f"7z a {FOLDER_OUT}/arx2", "Everything is Ok"))
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", f"cd {FOLDER_OUT}; "
                                                         f"7z e arx2.7z -o{FOLDER_folder1} -y", "Everything is Ok"))
    for i in make_files:
        res.append(ssh_checkout("0.0.0.0", "user2", "12345", f"ls {FOLDER_folder1}", i))
    safe_log(start_time, "log_test3")
    assert all(res), "test2 FAIL"


def test_step3(start_time, make_stat):
    safe_log(start_time, "log_test4")
    assert ssh_checkout("0.0.0.0", "user2", "12345", f"cd {FOLDER_OUT}; "
                                                     f"7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4(get_list, start_time, make_stat):
    safe_log(start_time, "log_test5")
    assert ssh_checkout("0.0.0.0", "user2", "12345", f"cd {FOLDER_OUT}; "
                                                     f"7z d arx2.7z {get_list[0]}", "Everything is Ok"), "test4 FAIL"


def test_step5(get_list, start_time, make_stat):
    safe_log(start_time, "log_test6")
    assert ssh_checkout("0.0.0.0", "user2", "12345",
                        f"cd {FOLDER_TST}; echo 'hello' >> {get_list[1]}; cd {FOLDER_OUT}; "
                        f"7z u arx2.7z {FOLDER_TST}/{get_list[1]}", "Everything is Ok"), "test5 FAIL"