import os
import shutil


'''
This script can walk recursively in the subfolders and copy all png files to a folder and rename them by serial number.
It also prepares a csv file that will have new id (serial number) to existing file name mapping.
Old table has information with the full nested directory path and labels etc. to which we can join this new csv for full
information.
'''

ROOTDIR = "./final_data/data/"
DESTDIR = "./new_data/"


if __name__ == '__main__':
    counter = 1
    with open(os.path.join(DESTDIR, 'filename_id_lookup.csv'), 'a') as dest:
        for folder, subs, files in os.walk(ROOTDIR):
            for filename in files:
                if '.png' in filename:
                    shutil.copyfile(os.path.join(folder, filename), os.path.join(DESTDIR, str(counter) + ".png"))
                    dest.write(f"{counter},{filename},{os.path.join(folder, filename)[13:]}\n")
                    counter += 1
