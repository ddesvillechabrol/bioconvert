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
""" description """
import os
import colorlog
from Bio import SeqIO

from bioconvert import ConvBase, extensions

_log = colorlog.getLogger(__name__)


class FASTA2CLUSTAL(ConvBase):
    """
    Converts a sequence alignment from :term:`FASTA` format to :term:`CLUSTAL` format::

        converter = FASTA2CLUSTAL(infile, outfile)
        converter(method='biopython')

    default method = biopython
    available methods = biopython, squizz
    """

    def __init__(self, infile, outfile=None, alphabet=None, *args, **kwargs):
        """.. rubric:: constructor

        :param str infile: input :term:`FASTA` file.
        :param str outfile: (optional) output :term:`CLUSTAL` file
        """
        super().__init__(infile, outfile)
        self.alphabet = alphabet
        self._default_method = 'biopython'

    def _method_biopython(self, threads=None):
        """
        Convert :term:`FASTA` interleaved file in :term:`CLUSTAL` format using biopython.

        :param threads: not used
        """
        sequences = list(SeqIO.parse(self.infile, "fasta", alphabet=self.alphabet))
        count = SeqIO.write(sequences, self.outfile, "clustal")
        _log.info("Converted %d records to clustal" % count)

    def _method_squizz(self, threads=None):
        """
        Convert :term:`FASTA` file in :term:`CLUSTAL` format using squizz tool.

        :param threads: not used
        """
        cmd = 'squizz -c CLUSTAL {infile} > {outfile}'.format(
            infile=self.infile,
            outfile=self.outfile)
        self.execute(cmd)
