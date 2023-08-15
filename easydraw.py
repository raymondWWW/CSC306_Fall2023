# Just a wrapper for drawSVG that uses global variables so that things are simplified a bit
!pip install drawSvg==1.2.2 numpy==1.21.1

import drawSvg as dSVG

def easydraw(*args,**kwargs):
    global drawSVG_easydraw
    drawSVG_easydraw = dSVG.Drawing(*args, **kwargs)

def Text(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Text(*args, **kwargs))

def Rectangle(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Rectangle(*args, **kwargs))

def Circle(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Circle(*args, **kwargs))

def Ellipse(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Ellipse(*args, **kwargs))

def ArcLine(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.ArcLine(*args, **kwargs))

def Path(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Path(*args, **kwargs))

def Lines(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Lines(*args, **kwargs))

def Line(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Line(*args, **kwargs))

def Arc(*args, **kwargs):
    drawSVG_easydraw.append(dSVG.Arc(*args, **kwargs))

def show_me_my_drawing():
    return drawSVG_easydraw
