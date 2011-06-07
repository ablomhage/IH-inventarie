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
__author__="Andreas"
__date__ ="$2011-mar-17 11:31:23$"

from setuptools import setup,find_packages
import py2exe

setup (
  name = 'IH Inventarie',
  version = '0.2',
  packages = find_packages(),
  windows=["main.py"],
  # Declare your packages' dependencies here, for eg:
  #install_requires=['foo>=3'],

  options = {"py2exe": {"compressed": 1,
            "optimize": 2,
            "ascii": 0,
            "includes":["dbhash"],
            "bundle_files": 1}},

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'Andreas Sundin',
  author_email = '',

  summary = 'Inventory database for Interaktiv Historia',
  url = '',
  license = 'BSD',
  long_description= 'Long description of the package',

  # could also include long_description, download_url, classifiers, etc.

  
)
