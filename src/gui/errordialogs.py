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
Created on 28 jun 2011

@author: Andreas Blomhage <a.blomhage@gmail.com>
'''

import wx

class ErrDlgUniqueID(wx.MessageDialog):
    def __init__(self, parent):
        wx.MessageDialog.__init__(self, parent, u"Detta ID-nummer finns redan. Vänligen ange ett nytt och försök igen.",
                                  u"Dublett funnen", wx.OK | wx.ICON_INFORMATION)
        self.ShowModal()
        self.Destroy()
#End of class ErrDlgUnique

class ErrDlgMissingID(wx.MessageDialog):
    def __init__(self, parent):
        wx.MessageDialog.__init__(self, parent, u"Objektets identifikationsnummer saknas, vänligen ange detta och försök igen.",
                                  u"ID behövs", wx.OK | wx.ICON_INFORMATION)
        
        self.ShowModal()
        self.Destroy()
        
#End of class ErrDlgIDMissing

