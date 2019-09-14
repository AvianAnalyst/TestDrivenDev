# Provisioning a new site
___
## Required Packages:

* nginx
* Python 3.7
* pipenv + pip
* Git

eg, on Ubuntu:

```bash
sudo apt update
sudo apt install python3.7 pip nginx git
python3.7 -m pip install pipenv
# Add .local/python/bin to path if it isn't already
export PATH=$PATH:/home/USER/.local/bin
```

## Nginx Virtual Host config
* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service
* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username
/home/username <br>
└── sites <br>
&emsp;├── DOMAIN1 <br>
&emsp;│&emsp;├── .env <br>
&emsp;│&emsp;├── db.sqlite3 <br>
&emsp;│&emsp;├── manage.py etc <br>
&emsp;│&emsp;├── static <br>
&emsp;│&emsp;└── virtualenv <br>
&emsp;└── DOMAIN2 <br>
&emsp; &emsp;├── .env <br>
&emsp; &emsp;├── db.sqlite3 <br>
&emsp; &emsp;├── etc <br>