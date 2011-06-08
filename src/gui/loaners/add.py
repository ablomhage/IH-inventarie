# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Copyright (c) 2011, Andreas Blomhage
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Andreas Blomhage BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
__author__="Andreas Blomhage"
__date__ ="$2011-mar-28 11:24:45$"

import dbhandler
#import addtest
import gui.templates.addperson as addperson
import exception
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('ih_example')

class AddLoanerDialog(addperson.AddTemplate):
    def __init__(self, parent, id, title):
        addperson.AddTemplate.__init__(self, parent, id, title)

    def OnSave(self, event):
        try:
            if(not addperson.AddTemplate.OnSave(self, event)):
                print "Trying"
        except ValueError, e:
            log.info('Missing contact')
        else:
            print "No exception"
            insert = super(AddLoanerDialog, self).return_values()
            print insert

            mydb = dbhandler.LoanerDB()
            mydb.insert_into_table(insert)


# End of class AddLoanerDialog
