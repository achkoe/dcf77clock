"""Make boxex for CNC.
"""
from pyx import *

unit.set(defaultunit="mm")

if __name__ == '__main__':
    lw = 0.1
    c = canvas.canvas()

    ha = 145
    ba = 150

    bi = 70
    hi = 70


    if 1:
        p = path.path()
        p.append(path.moveto(-bi/2, -hi/2))
        p.append(path.rlineto(0, hi))
        p.append(path.rlineto(bi, 0))
        p.append(path.rlineto(0, -hi))
        p.append(path.rlineto(-bi, 0))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue])

        p = path.path()
        p.append(path.moveto(-bi/2 - 1, -hi/2 - 1))
        p.append(path.rlineto(0, hi + 2))
        p.append(path.rlineto(bi + 2, 0))
        p.append(path.rlineto(0, -hi - 2))
        p.append(path.rlineto(-bi - 2, 0))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue])

        p = path.path()
        p.append(path.moveto(15, -95))
        p.append(path.rlineto(+30, 0))
        p.append(path.rlineto(0, 145))
        p.append(path.rlineto(-150, 0))
        p.append(path.rlineto(0, -30))
        p.append(path.closepath())
        c.stroke(p, [style.linewidth(lw), color.rgb.red])

        p = path.path()
        p.append(path.moveto(-105, 20))
        p.append(path.lineto(15, -95))
        p.append(path.rlineto(-10, 0))
        p.append(path.lineto(-105, 10))
        p.append(path.rlineto(0, 10))
        c.stroke(p, [style.linewidth(lw), color.rgb.blue])


    c.writeSVGfile("antenna2.svg")
    c.writeEPSfile("antenna2.eps")
    c.writePDFfile("antenna2.pdf")
