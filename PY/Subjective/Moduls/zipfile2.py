import os
import zipfile

fantasy_zip = zipfile.ZipFile('C:\\Users\\ASUS\\Documents\\PY\\Project\\Test\\Backup.zip', 'w')

for folder, subfolders, files in os.walk('/Project/Test'):

    for file in files:
        if file.endswith('.txt'):
            fantasy_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), '/Project/Test'),
                              compress_type=zipfile.ZIP_DEFLATED)