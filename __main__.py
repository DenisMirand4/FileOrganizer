import os
import shutil

def organize_files(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = get_file_type(file)
            print(file_type)
            if file_type:
                destination = os.path.join(destination_dir, file_type)
                if not os.path.exists(destination):
                    os.makedirs(destination)
                destination_file_path = os.path.join(destination, file)
                if not os.path.exists(destination_file_path):
                    shutil.move(file_path, destination)

def get_file_type(file_name):
    file_extension = os.path.splitext(file_name)[1]
    if file_extension in ('.jpg', '.png', '.gif', '.jpeg'):
        return 'images'
    elif file_extension in ('.doc', '.pdf', '.txt', '.pptx', '.docx'):
        return 'documents'
    elif file_extension in ('.mp4', '.avi', '.mkv', '.mov', '.flv'):
        return 'videos'
    elif file_extension in ('.mp3', '.wav', '.flac', '.ogg'):
        return 'audio'
    elif file_extension in ('.zip', '.rar', '.tar'):
        return 'compressed'
    elif file_extension in ('.exe', '.msi'):
        return 'installers'
    elif file_extension in ('.parquet', '.csv', '.tsv', '.xls', '.xlsx', '.json'):
        return 'data'
    elif file_extension in ('.xml', '.html', '.css', '.js', '.htm'):
        return 'web'
    elif file_extension in ('.bacpac', '.bak', '.mdf', '.ldf'):
        return 'databases'
    else:
        return 'others'

if __name__ == '__main__':
    source_directory = ''
    destination_directory = ''
    organize_files(source_directory, destination_directory)
