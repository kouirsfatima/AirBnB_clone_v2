#!/usr/bin/env python3
from fabric.api import env, put, run
from os.path import exists

env.hosts = ["54.144.148.22, 52.3.220.160 "] 
def do_deploy(archive_path):
    """Deploy the archive to the server."""
    if not exists(archive_path):
        return False

        put(archive_path, "/tmp/")

        archive_filename = archive_path.split("/")[-1]

        run("mkdir -p /data/web_static/releases/{}/".format(archive_filename[:-4]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename, archive_filename[:-4]))

        run("rm /tmp/{}".format(archive_filename))

        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
            archive_filename[:-4], archive_filename[:-4]))

        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_filename[:-4]))

        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            archive_filename[:-4]))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False

