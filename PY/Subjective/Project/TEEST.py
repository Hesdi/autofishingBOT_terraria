import os
from zipfile import ZipFile
import shutil


# Zip directory (Ref1)
def compress_directory(source_dir, output_filename, kind='zip'):
    shutil.make_archive(output_filename, kind, source)


# Zip multiple files (Ref2)

def zip_multiple_files(source_dir, target, extension=None):
    with ZipFile(target, 'w') as fzip:
        for folder, subfolders, files in os.walk(source_dir):
            for file in files:
                if extension and file.endswith(extension):
                    fzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), source_dir),
                               compress_type=zipfile.ZIP_DEFLATED)
                    continue
                fzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), source_dir),
                           compress_type=zipfile.ZIP_DEFLATED)
    return None


# Zip multiple files (Ref3)
def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

            # returning all file paths
    return file_paths


def zip_multiple_files2(source, target_filename):
    # path to folder which needs to be zipped
    directory = source

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

        # writing files to a zipfile
    with ZipFile(target_filename, 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

        print('All files zipped successfully!')