#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy."""
from fabric.api import *
from os import path
env.hosts = ['54.237.92.118', '100.25.17.250']


def do_deploy(archive_path):
    """Function to deploy"""
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        name_file = archive_path.split("/")[-1]
        name_folder = ("/data/web_static/releases/" + name_file.split(".")[0])
        run("mkdir -p {}".format(name_folder))
        run("tar -xzf /tmp/{} -C {}".format(name_file, name_folder))
        run("rm /tmp/{}".format(name_file))
        run("mv {}/web_static/* {}".format(name_folder, name_folder))
        run("rm -rf {}/web_static".format(name_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(name_folder))
        return True
    except Exception:
        return False
