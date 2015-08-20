#encoding: utf-8
def read_tranlated(fn):
    translated = {}
    for line in open(fn):
        line = line.rstrip()
        if not line:
            continue
        if line.startswith('\xef\xbb\xbf#'):
            continue
        if line.startswith(';'):
            continue
        if line.startswith('['):
            continue

        key, trans = line.split('=', 1)
        translated[key] = trans

    return translated


def merge(translated_file, new_template_file, merged_file):
    translated = read_tranlated(translated_file)
    fp = open(merged_file, 'w')
    fp.write('#NAME:简体中文 (Kommit 汉化)\n')
    cnt = 0
    for line in open(new_template_file):
        if not line.startswith(';'):
            fp.write(line)
            continue
        if line.startswith(';^'):
            fp.write(line)
            continue
        key = line[1:].split('=')[0]
        if key in translated:
            trans = translated[key]
            fp.write('%s=%s\n' % (key, trans))
            del translated[key]
            cnt += 1
        else:
            fp.write(line)

    print '%s merged' % cnt
    for k, v in translated.items():
        print k, v.decode('utf-8')
    fp.close()

if __name__ == '__main__':
    merge('zh_CN.ReaperLangPack.old', 'template_2015-03-23.ReaperLangPack', 'zh_CN.ReaperLangPack')
