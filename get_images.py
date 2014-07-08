# -*- coding: utf-8 -*-


import json
import asciitable

def skip_bad_lines(self, str_vals, ncols):  
  """Simply ignore every line with the wrong number of columns."""  
    
  print 'Skipping line:', ' '.join(str_vals)  
  return None  

def get_iss_photos():
    """
    Gets public photos from ISS missions and provide data input for tasks
    :arg string size: Size of the image from ISS mission
    :returns: A list of photos.
    :rtype: list
    http://eol.jsc.nasa.gov/sseop/images/ESC/small/ISS030/ISS030-E-67805.JPG
    """
    photos = []

    #asciitable.BaseReader.inconsistent_handler = skip_bad_lines 
    lista=asciitable.read('atlasOfNight.csv',guess=False,delimiter=",")
    
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
#print get_iss_photos()
