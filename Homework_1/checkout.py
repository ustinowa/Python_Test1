import string
import subprocess


def checkout(cmd, text_of_found, advance=False, word=None):
    if advance:
        found_list = text_of_found.split()
        for i in found_list:
            if i[-1] in string.punctuation:
                res = i.replace(i[-1], '')
                if word == res:
                    return True
        return False
    else:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        if text_of_found in result.stdout and result.returncode == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(checkout('cat /etc/os-release', 'Jammy, Jellyfish!', True, 'Jellyfish'))