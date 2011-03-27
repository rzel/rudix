#!/usr/bin/env python
# Life is hard without documentation

import sys, os
import getopt

PkgContents = '''<?xml version="1.0"?>
<pkg-contents spec="1.12">
{contents}
</pkg-contents>
'''
F0 = '<f n="{name}-install" o="{owner}" g="{group}" p="{perms}" pt="{name}-install" m="false" t="file">'
F = '<f n="{node}" o="{owner}" g="{group}" p="{perms}">'

DefaultDirAttributes = {'owner': 'root', 'group': 'wheel', 'perms': 123}
DefaultFileAttributes = {'owner': 'root', 'group': 'wheel', 'perms': 123}
DefaultFileExecAtrtibutes = {'owner': 'root', 'group': 'wheel', 'perms': 123}

def output_pkgcontents(path, name):
    contents = []
    d = DefaultDirAttributes.copy()
    d['name'] = name
    contents.append('  ' + F0.format(**d))
#     for dirpath, dirnames, filenames in os.walk(path):
#         print dirpath, dirnames, filenames
    contents.append('  </f>')
    contents = '\n'.join(contents)
    return PkgContents.format(contents=contents)

def main(argv=None):
    if not argv:
        argv = sys.argv
    opts, args = getopt.getopt(argv[1:], 'n:', ['name='])
    for opt, arg in opts:
        if opt in ('-n', '--name'):
            name = arg
    try:
        path = args[0]
    except IndexError:
        path = '.'
    print output_pkgcontents(path, name)
    return 0

if __name__ == '__main__':
    sys.exit(main())
