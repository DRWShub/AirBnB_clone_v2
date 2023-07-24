#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_$(date +'%Y-%m-%dT%H:%M:%S%z').tgz web_static")  # noqa

    except Exception as e:
        return None
