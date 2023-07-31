from sshcheckers import ssh_checkout, upload_files


def test_1():
    res = []
    upload_files("0.0.0.0", "user2", "12345", "p7zip-full.deb",
                 "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", "echo '12345' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "12345", "echo '12345' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    assert all(res), "test1 FAIL"
