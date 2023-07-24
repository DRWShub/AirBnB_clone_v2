#!/usr/bin/python3
"""Script to delete outdated version from archives"""
import os
from fabric.api import *

env.user = "ubuntu"
env.hosts = ["100.25.118.189", "34.234.204.223"]
env.key_filename = ["~/.ssh/id_rsa", "~/.ssh/id_rsa_new"]


def do_clean(number=0):
    """function to delete outdated versions"""
    for host, key_file in zip(env.hosts, env.key_filename):
        env.host_string = host
        env.key_filename = key_file

    number = 1 if int(number) == 0 else int(number)

    archvs = sorted(os.listdir("versions"))
    [archvs.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archvs]

    with cd("/data/web_static/releases"):
        archvs = run("ls -tr").split()
        archvs = [a for a in archvs if "web_static_" in a]
        [archvs.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archvs]