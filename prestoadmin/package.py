import logging
from fabric.decorators import task

from fabric.operations import sudo, put, os
from prestoadmin.util import constants

_LOGGER = logging.getLogger(__name__)
__all__ = ['install']


@task
def install(local_path):
    deploy(local_path)
    rpm_install(os.path.basename(local_path))


def deploy(local_path=None):
    _LOGGER.debug("Deploying rpm to nodes")
    sudo('mkdir -p ' + constants.REMOTE_PACKAGES_PATH)
    put(local_path, constants.REMOTE_PACKAGES_PATH, use_sudo=True)


def rpm_install(rpm_name):
    _LOGGER.info("Installing the rpm")
    sudo('rpm -i ' + constants.REMOTE_PACKAGES_PATH + "/" + rpm_name)