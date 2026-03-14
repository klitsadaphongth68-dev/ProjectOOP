import os
print('cwd', os.getcwd())
print('assets exists', os.path.isdir('assets'))
print('files', os.listdir('assets'))
path = os.path.join('assets', 'background.png')
print('path', path, 'exists', os.path.isfile(path))
