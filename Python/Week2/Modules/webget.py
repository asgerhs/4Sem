import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    filename = os.path.basename(url)
    if(os.path.isfile(filename)):
        print("File already exists.")
        
    else:
        if(to == None):
            local_filename = req.urlretrieve(url, './' + url.split('/')[-1])
        else:
            local_filename = req.urlretrieve(url, to)
    
    
    
    
