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
Created on 12 maj 2011

@author: Andreas Blomhage <a.blomhage@gmail.com>
'''

import gui.templates.object as objecttemplate
import gui.errordialogs as errdlg
import dbhandler

#TODO: Add Classdocumentation
class ObjectEdit(objecttemplate.TemplateObject):
    def __init__(self, parent, id, title):
        objecttemplate.TemplateObject.__init__(self, parent, id, title)

    def PopulateFrame(self, object):
        self.__objectID = object[0]
        self.tcID.SetValue("" + object[0])
        self.tcMeasurement.SetValue(object[2])
        self.tcPrice.SetValue(str(object[8]))
        self.tcDescription.SetValue(object[3])
        self.tcRepairs.SetValue(object[7])
#        self.cbAvailability.SetStringSelection()
        self.cbStorage.SetStringSelection(object[5])
        self.cbNationality.SetStringSelection(object[9])
        self.cbOwner.SetStringSelection(object[4])
        self.cbType.SetStringSelection(object[1])
        
    def OnSave( self, event ):
        objectID = self.tcID.GetValue()
        if(objectID):
            owner = self.cbOwner.GetValue()
            myownerdb = dbhandler.OwnerDB()
            owner = myownerdb.RetriveOwnerID(owner)
    
            description = self.tcDescription.GetValue()
            measurement = self.tcMeasurement.GetValue()
            rent = self.tcPrice.GetValue()
            repairs = self.tcRepairs.GetValue()
            storage = self.cbStorage.GetSelection()
    
            nationality = self.cbNationality.GetValue()
    
            type = self.cbType.GetValue()
            
            mydb = dbhandler.ObjectsDB()
            mydb.UpdateObject(self.__objectID, (objectID, type, measurement, description, owner, storage, repairs, rent, nationality,))
            
            self.Parent.RefreshDialog(objectID)
            self.Close()
        else:
            errdlg.ErrDlgMissingID(self)
        
        

