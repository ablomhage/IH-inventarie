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

'''
Created on 12 maj 2011

@author: Andreas Blomhage <a.blomhage@gmail.com>
'''

import gui.templates.object as objecttemplate
import gui.errordialogs as errdlg
import dbhandler

#TODO: Add Classdocumentation
class ObjectAdd(objecttemplate.TemplateObject):
    def __init__(self, parent, id, title):
        objecttemplate.TemplateObject.__init__(self, parent, id, title)
        
    def OnSave( self, event ):
        objectID = self.tcID.GetValue()
        if(objectID):
            owner = self.cbOwner.GetValue()
#            if(owner):
            myownerdb = dbhandler.OwnerDB()
            owner = myownerdb.RetriveOwnerID(owner)
#            owner = owner[0]
    
            description = self.tcDescription.GetValue()
            measurement = self.tcMeasurement.GetValue()
            rent = self.tcPrice.GetValue()
            repairs = self.tcRepairs.GetValue()
#            storage = self.cbStorage.GetSelection()
            storage = self.cbStorage.GetValue()
            
            nationality = self.cbNationality.GetValue()
            availability = self.cbAvailability.GetSelection()
            type = self.cbType.GetValue()
            
            mydb = dbhandler.ObjectsDB()
            try:
                mydb.InsertObject((objectID, type, measurement, description, owner, storage, availability, repairs, rent, nationality,))
            
                self.tcID.Clear()
                self.tcDescription.Clear()
                self.tcMeasurement.Clear()
                self.tcPrice.Clear()
                self.tcPrice.Disable()
                self.tcRepairs.Clear()

                self.cbStorage.SetSelection(-1)
                self.cbAvailability.SetSelection(-1)
                self.cbOwner.SetSelection(-1)
                self.cbNationality.SetSelection(-1)
                self.cbType.SetSelection(-1)
                
            except dbhandler.IntegrityError:
                #TODO: Needs a way to distinguise between a Null error and a unique error
                errdlg.ErrDlgUniqueID(self)
        else:
                errdlg.ErrDlgMissingID(self)
            
        
