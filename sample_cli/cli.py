# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name', help='The person to greet')
def main(count, name):
    for x in range(count):
        click.echo('Hello {}!'.format(name))
