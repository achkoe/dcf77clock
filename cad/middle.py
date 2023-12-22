"""Make boxex for CNC.
"""
from pyx import *

unit.set(defaultunit="mm")

if __name__ == '__main__':
    lw = 0.1
    c = canvas.canvas()

    hi = 35
    bi = 150

    if 1:
        p = path.path()
        #p.append(path.moveto(0, 0))
        p.append(path.moveto(-bi/2, -hi/2))
        p.append(path.rlineto(0, hi))
        p.append(path.rlineto(bi, 0))
        p.append(path.rlineto(0, -hi))
        p.append(path.rlineto(-bi, 0))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue])

    c.writeSVGfile("middle.svg")
    c.writeEPSfile("middle.eps")
    c.writePDFfile("middle.pdf")
