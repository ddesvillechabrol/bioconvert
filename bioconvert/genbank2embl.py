

# -*- coding: utf-8 -*-
##############################################################################
#  This file is part of Bioconvert software
#
#  Copyright (c) 2017 - Bioconvert Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/biokit/bioconvert
#  documentation: http://bioconvert.readthedocs.io
##############################################################################
""" description """

from bioconvert import ConvBase, extensions

__all__ = ["GENBANK2EMBL"]


class GENBANK2EMBL(ConvBase):
    """Convert :term:`GENBANK` file to :term:`EMBL` file

    Some description.

    """

    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input GENBANK file
        :param str outfile: output EMBL filename

        """
        super(GENBANK2EMBL, self).__init__(infile, outfile, *args, **kargs)

        self._default_method = "biopython"

    def _method_squizz(self, *args, **kwargs):
        """Header is less informative than the one obtained with biopython"""
        cmd = "squizz {} -f genbank -c embl > {} ".format(self.infile, self.outfile)
        self.execute(cmd)

    def _method_biopython(self, *args, **kwargs):
        from Bio import SeqIO
        SeqIO.convert(self.infile, "genbank", self.outfile, "embl")
