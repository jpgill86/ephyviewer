import os
import sys

from ephyviewer.myqt import QT_MODE
print('QT_MODE', QT_MODE)


def make_resources_icons():
    with open('icons.qrc','w') as f:
        f.write("""<!DOCTYPE RCC><RCC version="1.0">
    <qresource>
""")
        for p, d, files in os.walk('./'):
            for filename in files:
                if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.svg'):
                    f.write('            <file alias="%s">%s/%s</file>\r\n' % (filename, p[2:],filename) )

        f.write("""    </qresource>
</RCC>
""")

    if QT_MODE=='PyQt4':
        if sys.version_info > (3,):
            os.popen('pyrcc4 -py3 icons.qrc -o icons_py3_Qt4.py')
        else:
            os.popen('pyrcc4 icons.qrc -o icons_py2_Qt4.py')

    elif QT_MODE=='PyQt5':
        if sys.version_info > (3,):
            os.popen('pyrcc5  icons.qrc -o icons_py3.py')
        else:
            raise(NotImplementedError)


#------------------------------------------------------------------------------
if __name__ == '__main__' :
    make_resources_icons()
