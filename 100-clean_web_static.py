#!/usr/bin/python3
"""
A script that deletes out-of-date archives
"""

import os
from fabric.api import *

env.hosts = ['46.346.275.234', '65.276.72.310']
# <IP web-01>, <IP web-02>
# ^ All remote commands must be executed on your both web servers
# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)


def do_clean(number=0):
    """
    Delete all unnecessary archives
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
