# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
import click


@click.group()
@click.option('--verbose', is_flag=True, help="Will print verbose message")
@click.pass_context
def main(context, verbose):
    """
    A simple CLI calculator
    """
    if verbose:
        click.echo("Starting operation...")
    context.obj = {
        'verbose': verbose,
    }


@main.command()
@click.argument('first-addend', type=int)
@click.argument('second-addend', type=int)
@click.pass_context
def add(context, first_addend, second_addend):
    """
    Adds two number
    """
    if context.obj['verbose']:
        click.echo("Adding {} and {}...".format(first_addend, second_addend))
    click.echo(first_addend + second_addend)


@main.command()
@click.argument('minuend', type=int)
@click.argument('subtrahend', type=int)
@click.pass_context
def subtract(context, minuend, subtrahend):
    """
    Subtracts two number
    """
    if context.obj['verbose']:
        click.echo("Subtracting {} and {}...".format(minuend, subtrahend))
    click.echo(minuend - subtrahend)


@main.command()
@click.argument('first-factor', type=int)
@click.argument('second-factor', type=int)
@click.pass_context
def multiply(context, first_factor, second_factor):
    """
    Multiplies two number
    """
    if context.obj['verbose']:
        click.echo("Multiplying {} and {}...".format(first_factor, second_factor))
    click.echo(first_factor * second_factor)


@main.command()
@click.argument('dividend', type=int)
@click.argument('divisor', type=int)
@click.option('--floor', is_flag=True, help="Implements floor division")
@click.pass_context
def divide(context, dividend, divisor, floor):
    """
    Divides two number
    """
    if context.obj['verbose']:
        click.echo("Dividing {} and {}...".format(dividend, divisor))
    if floor:
        click.echo(dividend // divisor)
    else:
        click.echo(dividend / divisor)
