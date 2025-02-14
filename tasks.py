import glob
import shutil
from invoke import task


@task(aliases=['c'])
def clean(c):
    """Delete all .egg-info directories."""
    egg_info_dirs = glob.glob('**/*.egg-info', recursive=True)
    for dir in egg_info_dirs:
        shutil.rmtree(dir)
        print(f"Deleted {dir}")


@task(aliases=['i'])
def install(c):
    """Install the package in development mode."""
    c.run('pip install --upgrade pip')
    c.run('pip install -e .')