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
Created on 26 aug 2011

@author: Andreas Blomhage <a.blomhage@gmail.com>
'''
import wx

ID_SEARCH       = wx.NewId()

class MainSearchUI ( wx.Dialog ):
    
    def __init__( self, parent ):
        print("searchinit")
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 280,390 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        sizerMain = wx.BoxSizer( wx.VERTICAL )
        
        self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerPanelMain1 = wx.BoxSizer( wx.VERTICAL )
        
        sizerContent = wx.BoxSizer( wx.VERTICAL )
        
        self.panelObjects = wx.Panel( self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.textObjectOwner = wx.StaticText( self.panelObjects, wx.ID_ANY, u"Ägare:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textObjectOwner.Wrap( -1 )
        fgSizer1.Add( self.textObjectOwner, 0, wx.ALL, 5 )
        
        self.tcObjectOwner = wx.TextCtrl( self.panelObjects, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer1.Add( self.tcObjectOwner, 0, wx.ALL, 5 )
        
        self.textStorage = wx.StaticText( self.panelObjects, wx.ID_ANY, u"Förvaring:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textStorage.Wrap( -1 )
        fgSizer1.Add( self.textStorage, 0, wx.ALL, 5 )
        
        self.tcStorage = wx.TextCtrl( self.panelObjects, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer1.Add( self.tcStorage, 0, wx.ALL, 5 )
        
        self.textPrice = wx.StaticText( self.panelObjects, wx.ID_ANY, u"Pris (min/max):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textPrice.Wrap( -1 )
        fgSizer1.Add( self.textPrice, 0, wx.ALL, 5 )
        
        self.tcPriceMin = wx.TextCtrl( self.panelObjects, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer1.Add( self.tcPriceMin, 0, wx.ALL, 5 )
        
        
        fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.tcPriceMax = wx.TextCtrl( self.panelObjects, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer1.Add( self.tcPriceMax, 0, wx.ALL, 5 )
        
        bSizer10.Add( fgSizer1, 0, wx.EXPAND|wx.ALL, 5 )
        
        fgSizer4 = wx.FlexGridSizer( 2, 2, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.panelObjects, wx.ID_ANY, u"Tillgänglighet" ), wx.VERTICAL )
        
        self.m_checkBox1 = wx.CheckBox( self.panelObjects, wx.ID_ANY, u"Till salu", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )
        
        self.m_checkBox2 = wx.CheckBox( self.panelObjects, wx.ID_ANY, u"Uthyres", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )
        
        fgSizer4.Add( sbSizer1, 1, wx.EXPAND, 5 )
        
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.panelObjects, wx.ID_ANY, u"Diverse" ), wx.VERTICAL )
        
        self.m_checkBox3 = wx.CheckBox( self.panelObjects, wx.ID_ANY, u"Utlånad", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_checkBox3, 0, wx.ALL, 5 )
        
        self.m_checkBox4 = wx.CheckBox( self.panelObjects, wx.ID_ANY, u"Behov av reparation", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_checkBox4, 0, wx.ALL, 5 )
        
        fgSizer4.Add( sbSizer2, 1, wx.EXPAND, 5 )
        
        bSizer10.Add( fgSizer4, 0, wx.EXPAND|wx.ALL, 5 )
        
        fgSizer5 = wx.FlexGridSizer( 2, 2, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.textTypes = wx.StaticText( self.panelObjects, wx.ID_ANY, u"Typer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textTypes.Wrap( -1 )
        fgSizer5.Add( self.textTypes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice2Choices = []
        self.m_choice2 = wx.Choice( self.panelObjects, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        fgSizer5.Add( self.m_choice2, 0, wx.ALL, 5 )
        
        bSizer10.Add( fgSizer5, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.panelObjects.SetSizer( bSizer10 )
        self.panelObjects.Layout()
        bSizer10.Fit( self.panelObjects )
        sizerContent.Add( self.panelObjects, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.panelOwners = wx.Panel( self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panelOwners.Hide()
        
        fgSizer6 = wx.FlexGridSizer( 2, 2, 0, 0 )
        fgSizer6.SetFlexibleDirection( wx.BOTH )
        fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.textFirstName = wx.StaticText( self.panelOwners, wx.ID_ANY, u"Förnamn:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textFirstName.Wrap( -1 )
        fgSizer6.Add( self.textFirstName, 0, wx.ALL, 5 )
        
        self.tcFirstName = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcFirstName, 0, wx.ALL, 5 )
        
        self.textLastname = wx.StaticText( self.panelOwners, wx.ID_ANY, u"Efternamn:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textLastname.Wrap( -1 )
        fgSizer6.Add( self.textLastname, 0, wx.ALL, 5 )
        
        self.tcLastName = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcLastName, 0, wx.ALL, 5 )
        
        self.textStreet = wx.StaticText( self.panelOwners, wx.ID_ANY, u"Gatuadress:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textStreet.Wrap( -1 )
        fgSizer6.Add( self.textStreet, 0, wx.ALL, 5 )
        
        self.tcAddress = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcAddress, 0, wx.ALL, 5 )
        
        self.textZip = wx.StaticText( self.panelOwners, wx.ID_ANY, u"Postnummer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textZip.Wrap( -1 )
        fgSizer6.Add( self.textZip, 0, wx.ALL, 5 )
        
        self.tcZip = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcZip, 0, wx.ALL, 5 )
        
        self.textCity = wx.StaticText( self.panelOwners, wx.ID_ANY, u"Ort:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textCity.Wrap( -1 )
        fgSizer6.Add( self.textCity, 0, wx.ALL, 5 )
        
        self.tcTown = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcTown, 0, wx.ALL, 5 )
        
        self.textPhone = wx.StaticText( self.panelOwners, wx.ID_ANY, u"Telefonnummer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textPhone.Wrap( -1 )
        fgSizer6.Add( self.textPhone, 0, wx.ALL, 5 )
        
        self.tcPhone = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcPhone, 0, wx.ALL, 5 )
        
        self.textMobile = wx.StaticText( self.panelOwners, wx.ID_ANY, u"Mobilnummer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textMobile.Wrap( -1 )
        fgSizer6.Add( self.textMobile, 0, wx.ALL, 5 )
        
        self.tcMobile = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcMobile, 0, wx.ALL, 5 )
        
        self.textEmail = wx.StaticText( self.panelOwners, wx.ID_ANY, u"E-mail:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textEmail.Wrap( -1 )
        fgSizer6.Add( self.textEmail, 0, wx.ALL, 5 )
        
        self.tcEmail = wx.TextCtrl( self.panelOwners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer6.Add( self.tcEmail, 0, wx.ALL, 5 )
        
        self.panelOwners.SetSizer( fgSizer6 )
        self.panelOwners.Layout()
        fgSizer6.Fit( self.panelOwners )
        sizerContent.Add( self.panelOwners, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.panelLoaners = wx.Panel( self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panelLoaners.Hide()
        
        fgSizer61 = wx.FlexGridSizer( 2, 2, 0, 0 )
        fgSizer61.SetFlexibleDirection( wx.BOTH )
        fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.textFirstName1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"Förnamn:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textFirstName1.Wrap( -1 )
        fgSizer61.Add( self.textFirstName1, 0, wx.ALL, 5 )
        
        self.tcFirstName1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcFirstName1, 0, wx.ALL, 5 )
        
        self.textLastname1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"Efternamn:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textLastname1.Wrap( -1 )
        fgSizer61.Add( self.textLastname1, 0, wx.ALL, 5 )
        
        self.tcLastName1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcLastName1, 0, wx.ALL, 5 )
        
        self.textStreet1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"Gatuadress:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textStreet1.Wrap( -1 )
        fgSizer61.Add( self.textStreet1, 0, wx.ALL, 5 )
        
        self.tcAddress1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcAddress1, 0, wx.ALL, 5 )
        
        self.textZip1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"Postnummer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textZip1.Wrap( -1 )
        fgSizer61.Add( self.textZip1, 0, wx.ALL, 5 )
        
        self.tcZip1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcZip1, 0, wx.ALL, 5 )
        
        self.textCity1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"Ort:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textCity1.Wrap( -1 )
        fgSizer61.Add( self.textCity1, 0, wx.ALL, 5 )
        
        self.tcTown1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcTown1, 0, wx.ALL, 5 )
        
        self.textPhone1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"Telefonnummer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textPhone1.Wrap( -1 )
        fgSizer61.Add( self.textPhone1, 0, wx.ALL, 5 )
        
        self.tcPhone1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcPhone1, 0, wx.ALL, 5 )
        
        self.textMobile1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"Mobilnummer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textMobile1.Wrap( -1 )
        fgSizer61.Add( self.textMobile1, 0, wx.ALL, 5 )
        
        self.tcMobile1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcMobile1, 0, wx.ALL, 5 )
        
        self.textEmail1 = wx.StaticText( self.panelLoaners, wx.ID_ANY, u"E-mail:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textEmail1.Wrap( -1 )
        fgSizer61.Add( self.textEmail1, 0, wx.ALL, 5 )
        
        self.tcEmail1 = wx.TextCtrl( self.panelLoaners, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer61.Add( self.tcEmail1, 0, wx.ALL, 5 )
        
        self.panelLoaners.SetSizer( fgSizer61 )
        self.panelLoaners.Layout()
        fgSizer61.Fit( self.panelLoaners )
        sizerContent.Add( self.panelLoaners, 1, wx.EXPAND |wx.ALL, 5 )
        
        sizerPanelMain1.Add( sizerContent, 1, wx.EXPAND, 5 )
        
        sizerButtons = wx.BoxSizer( wx.HORIZONTAL )
        
        
        sizerButtons.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        
        rbSearchOptionsChoices = [ u"Objekt", u"Ägare", u"Låntagare" ]
        self.rbSearchOptions = wx.RadioBox( self.panelMain, wx.ID_ANY, u"Sökalternativ", wx.DefaultPosition, wx.DefaultSize, rbSearchOptionsChoices, 1, wx.RA_SPECIFY_COLS )
        self.rbSearchOptions.SetSelection( 0 )
        bSizer7.Add( self.rbSearchOptions, 0, wx.ALL, 5 )
        
        sizerButtons.Add( bSizer7, 0, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.buttonSearch = wx.Button( self.panelMain, ID_SEARCH, u"Sök", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.buttonSearch, 0, wx.ALL, 5 )
        
        self.buttonCancel = wx.Button( self.panelMain, wx.ID_CLOSE, u"Avbryt", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonCancel.SetDefault() 
        bSizer8.Add( self.buttonCancel, 0, wx.ALL, 5 )
        
        self.Bind(wx.EVT_BUTTON, self.OnSearch, id=ID_SEARCH)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, id=wx.ID_CLOSE)
        self.rbSearchOptions.Bind(wx.EVT_RADIOBOX, self.OnChange)
        
        sizerButtons.Add( bSizer8, 0, wx.EXPAND, 5 )
        
        sizerPanelMain1.Add( sizerButtons, 0, wx.EXPAND, 5 )
        
        self.panelMain.SetSizer( sizerPanelMain1 )
        self.panelMain.Layout()
        sizerPanelMain1.Fit( self.panelMain )
        sizerMain.Add( self.panelMain, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.SetSizer( sizerMain )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.Show()
    
    def __del__( self ):
        pass
    
    def HidePanel(self, panel):
        if panel.IsShown():
            panel.Hide()
            
    def ShowPanel(self, panel):
        if not panel.IsShown():
            panel.Show()
    
    def OnChange(self, event):
        item = event.GetSelection()
        
        if item == 1:
            self.HidePanel(self.panelObjects)
            self.HidePanel(self.panelLoaners)
            self.ShowPanel(self.panelOwners)
        elif item == 2:
            self.HidePanel(self.panelObjects)
            self.HidePanel(self.panelOwners)
            self.ShowPanel(self.panelLoaners)
        else:
            self.HidePanel(self.panelLoaners)
            self.HidePanel(self.panelOwners)
            self.ShowPanel(self.panelObjects)
            
    
    def OnQuit( self, event ):
        self.Close()
        
    def OnSearch(self, event):
        selection = self.rbSearchOptions.GetSelection()
        
        if selection == 1:
            pass
        elif selection == 2:
            pass
        else:
            owner = self.tcObjectOwner.GetValue()
            
            print owner

