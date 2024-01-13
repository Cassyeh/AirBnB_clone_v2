#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents
of the web_static folder in directory
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Returns the .tgz archive path if archive has been correctly generated
    else, return None
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
