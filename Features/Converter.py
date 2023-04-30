import os
import time
from Features.Nasa import NasaNews
def DateConvt(Query):
    Date = Query.replace(" january ","-01-")
    Date = Date.replace(" february ","-02-")
    Date = Date.replace(" march ","-03-")
    Date = Date.replace(" april ","-04-")
    Date = Date.replace(" may ","-05-")
    Date = Date.replace(" june ","-06-")
    Date = Date.replace(" july ","-07-")
    Date = Date.replace(" august ","-08-")
    Date = Date.replace(" september ","-09-")
    Date = Date.replace(" october ","-10-")
    Date = Date.replace(" november ","-11-")
    Date = Date.replace(" december ","-12-")
    # Date = Date.replace(" st ","")
    # Date = Date.replace(" nd ","")
    # Date = Date.replace(" rd ","")
    # Date = Date.replace(" th ","")
    Date = Date.replace(" ","")
    return str(Date)

# NasaNews("Date")

    