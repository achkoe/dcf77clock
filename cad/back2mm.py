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
        c.stroke(p, [style.linewidth(lw), color.rgb.red, trafo.mirror(0)])
        #c.stroke(p, [style.linewidth(lw), color.rgb.blue])

        p = path.path()
        p.append(path.moveto(-bi/2, -hi/2))
        p.append(path.moveto(-bi/2 + 8, -8.5))
        p.append(path.rlineto(-8, 0))
        p.append(path.rlineto(0, 12))
        p.append(path.rlineto(8, 0))
        p.append(path.rlineto(0, -12))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue, trafo.mirror(0)])

        p = path.path()
        p.append(path.moveto(-bi/2, -hi/2))
        p.append(path.moveto(29, +hi/2))
        p.append(path.rlineto(8, 0))
        p.append(path.rlineto(0, -2.5))
        p.append(path.rlineto(-8, 0))
        p.append(path.rlineto(0, 2.5))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue, trafo.mirror(0)])

        p = path.path()
        p.append(path.moveto(-bi/2, -hi/2))
        p.append(path.moveto(55, -hi/2 + 5))
        p.append(path.rlineto(7, 0))
        p.append(path.rlineto(0, 10))
        p.append(path.rlineto(-7, 0))
        p.append(path.rlineto(0, -10))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue, trafo.mirror(0)])

        p = path.circle(55 + 3.5, -hi/2 + 5 + 5, 2.5)
        c.stroke(p, [style.linewidth(lw), color.rgb.blue, trafo.mirror(0)])

    c.writeSVGfile("back2mm.svg")
    c.writeEPSfile("back2mm.eps")
    c.writePDFfile("back2mm.pdf")
