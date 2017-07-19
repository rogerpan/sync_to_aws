import os
import time
import s3backupfile
import datetime


def creation_date(path_to_file):
    """get the file creation date or modification date"""
    stat = os.stat(path_to_file)
    try:
        return stat.st_birthtime
    except AttributeError:
        return stat.st_mtime


def deleteBackupfile(**del_context):
    """ Delete backup file based on the following three criteria
         mtime or ctime age >= retention_hours,
         and exist on S3,

        args:
            del_context = { 'walk_base_dir': '/data/mssql', #start travers dir
                'extension': ('.bak', '.BAK'),  # the file extensions to check
                'retention_hours': 70,  # hours of file age to be deleted
                'bucket_name': 'datg-databases-backup',  # s3 bucket name
                'backup_base_dir':'/data/' }  # the os level backup base dir
       return:
            None
    """
    total_files = 0

    ret = dict(datetime = str(datetime.datetime.now()),
               supposed_removed_files = 0,
               removed_files = 0 )

    for root, dirs, files in os.walk(del_context['walk_base_dir']):
        for name in files:
            if name.lower().endswith(del_context['extension']):
                total_files += 1
                fullpath = os.path.join(root, name)
                mtime = creation_date(fullpath)
                diff = round((int(time.time()) - mtime)/3600, 1)
                if diff >= del_context['retention_hours']:
                    # print(diff, 'hours', fullpath)
                    s3file = s3backupfile.S3Backupfile(
                                del_context['bucket_name'],
                                fullpath,
                                del_context['backup_base_dir'])
                    if(s3file.check_s3_object_exist()):
                        os.remove(fullpath)
                        # print('removed')
                        ret['removed_files'] += 1
                    else:
                        # print('kept, the file does not exist on S3 yet')
                        ret['supposed_removed_files'] += 1

    ret['kept_files'] = total_files - ret['removed_files']
    return ret

