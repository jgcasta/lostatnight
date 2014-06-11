# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import json
import asciitable


def get_iss_photos():
    """
    Gets public photos from ISS missions
    :arg string size: Size of the image from ISS mission
    :returns: A list of photos.
    :rtype: list
    http://eol.jsc.nasa.gov/sseop/images/ESC/small/ISS030/ISS030-E-67805.JPG
    """
    photos = []
    lista=asciitable.read('datosISS.csv')

    for i in lista:
        tmpMission=i['ISS-ID'].split('-E-')
        mission = tmpMission[0]
        idIss = tmpMission[1]
        
        pattern_s = "http://eol.jsc.nasa.gov/sseop/images/ESC/%s/%s/%s-E-%s.JPG" % (
            "small",
            mission,
            mission,
            idIss)
        pattern_b = "http://eol.jsc.nasa.gov/sseop/images/ESC/%s/%s/%s-E-%s.JPG" % (
            'large',
            mission,
            mission,
            idIss)

        linkData = "http://eol.jsc.nasa.gov/scripts/sseop/photo.pl?mission=%s&roll=E&frame=%s" % (
            mission,
            idIss)
        idISS = idIss

        citylon2 = str(i['nlon'])

        citylat2 = str(i['nlat'])
        
        f = '50'
        
        tmp = dict(link_small=pattern_s,
                   link_big=pattern_b,
                   linkData=linkData,
                   idISS=idISS,
                   citylon=citylon2,
                   citylat=citylat2,
                   focal=f
                   )
        photos.append(tmp)
    return photos

#get_iss_photos()
