"""Make boxex for CNC.
"""
from pyx import *

unit.set(defaultunit="mm")

if __name__ == '__main__':
    lw = 0.1
    c = canvas.canvas()
    x, y = 0, 0
    ha = 35
    ba = 151

    hi = 29
    bi = 133

    if 0:
        p = path.path()
        p.append(path.moveto(0, 0))
        p.append(path.rlineto(ba, 0))
        p.append(path.rlineto(0, ha))
        p.append(path.rlineto(-ba, 0))
        p.append(path.rlineto(0, -ha))

        c.stroke(p, [style.linewidth(lw), color.rgb.blue])

    if 1:
        p = path.path()
        #p.append(path.moveto(0, 0))
        p.append(path.moveto(-bi/2, -hi/2))
        p.append(path.rlineto(0, hi))
        p.append(path.rlineto(bi, 0))
        p.append(path.rlineto(0, -hi))
        p.append(path.rlineto(-bi, 0))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue])

    c.writeSVGfile("front.svg")
    c.writeEPSfile("front.eps")
    c.writePDFfile("front.pdf")
