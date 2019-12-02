import os

print("## مذكرات الشيخ شعبان علي في علم التجويد")
EXTS_TO_DISPLAY = [".pdf", ".docx", ".doc", ]

FILES_TO_EXCLUDE = [".DS_Store"]
DIRS_TO_EXCLUDE = ["pdfs", ".git"]
def list_files_in_dir(fpath):
    my_files = [os.path.splitext(p)[0] for p in os.listdir(fpath) if not os.path.isdir(p)]
    return set([x for x in my_files if x not in FILES_TO_EXCLUDE])

def list_dirs_in_dir(fpath):
    my_dirs = [x for x in os.listdir(".") if os.path.isdir(x)]
    return set([x for x in my_dirs if x not in DIRS_TO_EXCLUDE])

def fix_filenames_with_space(flist):
    # fix names with space
    for f in flist:
        for ext in EXTS_TO_DISPLAY:
            fpath = "{}{}".format(f, ext)
            if os.path.exists(fpath) and " " in fpath:
                os.rename(fpath, fpath.replace(" ", "_"))

def fix_dirnames_with_space(dlist):
    # fix names with space
    for fpath in dlist:
        if os.path.exists(fpath) and " " in fpath:
            os.rename(fpath, fpath.replace(" ", "_"))
                

file_names = list_files_in_dir(".")
directories = list_dirs_in_dir(".")

fix_filenames_with_space(file_names)
fix_dirnames_with_space(directories)

# get the new names
#file_names = set([os.path.splitext(p)[0] for p in os.listdir(".")])

current_working_dir = os.getcwd()
file_names = list_files_in_dir(".")
# change working dir using os.chdir()

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

# for d in directories:
#     dpath = "./{}".format(d)
#     file_names = list_files_in_dir(dpath)
#     fix_filenames_with_space(file_names)