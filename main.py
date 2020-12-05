# -*- coding: utf-8 -*-

from resources.lib import kodilogging
# from resources.lib import plugin

import logging
import xbmcaddon
import xbmcgui

# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
kodilogging.config()

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
line1 = "HOLA MUNDO"
xbmcgui.Dialog().ok(__addonname__,line1)

#plugin.run()


