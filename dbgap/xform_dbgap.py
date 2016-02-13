# Copyright (c) 2016, Mayo Clinic
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
import jsonasobj
from dbgap.constants import *

# context = jsonasobj.load(open(os.path.join(os.path.dirname(__file__), '..', 'static', 'json', 'context.json')))
context = jsonasobj.loads('{"@context": "http://localhost:8080/json/context.json"}')
dimension_type_map = {'string': 'xsd:string'}


def xform_dbgap_dimension(inp: jsonasobj.JsonObj) -> None:
        inp['@type'] = BIOCADDIE + "Dimension"
        inp['@id'] = BIOCADDIE + inp.id
        inp['identifierInfo'] = [{'identifier': DBGAP + inp.id,
                                  'identifierScheme': 'dbgap'}]
        if 'type' in inp and inp.type in dimension_type_map:
            inp['dimensionType'] = dimension_type_map[inp.type]
            del inp['type']


def xform_dbgap_dataset(inp: jsonasobj.JsonObj) -> jsonasobj.JsonObj:
    if 'data_table' not in inp:
        print("HERE")
    inp.data_table['@id'] = BIOCADDIE + inp.data_table.study_id
    inp.data_table.identifierInfo = [{'identifier': DBGAP + inp.data_table.study_id,
                                      'identifierScheme': 'dbgap'}]
    inp.data_table.date_info = [{'date': inp.data_table.date_created,
                                 'dateType': 'dct:created'}]
    inp.data_table['@type'] = BIOCADDIE + "Dataset"
    [xform_dbgap_dimension(v) for v in inp.data_table.variable]
    inp.data_table['hasPartDimension'] = [DBGAP + v.id for v in inp.data_table.variable]

    # Add the context the resulting JSON
    inp['@context'] = context['@context']
    return inp

