﻿


__version__ = "0.2021.3.17"



from .LessC import LessC

def lessc(minify:bool = False):
	return LessC(minify)
#

