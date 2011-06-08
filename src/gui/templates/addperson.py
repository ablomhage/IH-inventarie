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
__author__ = "Andreas Blomhage"
__date__ = "$2011-mar-28 10:43:24$"

import wx
import wx.lib.intctrl
import string

class ValidateContact( wx.PyValidator ):
    def __init__( self ):
        wx.PyValidator.__init__( self )

    def Clone( self ):
        return ValidateContact()

    def Validate( self, win ):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        if len( text ) == 0:
            wx.MessageBox( u"En kontakt måste finnas angiven!", "Error" )
            textCtrl.SetBackgroundColour( "pink" )
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour( 
                wx.SystemSettings_GetColour( wx.SYS_COLOUR_WINDOW ) )
            textCtrl.Refresh()
            return True


    def TransferToWindow( self ):
        """ Transfer data from validator to window.
    
            The default implementation returns False, indicating that an error
            occurred.  We simply return True, as we don't do any data transfer.
        """
        return True # Prevent wxDialog from complaining.
    
    
    def TransferFromWindow( self ):
        """ Transfer data from window to validator.
    
            The default implementation returns False, indicating that an error
            occurred.  We simply return True, as we don't do any data transfer.
        """
        return True # Prevent wxDialog from complaining.


class ValidatePhone( wx.PyValidator ):
    def __init__( self, flag ):
        wx.PyValidator.__init__( self )
        self.flag = flag
        self.Bind( wx.EVT_CHAR, self.OnChar )


    def Clone( self ): # Required method for validator
        return ValidatePhone( self.flag )
    def TransferToWindow( self ):
        return True # Prevent wxDialog from complaining.
    def TransferFromWindow( self ):
        return True # Prevent wxDialog from complaining.
    def Validate( self, win ):
        return True

    def OnChar( self, event ):
        keycode = int( event.GetKeyCode() )
        if keycode < 256:
            #print keycode
            key = chr( keycode )
            #print key
            if self.flag == 'no-alpha' and key in string.letters:
                return
            if self.flag == 'no-digit' and key in string.digits:
                return
        event.Skip()

# End of class ValidatePhone

class AddTemplate( wx.Frame ):
    savedata = ()
    def __init__( self, parent, id, title ):
        wx.Frame.__init__( self, parent, id, title, size = ( 400, 400 ),
        style = ( wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN ) )
        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui( self ):

        self.SetExtraStyle( wx.WS_EX_VALIDATE_RECURSIVELY )

        panel = wx.Panel( self )

        sizer = wx.GridBagSizer( 6, 9 )

        company = wx.StaticText( panel, label = u"Företag/Förening" )
        contact = wx.StaticText( panel, label = "Kontakt" )
        address = wx.StaticText( panel, label = "Gatuadress" )
        postal = wx.StaticText( panel, label = "Postnummer" )
        town = wx.StaticText( panel, label = "Ort" )
        phone = wx.StaticText( panel, label = "Telefonnummer" )
        mobile = wx.StaticText( panel, label = "Mobilnummer" )
        email = wx.StaticText( panel, label = "E-mail" )

        self.tc_company = wx.TextCtrl( panel, wx.ID_ANY )
        self.tc_contact = wx.TextCtrl( panel, wx.ID_ANY, validator = ValidateContact() )
        self.tc_address = wx.TextCtrl( panel, wx.ID_ANY )
        self.tc_postal = wx.lib.intctrl.IntCtrl( panel, wx.ID_ANY, max = 99999, limited = True )
        self.tc_town = wx.TextCtrl( panel, wx.ID_ANY )
        self.tc_phone = wx.TextCtrl( panel, wx.ID_ANY, validator = ValidatePhone( 'no-alpha' ) )
        self.tc_mobile = wx.TextCtrl( panel, wx.ID_ANY )
        self.tc_email = wx.TextCtrl( panel, wx.ID_ANY )



        sizer.Add( company, pos = ( 0, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_company, pos = ( 0, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        sizer.Add( contact, pos = ( 1, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_contact, pos = ( 1, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        sizer.Add( address, pos = ( 2, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_address, pos = ( 2, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        sizer.Add( postal, pos = ( 3, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_postal, pos = ( 3, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        sizer.Add( town, pos = ( 4, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_town, pos = ( 4, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        sizer.Add( phone, pos = ( 5, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_phone, pos = ( 5, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        sizer.Add( mobile, pos = ( 6, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_mobile, pos = ( 6, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        sizer.Add( email, pos = ( 7, 0 ), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5 )
        sizer.Add( self.tc_email, pos = ( 7, 2 ), span = ( 1, 3 ),
            flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 5 )

        buttonOk = wx.Button( panel, wx.ID_SAVE, size = ( 90, 28 ) )
        buttonClose = wx.Button( panel, wx.ID_EXIT, size = ( 90, 28 ) )
        sizer.Add( buttonOk, pos = ( 9, 3 ) )
        sizer.Add( buttonClose, pos = ( 9, 4 ), flag = wx.RIGHT | wx.BOTTOM, border = 5 )

        self.Bind( wx.EVT_BUTTON, self.OnSave, id = wx.ID_SAVE )
        self.Bind( wx.EVT_BUTTON, self.OnQuit, id = wx.ID_EXIT )

        sizer.AddGrowableCol( 1 )
        sizer.AddGrowableRow( 2 )
        panel.SetSizerAndFit( sizer )

    def OnQuit( self, event ):
        self.Close()

# End of class AddBase

