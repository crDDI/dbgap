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
import os
import unittest
import shutil
from dbgap.file_downloader import FileDownloader

single_file_template = 'dbgap/studies/%(study)s/%(fullname)s/GapExchange_%(fullname)s.xml'
directory_template = '/dbgap/studies/%(study)s/%(fullname)s/pheno_variable_summaries'


class FileDownloaderTestCase(unittest.TestCase):
    def test_dowload_single_file(self):
        study = 'phs001007'
        fullname = study + ".v1.p1"
        dld = FileDownloader('ftp.ncbi.nlm.nih.gov')
        self.assertEqual(open(os.path.join('data', 'phs001007.xml')).read(),
                         dld.download_file(single_file_template % dict(study=study, fullname=fullname)))

    def test_dir_download(self):
        test_dir = os.path.join('data', 'dltest')
        shutil.rmtree(test_dir, ignore_errors=True)
        os.makedirs(test_dir)
        study = 'phs000722'
        fullname = study + ".v1.p1"
        dld = FileDownloader('ftp.ncbi.nlm.nih.gov')
        self.assertEqual(4, dld.download_dir(directory_template % dict(study=study, fullname=fullname), test_dir,
                         name_map=lambda s: s.replace('.xml', '.tst'), file_filtr=lambda s: 'data_dict' in s))


if __name__ == '__main__':
    unittest.main()
