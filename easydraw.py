# easydraw.py

# Ensure required packages are installed. In the Colab notebook, run:
# !pip install drawSvg==1.2.2 numpy==1.21.1

import drawSvg as dSVG

_drawSVG_easydraw = None

def _ensure_initialized():
    global _drawSVG_easydraw
    if _drawSVG_easydraw is None:
        raise Exception("Please initialize using easydraw() before drawing.")

def easydraw(*args, **kwargs):
    global _drawSVG_easydraw
    _drawSVG_easydraw = dSVG.Drawing(*args, **kwargs)

def Text(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Text(*args, **kwargs))

def Rectangle(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Rectangle(*args, **kwargs))

def Circle(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Circle(*args, **kwargs))

def Ellipse(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Ellipse(*args, **kwargs))

def ArcLine(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.ArcLine(*args, **kwargs))

def Path(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Path(*args, **kwargs))

def Lines(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Lines(*args, **kwargs))

def Line(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Line(*args, **kwargs))

def Arc(*args, **kwargs):
    _ensure_initialized()
    _drawSVG_easydraw.append(dSVG.Arc(*args, **kwargs))

def show_me_my_drawing():
    _ensure_initialized()
    return _drawSVG_easydraw
