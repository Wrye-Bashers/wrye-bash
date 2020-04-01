# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#  This file is part of Wrye Bash.
#
#  Wrye Bash is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  Wrye Bash is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Wrye Bash; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2020 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================
"""This module lists the files installed in the Data folder in a completely
vanilla Fallout 3 setup."""

#--Every file in the Data directory from Bethsoft
vanilla_files = {
    # Section 1: Vanilla files
    u'Credits.txt',
    u'CreditsWacky.txt',
    u'Fallout3.esm',
    u'Fallout - MenuVoices.bsa',
    u'Fallout - Meshes.bsa',
    u'Fallout - Misc.bsa',
    u'Fallout - Sound.bsa',
    u'Fallout - Textures.bsa',
    u'Fallout - Voices.bsa',
    u'LODSettings\\aaaForgotten1.DLODSettings',
    u'LODSettings\\aaaForgotten4.DLODSettings',
    u'LODSettings\\aaaForgotten5.DLODSettings',
    u'Music\\Base\\Base_01.mp3',
    u'Music\\Base\\Base_02.mp3',
    u'Music\\Base\\Base_03.mp3',
    u'Music\\Base\\Base_04.mp3',
    u'Music\\Battle\\Battle_01.mp3',
    u'Music\\Battle\\Battle_02.mp3',
    u'Music\\Battle\\Battle_03.mp3',
    u'Music\\Battle\\Battle_04.mp3',
    u'Music\\Battle\\Battle_05.mp3',
    u'Music\\Battle\\Battle_06.mp3',
    u'Music\\Battle\\Battle_07.mp3',
    u'Music\\Battle\\Finale\\Battle_01.mp3',
    u'Music\\Battle\\Finale\\Battle_02.mp3',
    u'Music\\Battle\\Finale\\Battle_03.mp3',
    u'Music\\Battle\\Finale\\Battle_04.mp3',
    u'Music\\Battle\\Finale\\Battle_05.mp3',
    u'Music\\Battle\\Finale\\Battle_06.mp3',
    u'Music\\Battle\\Finale\\Battle_07.mp3',
    u'Music\\Dungeon\\Dungeon_01.mp3',
    u'Music\\Dungeon\\Dungeon_02.mp3',
    u'Music\\Dungeon\\Dungeon_03.mp3',
    u'Music\\Dungeon\\Dungeon_04.mp3',
    u'Music\\Dungeon\\Dungeon_05.mp3',
    u'Music\\Endgame\\Endgame_01.mp3',
    u'Music\\Endgame\\Endgame_02.mp3',
    u'Music\\Endgame\\Endgame_03.mp3',
    u'Music\\Endgame\\Endgame_04.mp3',
    u'Music\\Endgame\\Endgame_05.mp3',
    u'Music\\Endgame\\Endgame_06.mp3',
    u'Music\\Endgame\\Endgame_07.mp3',
    u'Music\\Endgame\\Endgame_08.mp3',
    u'Music\\Endgame\\Endgame_09.mp3',
    u'Music\\Endgame\\Endgame_11.mp3',
    u'Music\\Endgame\\Endgame_12.mp3',
    u'Music\\Endgame\\Endgame_14.mp3',
    u'Music\\Endgame\\Endgame_15.mp3',
    u'Music\\Endgame\\Endgame_17.mp3',
    u'Music\\Endgame\\Endgame_18.mp3',
    u'Music\\Endgame\\Endgame_19.mp3',
    u'Music\\Explore\\Explore_01.mp3',
    u'Music\\Explore\\Explore_02.mp3',
    u'Music\\Explore\\Explore_03.mp3',
    u'Music\\Explore\\Explore_04.mp3',
    u'Music\\Explore\\Explore_05.mp3',
    u'Music\\Explore\\Explore_06.mp3',
    u'Music\\Explore\\Explore_07.mp3',
    u'Music\\Public\\Public_01.mp3',
    u'Music\\Public\\Public_02.mp3',
    u'Music\\Public\\Public_03.mp3',
    u'Music\\Public\\Public_04.mp3',
    u'Music\\Public\\Public_05.mp3',
    u'Music\\Special\\Death.mp3',
    u'Music\\Special\\ExitTheVault.mp3',
    u'Music\\Special\\MainTitle.mp3',
    u'Music\\Special\\Success.mp3',
    u'Music\\Tension\\Tension_01.mp3',
    u'Music\\TranquilityLane\\MUS_TranquilityLane_01_LP.mp3',
    u'Music\\TranquilityLane\\MUS_TranquilityLane_02_LP.mp3',
    u'Shaders\\shaderpackage002.sdp',
    u'Shaders\\shaderpackage003.sdp',
    u'Shaders\\shaderpackage004.sdp',
    u'Shaders\\shaderpackage006.sdp',
    u'Shaders\\shaderpackage007.sdp',
    u'Shaders\\shaderpackage009.sdp',
    u'Shaders\\shaderpackage010.sdp',
    u'Shaders\\shaderpackage011.sdp',
    u'Shaders\\shaderpackage012.sdp',
    u'Shaders\\shaderpackage013.sdp',
    u'Shaders\\shaderpackage014.sdp',
    u'Shaders\\shaderpackage015.sdp',
    u'Shaders\\shaderpackage016.sdp',
    u'Shaders\\shaderpackage017.sdp',
    u'Shaders\\shaderpackage018.sdp',
    u'Shaders\\shaderpackage019.sdp',
    u'Video\\1 year later.bik',
    u'Video\\2 weeks later.bik',
    u'Video\\3 years later.bik',
    u'Video\\6 years later.bik',
    u'Video\\9 years later.bik',
    u'Video\\B01.bik',
    u'Video\\B02.bik',
    u'Video\\B03.bik',
    u'Video\\B04.bik',
    u'Video\\B05.bik',
    u'Video\\B06.bik',
    u'Video\\B07.bik',
    u'Video\\B08.bik',
    u'Video\\B09.bik',
    u'Video\\B10.bik',
    u'Video\\B11.bik',
    u'Video\\B12.bik',
    u'Video\\B13.bik',
    u'Video\\B14.bik',
    u'Video\\B15.bik',
    u'Video\\B16.bik',
    u'Video\\B17.bik',
    u'Video\\B18.bik',
    u'Video\\B19.bik',
    u'Video\\B20.bik',
    u'Video\\B21.bik',
    u'Video\\B22.bik',
    u'Video\\B23.bik',
    u'Video\\B24.bik',
    u'Video\\B25.bik',
    u'Video\\B26.bik',
    u'Video\\B27.bik',
    u'Video\\B28.bik',
    u'Video\\B29.bik',
    u'Video\\Fallout INTRO Vsk.bik',
    # Section 2: DLCs
    u'anchorage.esm',
    u'anchorage - main.bsa',
    u'anchorage - sounds.bsa',
    u'thepitt.esm',
    u'thepitt - main.bsa',
    u'thepitt - sounds.bsa',
    u'brokensteel.esm',
    u'brokensteel - main.bsa',
    u'brokensteel - sounds.bsa',
    u'pointlookout.esm',
    u'pointlookout - main.bsa',
    u'pointlookout - sounds.bsa',
    u'zeta.esm',
    u'zeta - main.bsa',
    u'zeta - sounds.bsa',
    u'DLCList.txt',
}
