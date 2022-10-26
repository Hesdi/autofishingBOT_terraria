import zipfile

source = 'C:\\Users\\ASUS\\Documents\\PY\\Project\\Test\\lalao.txt'
jungle_zip = zipfile.ZipFile('C:\\Users\\ASUS\\Documents\\PY\\Project\\Test\\Backup.zip', 'w')
jungle_zip.write(source, compress_type=zipfile.ZIP_DEFLATED)