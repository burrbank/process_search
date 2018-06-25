import os
import subprocess as subpr
import re

if not os.name == 'posix':
    raise OSError('OS not currently supported')


def format_response(row):
    """Separate row from ps into an organized object"""
    pat = re.compile('[ ]+')
    row = re.split(pat, row)
    length = len(row)
    args = None
    if length == 3:
        pid, user, cmd = row
    elif length > 3:
        pid = row[1]
        user = row[2]
        cmd = row[3]
        args = row[4:]
    else:
        pid, user, cmd = None, None, None

    return pid, user, cmd, args


def list_all():
    """list all processes currently running on system"""
    ps = subpr.Popen(['ps', '-eo', 'pid,user,args'], stdout=subpr.PIPE)
    res = ps.stdout.read().split('\n')
    out = [format_response(x) for x in res]
    return out


def list_all_python():
    """list all currently running python processes"""
    return [x for x in list_all() if x[2] is not None and x[2] == 'python']


def is_running(script_name):
    """"determine if a particular python script is running"""
    py_proc = list_all_python()
    for _, _, _, args in py_proc:
        if args[0] == script_name:
            return True
    else:
        return False


if __name__ == '__main__':
    print(list_all_python())
    print(is_running('main.py'))
    print(is_running('test.py'))

