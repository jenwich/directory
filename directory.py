owners = [
    { 'id': 1, 'name': 'steve' },
]

files = [
    { 'id': 1, 'name': 'hello', 'folder_id': 1, 'label_ids': [1, 2] },
    { 'id': 2, 'name': 'world', 'folder_id': 1, 'label_ids': [2] },
    { 'id': 3, 'name': 'bye', 'folder_id': 2, 'label_ids': [1], 'attrs': [ { 'attr_id': 1, 'value': 'red' } ] },
]

folders = [
    { 'id': 1, 'owner_id': 1, 'name': 'greeting' },
    { 'id': 2, 'owner_id': 1, 'name': 'farewell' },
]

labels = [
    { 'id': 1, 'owner_id': 1, 'name': 'action' },
    { 'id': 2, 'owner_id': 1, 'name': 'object' },
]

attrs = [
    { 'id': 1, 'owner_id': 1, 'name': 'color' },
    { 'id': 2, 'owner_id': 1, 'name': 'size' },
]

def get_files_in_folder(folder_id):
    found_files = [file for file in files if file['folder_id'] == folder_id]
    return found_files

def get_labels(label_ids):
    found_labels = [label for label in labels if label['id'] in label_ids]
    return found_labels

def travel():
    for folder in folders:
        print(f'Folder {folder["name"]}')
        folder_files = get_files_in_folder(folder['id'])

        for file in folder_files:
            file_label_names = [label['name'] for label in get_labels(file['label_ids'])]
            print(f'\tFile {file["name"]} | Labels: {", ".join(file_label_names)}')

travel()

