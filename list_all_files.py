#!/usr/bin/env python

import sys
import traceback
import s3backupfile

S3_context = {'walk_base_dir': '/data/mssql/AM-NCKM-DSVM001/Program Files/Microsoft SQL Server/MSSQL10_50.MSSQLSERVER/MSSQL/Backup',
               'extension': ('.bak', '.BAK'),
               'retention_hours': 120,
               'bucket_name': 'datg-databases-backup',
               'backup_base_dir': '/data/mssql/AM-NCKM-DSVM001/Program Files/Microsoft SQL Server/MSSQL10_50.MSSQLSERVER/MSSQL/Backup/master'}



if __name__ == '__main__':
    try:
        s3file = s3backupfile.S3Backupfile(
            S3_context['bucket_name'],
            S3_context['walk_base_dir'],
            S3_context['backup_base_dir'])
        s3file.list_s3_objects()
    except:
        print("Something Wrong with exception")
        traceback.print_exc()
        sys.exit(1)
