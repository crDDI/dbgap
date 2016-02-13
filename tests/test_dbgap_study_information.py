# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
import os

from dict_compare import dict_compare
from dbgap.dbgap_study_information import *


def data_dir(fn: str) -> str:
    return os.path.join('data', fn)


class StudyInformationTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(
            dict_compare({'studyid': 'phs00001', 'versionedid': 'phs00001.v1', 'fullid': 'phs00001.v1.p1'},
                         StudyIdentifier(1, 1, 1).identifiers))


class DBGaPStudyInformationTestCase(unittest.TestCase):
    def test_get_information(self):
        self.assertEqual(open(data_dir('phs001007.xml')).read(),
                         get_study_information(StudyIdentifier(1007, 1, 1)))

    def test_biocaddie_json(self):
        raw_json = jsonasobj.loads(open(data_dir('phs001007.json')).read())
        s = biocaddie_json(raw_json, ['pht003897.v1', 'pht003898.v1', 'pht003899.v1', 'pht003900.v1'])._as_dict
        self.assertTrue(dict_compare(jsonasobj.loads(open(data_dir('phs001007.biocaddie.json')).read())._as_dict, s))


if __name__ == '__main__':
    unittest.main()
