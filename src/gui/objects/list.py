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
# -*- coding: UTF-8 -*-
'''
Created on 10 maj 2011

@author: Andreas Blomhage
'''

import gui.templates.list as listtmpl
import gui.objects.info as objectinfo
import dbhandler

class ObjectList(listtmpl.ListTmpl):
    def __init__(self, parent):
        listtmpl.ListTmpl.__init__(self, parent)

    def FetchData(self):
        try:
            self.SetColumns([u"ID", u"Benämning", u"Typ", u"Ägare", u"Förvaringsplats"])
            self.SetColumnWidth([50, -1, 100, 100, 100]) 
            self.SetItems(dict(enumerate(dbhandler.ObjectsDB().RetriveSpecificObjectData("objectid, description, type, owner, storage"))))
        except:
            self.SetItems({ })
            print("Error retriving object data from database")
            
    def PopulateList(self):
        self.DefineListHeader()
        items = self.GetItems().items()
        for key, data in items:
            owner = dbhandler.OwnerDB().RetriveOwner(data[3])
#            data = data[:3] + (owner,data[4:],)
            tmpdata = list(data)
            tmpdata[3] = owner
            data = tuple(tmpdata)
            self.AppendListItem(key, data)

        self.currentItem = 0

    def OnDoubleClick(self, event):
        dlg = objectinfo.ObjectInfo(self, -1, "Information", self.listCtrl.GetItemText(self.currentItem))
        event.Skip()

