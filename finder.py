import os
import shutil


search_folder = 'ru' 
existing_files = []

for currentpath, folders, files in os.walk(search_folder):
	for file in files:
		if file.endswith('.md'):
			existing_files.append(os.path.join(currentpath, file)[3:])



with open(os.path.join(search_folder, 'SUMMARY.md')) as f:
	lines = f.readlines()

summary_files = [line for line in lines if '*' in line]


orphaned_files = []
found = False

for filename in existing_files:
	for line in lines:
		stripped_line = line[line.find('(')+1:line.find(')')]
		if filename == stripped_line:
			found = True
			break
	if not found:
		orphaned_files.append(filename)
	found = False


# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

orphaned_files.remove('SUMMARY.md')
orphaned_files.remove('waves-client/security.md')

current_folder = '/Users/mmaslin/Dropbox/Dropbox/Waves/waves-documentation'


for file in orphaned_files:
	# print(file)
	file_name = file.split('/')[-1]
	file_path = f'{current_folder}/en/{file}'
	target_path = f'{current_folder}/unused_docs/{file_name}'
	print(file_name)
	shutil.move(file_path, target_path)
	print(file, 'moved')

