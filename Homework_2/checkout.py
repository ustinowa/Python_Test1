import subprocess

FOLDER_TST = "/home/user/tst"
FOLDER_OUT = "/home/user/out"
FOLDER_folder1 = "/home/user/folder_1"
FOLDER_folder2 = "/home/user/folder_2"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0 or text in result.stderr:
        return True
    else:
        return False