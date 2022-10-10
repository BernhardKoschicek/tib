from tib.data.images.volumes import tib11, tib14, tib16, tib17, tib18
from tib.data.images.subprojects import borderzones, digtib, holdura, \
    montenegro

IMAGES_TIB = tib11 + tib14 + tib16 + tib17 + tib18
IMAGES_SUB = montenegro + borderzones + digtib + holdura
IMAGES = IMAGES_TIB + IMAGES_SUB

