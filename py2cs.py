#!/usr/bin/python3

import os, re

d = "py-codes" # https://github.com/avian2/unidecode/tree/master/unidecode
print("working...")

fp = open("unidecode_native.c", "w")
fp.write('''char *buffer[503][256] =
{\n''')


def formatch(ch, cc):
    if (ch == None):
        return 'a'
    if ch == "":
        return ""
    # ch = ch.replace("\r", "")
    ch = ch.replace("\\", "\\\\")
    ch = ch.replace("\"", "\\\"")
    ch = ch.replace("%", "%%")
    ch = ch.replace("\n", "")
    ch = ch.replace("\r", "")
    # return ch if cc > 31 else "\\u" + ('%x' % cc).rjust(4, '0')
    return ch if cc > 31 else ""

prev = 0
for file in [file for file in os.listdir(d) if not file in [".", ".."]]:
    m = re.search('x(.{3})\.py$', file)
    if m:
        data = __import__(d + "." + file[0:-3], [], [], ['data']).data
        missing = 256 - len(data)
        if missing != 0:
            fill = "[?]" if data[-1] == "[?]" else ""
            data += (fill,)*missing
        assert len(data) == 256
        c = 0
        row = (int(m.group(1), 16))
        num = int(m.group(1), 16) * 256

        if prev != row:
            for i in range(prev + 1, row):
                fp.write('    /* (%s) */ { 0 }, \n' % i)

        fp.write('    /* %s */ { ' % row)

        for ch in data:
            fp.write('"%s" %s' % (
                formatch(ch, num + c),
                "," if c < 255 else ""))
            c = c + 1

        fp.write(' },\n')
        prev = row

fp.write('''};

char *Lookup(int high, int low)
{
    if (high >= 503)
    {
        return "";
    }

    if (buffer[high] == 0)
    {
        return "";
    }

    return buffer[high][low];
}
''')
print("converted!")

