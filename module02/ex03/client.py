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


cli.add_command(ping)
cli.add_command(list)

if __name__ == "__main__":
    cli()