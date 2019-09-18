import random

from fabric import task
from patchwork.files import append, exists


REPO_URL = 'https://github.com/aviananalyst/testdrivendev.git'


def _get_latest_source(c, current_commit):
    print('check if .git exists')
    if exists(c, '.git'):
        print('it does, git fetch')
        c.run('git fetch')
    else:
        print('it does not, git clone repo')
        c.run(f'git clone {REPO_URL} .')

    print('update to current commit')
    c.run(f'git reset --hard {current_commit}')


def _create_or_update_dotenv(c):
    print('add django debug env var')
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    print('add sitename env var')
    append('.env', f'SITENAME={c.host}')
    print('check if secret key exists')
    current_contents = c.run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        print('it does not, make a new one and add it')
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')
    else:
        print('it does')


@task
def deploy(c):
    site_folder = f'/home/{c.user}/sites/{c.host}'
    print(f'site_folder set to: {site_folder}')
    print('ensure site directory exists')
    c.run(f'mkdir -p {site_folder}')
    print('get current commit')
    current_commit = c.local("git log -n 1 --format=%h")
    print('following commands done in site_folder on remote machine')
    with c.cd(site_folder):
        print('update source')
        _get_latest_source(c, current_commit)
        print('update dependencies')
        c.run('pipenv sync')
        print('update dotenv')
        _create_or_update_dotenv(c)
        print('collect static files')
        c.run('pipenv run collect_static')
        print('perform migrations')
        c.run('pipenv run update_db')

