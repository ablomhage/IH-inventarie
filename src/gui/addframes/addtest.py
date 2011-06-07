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
__date__ ="$2011-mar-28 10:43:24$"

import wx
import wx.lib.intctrl
import string
import exception

class ValidateContact(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        return ValidateContact()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        print(text)

        if len(text) == 0:
            wx.MessageBox("En kontakt måste finnas angiven!", "Error")
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            #raise ValueError("Missing contact")
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True


    def TransferToWindow(self):
        """ Transfer data from validator to window.

             The default implementation returns False, indicating that an error
             occurred.  We simply return True, as we don't do any data transfer.
         """
        return True # Prevent wxDialog from complaining.


    def TransferFromWindow(self):
        """ Transfer data from window to validator.

             The default implementation returns False, indicating that an error
             occurred.  We simply return True, as we don't do any data transfer.
         """
        return True # Prevent wxDialog from complaining.

# End of class ValidateContact

class ValidatePhone(wx.PyValidator):
    def __init__(self, flag):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)


    def Clone(self): # Required method for validator
        return ValidatePhone(self.flag)
    def TransferToWindow(self):
        return True # Prevent wxDialog from complaining.
    def TransferFromWindow(self):
        return True # Prevent wxDialog from complaining.
    def Validate(self, win):
        return True

    def OnChar(self, event):
        keycode = int(event.GetKeyCode())
        if keycode < 256:
            #print keycode
            key = chr(keycode)
            #print key
            if self.flag == 'no-alpha' and key in string.letters:
                return
            if self.flag == 'no-digit' and key in string.digits:
                return
        event.Skip()

# End of class ValidatePhone

class AddBase(wx.Dialog):
    savedata=()
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title)
        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui(self):
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        self.SetAutoLayout(True)
        VSPACE = 10

        company = wx.StaticText(self, label="Företag/Förening")
        contact = wx.StaticText(self, label="Kontakt")
        address = wx.StaticText(self, label="Gatuadress")
        postal  = wx.StaticText(self, label="Postnummer")
        town    = wx.StaticText(self, label="Ort")
        phone   = wx.StaticText(self, label="Telefonnummer")
        mobile  = wx.StaticText(self, label="Mobilnummer")
        email   = wx.StaticText(self, label="E-mail")

        self.tc_company  = wx.TextCtrl(self, wx.ID_ANY)
        self.tc_contact  = wx.TextCtrl(self, wx.ID_ANY, "", validator = ValidateContact())
        self.tc_address  = wx.TextCtrl(self, wx.ID_ANY)
        self.tc_postal   = wx.lib.intctrl.IntCtrl(self, wx.ID_ANY, max=99999, limited=True)
        self.tc_town     = wx.TextCtrl(self, wx.ID_ANY)
        self.tc_phone    = wx.TextCtrl(self, wx.ID_ANY, validator = ValidatePhone('no-alpha'))
        self.tc_mobile   = wx.TextCtrl(self, wx.ID_ANY)
        self.tc_email    = wx.TextCtrl(self, wx.ID_ANY)

        fgs = wx.FlexGridSizer(cols=2)

        #fgs.Add((1,1));

        #Company
        fgs.Add(company, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_company)

        fgs.Add((1,VSPACE)); fgs.Add((1,VSPACE))

        #Contact
        fgs.Add(contact, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_contact)

        fgs.Add((1,VSPACE)); fgs.Add((1,VSPACE))

        #Address
        fgs.Add(address, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_address)

        #Postal
        fgs.Add(postal, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_postal)

        #Town
        fgs.Add(town, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_town)

        #Phone
        fgs.Add(phone, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_phone)

        #Mobile
        fgs.Add(mobile, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_mobile)

        #E-mail
        fgs.Add(email, 0, wx.ALIGN_LEFT|wx.CENTER)
        fgs.Add(self.tc_email)

        buttons = wx.StdDialogButtonSizer() #wx.BoxSizer(wx.HORIZONTAL)
        b = wx.Button(self, wx.ID_SAVE, "Save")
        b.SetDefault()
        buttons.AddButton(b)
        buttons.AddButton(wx.Button(self, wx.ID_CANCEL, "Cancel"))
        buttons.Realize()

        self.Bind(wx.EVT_BUTTON, self.OnSave, id=wx.ID_SAVE)

        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(fgs, 1, wx.GROW|wx.ALL, 25)
        border.Add(buttons, 0, wx.GROW|wx.BOTTOM, 5)
        self.SetSizer(border)
        border.Fit(self)
        self.Layout()
        
        
        #self.Bind(wx.EVT_BUTTON, self.OnQuit, id=wx.ID_CANCEL)

    def return_values(self):
        company = self.tc_company.GetValue()
        contact = self.tc_contact.GetValue()
        address = self.tc_address.GetValue()
        postal  = self.tc_postal.GetValue()
        town    = self.tc_town.GetValue()
        phone   = self.tc_phone.GetValue()
        mobile  = self.tc_mobile.GetValue()
        email   = self.tc_email.GetValue()
        insert = (company, contact, address, postal, town, phone, mobile, email)
        return insert

    def OnSave(self, event):
        #Doesn't seem to work to raise an exception in the validator, so we need to do it like this instead.
        if(not self.Validate()):
            raise ValueError("Missing contact")
#        try:
#            self.Validate()
#        except ValueError:
#            print "Error caught"
#            raise ValueError("Missing contact")
        

    def OnQuit(self, event):
        self.Close()

# End of class AddBase
