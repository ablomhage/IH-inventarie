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
__author__="Andreas Sundin"
__date__ ="$2011-mar-28 10:45:03$"

import dbhandler
import wx

class AddObjectDialog(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(550,275),
            style=(wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(4, 10)

        mytypedb = dbhandler.ObjectTypesDB()
        myownerdb = dbhandler.OwnerDB()
        types = mytypedb.RetriveTypesSorted()
        owners = myownerdb.RetriveListOfOwners()
        nationalities = dbhandler.NationalityDB().RetriveNationalities()

        #Object-ID
        objectid = wx.StaticText(panel, label="ObjektID")
        self.tc_objectid = wx.TextCtrl(panel, wx.ID_ANY)
        sizer.Add(objectid, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.tc_objectid, pos=(0, 1), span=(1, 2),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #Type
        type = wx.StaticText(panel, label="Typ")
        self.cb_type = wx.ComboBox(panel, -1, choices=types, style=wx.CB_READONLY)
        sizer.Add(type, pos=(0, 4), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.cb_type, pos=(1, 4), span=(1, 1),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #Owner
        owner = wx.StaticText(panel, label=u"Ägare")
        self.cb_owner = wx.ComboBox(panel, -1, choices=owners, style=wx.CB_READONLY)
        sizer.Add(owner, pos=(2, 4), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.cb_owner, pos=(3, 4), span=(1, 2),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #Description
        description = wx.StaticText(panel, label=u"Benämning")
        self.tc_description = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE)
        sizer.Add(description, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.tc_description, pos=(1,1), span=(4, 3),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #Measurement
        measurement = wx.StaticText(panel, label=u"Mått/sidor/antal")
        self.tc_measurement = wx.TextCtrl(panel, wx.ID_ANY)
        sizer.Add(measurement, pos=(4, 4), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.tc_measurement, pos=(4,5), span=(1, 1),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #Repairs
        self.chb_repairs = wx.CheckBox(panel, label="Reparationer")
        self.tc_repairs = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE)
        sizer.Add(self.chb_repairs, pos=(5, 0))
        sizer.Add(self.tc_repairs, pos=(5,1), span=(3, 3),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #Description
        storage = wx.StaticText(panel, label=u"Förvaringsplats")
        self.tc_storage = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE)
        sizer.Add(storage, pos=(5, 4), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.tc_storage, pos=(5,5), span=(3, 3),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #Nationalities
        nationality = wx.StaticText(panel, label="Nationalitet")
        self.cb_nationality = wx.ComboBox(panel, -1, choices=nationalities, style=wx.CB_READONLY)
        sizer.Add(nationality, pos=(0, 5), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.cb_nationality, pos=(1, 5), span=(1, 1),
            flag=wx.TOP, border=5)

        #Rent
        rent = wx.StaticText(panel, label="Uthyrespris")
        self.tc_rent = wx.TextCtrl(panel, wx.ID_ANY)
        sizer.Add(rent, pos=(8, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(self.tc_rent, pos=(8,1), span=(1, 1),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        buttonOk = wx.Button(panel, wx.ID_SAVE, size=(90, 28))
        buttonClose = wx.Button(panel, wx.ID_EXIT, size=(90, 28))
        sizer.Add(buttonOk, pos=(8, 5))
        sizer.Add(buttonClose, pos=(8, 6), flag=wx.RIGHT|wx.BOTTOM, border=5)

        self.Bind(wx.EVT_BUTTON, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, id=wx.ID_EXIT)

        #sizer.AddGrowableCol(1)
        #sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)

    def OnSave(self, event):
        objectid = self.tc_objectid.GetValue()
        if(objectid):
            owner = self.cb_owner.GetValue()
            if(owner):


                myownerdb = dbhandler.OwnerDB()
                owner = myownerdb.get_owner_id(owner)

                owner = owner[0]

                description = self.tc_description.GetValue()
                measurement = self.tc_measurement.GetValue()
                rent = self.tc_rent.GetValue()
                repairs = self.tc_repairs.GetValue()
                storage = self.tc_storage.GetValue()

                nationality = self.cb_nationality.GetValue()

                type = self.cb_type.GetValue()

                repairsneeded = self.chb_repairs.GetValue()

                
                mydb = dbhandler.ObjectsDB()
                mydb.insert_into_table((objectid, type, measurement, description, owner, storage, repairsneeded, repairs, rent, nationality,))
                

                self.tc_objectid.Clear()
                self.tc_description.Clear()
                self.tc_measurement.Clear()
                self.tc_rent.Clear()
                self.tc_repairs.Clear()
                self.tc_storage.Clear()

                self.cb_nationality.Clear()
                self.cb_owner.Clear()
                self.cb_type.Clear()

                self.chb_repairs.SetValue(False)
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

    def OnQuit(self, event):
        self.Close()

# End of class AddObjectDialog
