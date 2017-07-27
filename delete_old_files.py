#!/usr/bin/env python

import sys
import traceback
import s3backupfile

del_context = {'walk_base_dir': '/data/mssql',
               'extension': ('.bak', '.BAK'),
               'retention_hours': 120,
               'bucket_name': 'datg-databases-backup',
               'backup_base_dir': '/data/'}


if __name__ == '__main__':
    try:
        print(s3backupfile.deleteBackupfile(**del_context))
    except:
        print("Something Wrong with exception")
        traceback.print_exc()
        sys.exit(1)
