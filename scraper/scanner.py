# Python program to explain os.scandir() method
# After scanning directory, files will be automatically be uploaded to s3
# Then deleted from directory

# importing os module
import os
import glob




def scan_files():
    path = '/'
    obj = os.scandir(path)
    print("Files and Directories in '% s':" % path)
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            print(entry.name)
    obj.close()


def delete_pdfs():
    files = glob.glob('/*.pdf', recursive=True)

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
