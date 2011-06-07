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
__date__ ="$2011-mar-28 10:47:23$"

import dbhandler
import addpersonbase
import wx

class AddOwnerDialog(addpersonbase.AddBase):
    def __init__(self, parent, id, title):
        addpersonbase.AddBase.__init__(self, parent, id, title)

    def OnSave(self, event):
        company = self.tc_company.GetValue()
        contact = self.tc_contact.GetValue()
        if(company or contact):
            address = self.tc_address.GetValue()
            postal     = self.tc_postal.GetValue()
            town    = self.tc_town.GetValue()
            phone   = self.tc_phone.GetValue()
            mobile  = self.tc_mobile.GetValue()
            email   = self.tc_email.GetValue()
            insert = (company, contact, address, postal, town, phone, mobile, email)

            mydb = dbhandler.OwnerDB()

            mydb.insert_into_table(insert)

            self.tc_company.Clear()
            self.tc_contact.Clear()
            self.tc_address.Clear()
            self.tc_postal.Clear()
            self.tc_town.Clear()
            self.tc_phone.Clear()
            self.tc_mobile.Clear()
            self.tc_email.Clear()
        else:
            dlg = wx.MessageDialog(self, u"Företagets, föreningens eller privatpersonens namn saknas, vänligen åtgärda detta.",
                              "Namn saknas", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
# End of class AddOwnerDialog
