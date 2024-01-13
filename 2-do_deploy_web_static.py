#!/usr/bin/python3
"""
A script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers
"""


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['46.346.275.234', '65.276.72.310'] 
# <IP web-01>, <IP web-02>
# ^ All remote commands must be executed on your both web servers
# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)


def do_deploy(archive_path):
    """ 
    Distributes an archive to web servers
    """
    if exists(archive_path) is False:
        return False  # Returns False if the file at archive_path doesnt exist
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except:
        return False
