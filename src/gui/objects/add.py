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

import wx
import dbhandler

ID_LEND  = wx.NewId()
ID_CHANGEID  = wx.NewId()
ID_CHANGETYPE = wx.NewId()

class ObjectAdd(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(500,300))
        self.__InitUI()
        self.Centre()
        self.Show()

    def __InitUI(self):
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=7)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        types = dbhandler.ObjectTypesDB().RetriveTypesSorted()
        owners = dbhandler.OwnerDB().RetriveListOfOwners()

        #=======================================================================
        # Object-ID
        #=======================================================================
        textID          = wx.StaticText(self, label="ObjektID: ")
        self.tcID           = wx.TextCtrl(self, wx.ID_ANY, size=(150,-1))
        grid.Add(textID, pos=(0,0))
        grid.Add(self.tcID, pos=(0,1))
        
        #=======================================================================
        # Type
        #=======================================================================
        textType = wx.StaticText(self, label="Objekttyp: ")
        self.cbType = wx.ComboBox(self, -1, choices=types, style=wx.CB_READONLY)

        grid.Add(textType, pos=(0,2))
        grid.Add(self.cbType, pos=(0,3))
        
        #=======================================================================
        # Measurement
        #=======================================================================
        textMeasurement     = wx.StaticText(self, label=u"Mått/antal/sidor: ")
        self.tcMeasurement  = wx.TextCtrl(self, wx.ID_ANY, size=(150, -1))

        grid.Add(textMeasurement, pos=(1,0))
        grid.Add(self.tcMeasurement, pos=(1,1))
        
        #=======================================================================
        # Nationality
        #=======================================================================
        textNationality     = wx.StaticText(self, label="Nationalitet: ")
        nationality = dbhandler.NationalityDB().RetriveNationalities()
        self.cbNationality = wx.ComboBox(self, -1, choices=nationality, style=wx.CB_READONLY)

        grid.Add(textNationality, pos=(1,2))
        grid.Add(self.cbNationality, pos=(1,3))
        
        #=======================================================================
        # Owner
        #=======================================================================
        textOwner     = wx.StaticText(self, label=u"Ägare: ")
        self.cbOwner = wx.ComboBox(self, -1, choices=owners, style=wx.CB_READONLY)
        
        grid.Add(textOwner, pos=(2,0))
        grid.Add(self.cbOwner, pos=(2,1))
        
        #=======================================================================
        # Storage
        #=======================================================================
        textStorage     = wx.StaticText(self, label=u"Förvaringsplats: ")
        self.tcStorage  = wx.TextCtrl(self, wx.ID_ANY, size=(150, -1))

        grid.Add(textStorage, pos=(2,2))
        grid.Add(self.tcStorage, pos=(2,3))
        
        #=======================================================================
        # Rent
        #=======================================================================
        textRent     = wx.StaticText(self, label="Uthyrningspris: ")
        self.tcRent  = wx.TextCtrl(self, wx.ID_ANY, size=(150, -1))

        grid.Add(textRent, pos=(3,0))
        grid.Add(self.tcRent, pos=(3,1))
        
        #=======================================================================
        # Rented
        #=======================================================================
#        textRented     = wx.StaticText(self, label="Uthyrd till: ")
#        self.tcRented  = wx.TextCtrl(self, wx.ID_ANY, size=(150, -1), style=wx.TE_READONLY)
#        #Make a special thing here.
#        self.tcRented.Enable(False)
#        grid.Add(textRented, pos=(3,2))
#        grid.Add(self.tcRented, pos=(3,3))
        
        
        #=======================================================================
        # Description
        #=======================================================================
        textDescription = wx.StaticText(self, label=u"Benämning: ")
        self.tcDescription  = wx.TextCtrl(self, wx.ID_ANY, size=(150, 90), style=wx.TE_MULTILINE)

        grid.Add(textDescription, pos=(4,0))
        grid.Add(self.tcDescription, pos=(4,1))
        
        #=======================================================================
        # Repairs
        #=======================================================================
        textRepairs = wx.StaticText(self, label="Reparationsbehov: ")
        self.tcRepairs  = wx.TextCtrl(self, wx.ID_ANY, size=(150, 90), style=wx.TE_MULTILINE)

        grid.Add(textRepairs, pos=(4,2))
        grid.Add(self.tcRepairs, pos=(4,3))

        btClose = wx.Button(self, wx.ID_CLOSE, u"Stäng")
        btSave  = wx.Button(self, wx.ID_SAVE, "Spara")

        buttons = wx.BoxSizer(wx.HORIZONTAL)
        
        buttons.Add(btSave, wx.RIGHT)
        buttons.Add(btClose, wx.RIGHT)
        


        self.Bind(wx.EVT_BUTTON, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, id=wx.ID_CLOSE)
        
        hSizer.Add(grid, 0, wx.ALL, 5)

        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(buttons, 0, wx.ALIGN_RIGHT)
        self.SetSizerAndFit(mainSizer)
        
        
    def OnQuit( self, event ):
        self.Close()
        
    def OnSave( self, event ):
        objectID = self.tcID.GetValue()
        if(objectID):
            owner = self.cbOwner.GetValue()
            if(owner):
                myownerdb = dbhandler.OwnerDB()
                owner = myownerdb.get_owner_id(owner)
        
                owner = owner[0]
        
                description = self.tcDescription.GetValue()
                measurement = self.tcMeasurement.GetValue()
                rent = self.tcRent.GetValue()
                repairs = self.tcRepairs.GetValue()
                storage = self.tcStorage.GetValue()
        
                nationality = self.cbNationality.GetValue()
        
                type = self.cbType.GetValue()
                
                mydb = dbhandler.ObjectsDB()
                mydb.insert_into_table((objectID, type, measurement, description, owner, storage, 0, repairs, rent, nationality,))
                

                self.tcID.Clear()
                self.tcDescription.Clear()
                self.tcMeasurement.Clear()
                self.tcRent.Clear()
                self.tcRepairs.Clear()
                self.tcStorage.Clear()

                self.cbNationality.Clear()
                self.cbOwner.Clear()
                self.cbType.Clear()
            else:
                dlg = wx.MessageDialog(self, u"En ägare av objektet måste anges innan en sparning kan ske. Vänligen ange en och försök igen.",
                              u"ägare saknas", wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, u"Objektets identifikationsnummer saknas, vänligen ange detta och försök igen.",
                              u"ObjektID behövs", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        
        

