# -*- coding: utf-8 -*-
#
#  This file is part of Bioconvert software
#
#  Copyright (c) 2017 - Bioconvert Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/biokit/bioconvert
#  documentation: http://bioconvert.readthedocs.io
#
##############################################################################
"""NEXUS2PHYLIP conversion"""
import os

import colorlog
from Bio import SeqIO

from bioconvert import ConvBase, extensions

_log = colorlog.getLogger(__name__)


__all__ = ['NEXUS2PHYLIP']


class NEXUS2PHYLIP(ConvBase):
    """
    Converts a sequence alignment from :term:`NEXUS` format to :term:`PHYLIP` format. ::
    """

    def __init__(self, infile, outfile=None, alphabet=None, *args, **kwargs):
        """.. rubric:: constructor

        :param str infile: input :term:`NEXUS` file.
        :param str outfile: (optional) output :term:`PHYLIP` file
        """
        super().__init__(infile, outfile)
        self.alphabet = alphabet
        self._default_method = 'goalign'

    def _method_goalign(self, threads=None, *args, **kwargs):
        """
        Convert :term:`NEXUS` interleaved file in :term:`PHYLIP` format using goalign tool.
        https://github.com/fredericlemoine/goalign

        :param threads: not used.
        """
        self.install_tool('goalign')
        cmd = 'goalign reformat phylip -i {infile} -o {outfile} -x'.format(
            infile=self.infile,
            outfile=self.outfile)
        self.execute(cmd)
