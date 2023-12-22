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
        p.append(path.moveto(-bi/2, -hi/2))
        p.append(path.rlineto(0, hi))
        p.append(path.rlineto(bi - 50, 0))
        p.append(path.rlineto(0, -5))
        p.append(path.rlineto(20, 0))
        p.append(path.rlineto(0, -30))
        p.append(path.rlineto(-120, 0))
        #p.append(path.rlineto(-bi, 0))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue, trafo.mirror(0)])
        #c.stroke(p, [style.linewidth(lw), color.rgb.blue])

    c.writeSVGfile("back6mm.svg")
    c.writeEPSfile("back6mm.eps")
    c.writePDFfile("back6mm.pdf")
