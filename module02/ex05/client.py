#!/usr/bin/env python3

# ============================================================================#
# =============================== LIBRARIES ==================================#
# ============================================================================#

import sys
import click
import requests

# ============================================================================#
# ================================ FUNCTIONS =================================#
# ============================================================================#


@click.group()
def cli():
    pass

@click.command()
@click.option('--ip', default='0.0.0.0', help="Ip of the API")
def ping(ip):
    r = requests.get("http://{}:5000/".format(ip)).json()
    if r['status'] == 200:
        print(r['message'])

@click.command()
@click.option('--ip', default='0.0.0.0', help="Ip of the API")
def list(ip):
    r = requests.get("http://{}:5000/list_files".format(ip)).json()
    if r['status'] == 200:
        for e in r['content']:
            print(e)

@click.command()
@click.option('--ip', default='0.0.0.0', help="Ip of the API")
@click.option('--filename', help="File")
def delete(ip, filename):
    r = requests.get("http://{}:5000/delete/{}".format(ip, filename)).json()
    if r['status'] == 200:
        print(r['message'])

@click.command()
@click.option('--ip', default='0.0.0.0', help="Ip of the API")
@click.option('--filename', help="File")
def upload(ip, filename):
    r = requests.get("http://{}:5000/upload/{}".format(ip, filename)).json()
    if r['status'] == 200:
        with open(filename, 'rb') as file_to_upload:
            files = {'file': (filename, file_to_upload)}
            upload_response = requests.post(r['content']['url'], data=r['content']['fields'], files=files)
            if upload_response.status_code == 204:
                print(r['message'])

@click.command()
@click.option('--ip', default='0.0.0.0', help="Ip of the API")
@click.option('--filename', help="File")
def download(ip, filename):
    r = requests.get("http://{}:5000/download/{}".format(ip, filename)).json()
    if r['status'] == 200:
        rr = requests.get(r['content'])
        with open(filename, 'wb') as f:
            f.write(rr.content)
        print(r['message'])

cli.add_command(ping)
cli.add_command(list)
cli.add_command(delete)
cli.add_command(upload)
cli.add_command(download)

if __name__ == "__main__":
    cli()