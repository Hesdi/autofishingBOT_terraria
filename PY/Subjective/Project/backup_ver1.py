import os
import time
import zipfile
import keyboard

print('''Чтобы создать файл с комемнтариями нажмите 'Y' 
Чтобы создать файл без коментариев нажмите 'N' 
Чтобы выйти нажмите 'Esc' ''')

def Yes():
    source = input('\nПуть к файлу: ')
    comments = (input('Введите комементарии: '))
    target_dir = ('C:\\Users\\ASUS\\Documents\\PY\\Project\\Backups\\' +
                time.strftime('%Y{0}%m{0}%d{1}%H{2}%M{2}%S   ').format('_', '   ', '꞉') + comments + '.zip')
    target = zipfile.ZipFile('C:\\Users\\ASUS\\Documents\\PY\\Project\\Backups\\' +
                time.strftime('%Y{0}%m{0}%d{1}%H{2}%M{2}%S   ').format('_', '   ', '꞉') + comments + '.zip', 'w')
    for folder, subfolders, files in os.walk(source):
        for file in files:
            target.write(os.path.join(folder, file),
                         os.path.relpath(os.path.join(folder, file), source), compress_type=zipfile.ZIP_DEFLATED)
    print('Резервная копия успешно создана в ', target_dir)

def No():
    source = input('\nПуть к файлу: ')
    target_dir = ('C:\\Users\\ASUS\\Documents\\PY\\Project\\Backups\\' +
                time.strftime('%Y{0}%m{0}%d{1}%H{2}%M{2}%S').format('_', '   ', '꞉') + '.zip')
    target = zipfile.ZipFile('C:\\Users\\ASUS\\Documents\\PY\\Project\\Backups\\' +
                time.strftime('%Y{0}%m{0}%d{1}%H{2}%M{2}%S').format('_', '   ', '꞉') + '.zip', 'w')
    for folder, subfolders, files in os.walk(source):
        for file in files:
            target.write(os.path.join(folder, file),
                         os.path.relpath(os.path.join(folder, file), source), compress_type=zipfile.ZIP_DEFLATED)
    print('Резервная копия успешно создана в ', target_dir)

keyboard.add_hotkey('y', Yes)
keyboard.add_hotkey('n', No)

keyboard.wait('Esc')