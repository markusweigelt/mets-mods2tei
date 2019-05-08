# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import click
from urllib.request import urlopen

from pkg_resources import resource_filename, Requirement

from mets_mods2teiHeader import Mets
from mets_mods2teiHeader import Tei

@click.command()
@click.argument('mets', required=True)
def cli(mets):
    """ METS: File containing or URL pointing to the METS/MODS XML to be converted """
    
    #
    # interpret mets argument
    try:
        f = urlopen(mets)
    except:
        f = open(mets, "rb")

    #
    # read in METS
    mets = Mets.read(f)

    #
    # create TEI (from skeleton)
    tei = Tei()

    #
    # replace skeleton values by real ones
    tei.set_main_title(mets.get_main_title())

    click.echo(tei.tostring())


if __name__ == '__main__':
    cli()
