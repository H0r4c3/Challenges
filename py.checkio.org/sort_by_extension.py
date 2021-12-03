'https://py.checkio.org/en/mission/sort-by-extension/'

'''
You are given a list of files. You need to sort this list by the file extension. The files with the same extension should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp".
Input: A list of filenames.

Output: A list of filenames.

os module not allowed!!!
'''

import re
from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    files1 = list()
    for item in files:
        if item.rsplit('.', 1)[0] == '':
            files1.append(item)
            files.remove(item)
            
    r = re.compile('\.\w+$')
    files.sort(key=lambda f: (re.findall(r, f), f.rsplit('.', 1)[0]))
    
    files1.sort()
    files1.extend(files)
    
    return files1


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))
    print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))
    print(sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']