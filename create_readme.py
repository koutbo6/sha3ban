import os

print("## مذكرات الشيخ شعبان علي في علم التجويد")
EXTS_TO_DISPLAY = [".pdf", ".docx", ".doc", ]
file_names = set([os.path.splitext(p)[0] for p in os.listdir(".")])

# fix names with space
for f in file_names:
    for ext in EXTS_TO_DISPLAY:
        fpath = "{}{}".format(f, ext)
        if os.path.exists(fpath) and " " in fpath:
            os.rename(fpath, fpath.replace(" ", "_"))

# get the new names
file_names = set([os.path.splitext(p)[0] for p in os.listdir(".")])

# create readme
for f in file_names:
    for ext in EXTS_TO_DISPLAY:
        fpath = "{}{}".format(f, ext)
        if os.path.exists(fpath):
            print('- {} [{}]({})'.format(
                f.replace("-", " ").replace("_", " "),
                ext[1:],
                fpath))
            break
