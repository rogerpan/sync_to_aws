import pytest
import s3backupfile


@pytest.fixture
def backupfile():
    bucket_name = 'datg-databases-backup'
    file_name='/data/mssql/DATGKM-PDBW201B/MSSQL11.MSSQLSERVER/MSSQL/Backup/master/master_20170717003001.BAK'
    backup_base_dir = '/data/'
    return s3backupfile.S3Backupfile(bucket_name, file_name, backup_base_dir)

@pytest.fixture
def badfile():
    bucket_name = 'datg-databases-backup'
    file_name='/data/mssql/AMFLORCDS001V01/C331229-001/TSFINdb01.baks'
    backup_base_dir = '/data/'
    return s3backupfile.S3Backupfile(bucket_name, file_name, backup_base_dir)


def test_bad_base_ex():
    bucket_name = 'datg-databases-backup'
    file_name='/data/mssql/AMFLORCDS001V01/C331229-001/TSFINdb01.bak'
    backup_base_dir = '/xdata/'
    with pytest.raises(ValueError):
        tt = s3backupfile.S3Backupfile(bucket_name, file_name, backup_base_dir)




def test_check_file_exit(backupfile):
    assert backupfile.check_file_exist() is True

def test_check_s3_object_exit(backupfile):
    assert backupfile.check_s3_object_exist() is True

def test_check_file_exist_exception(badfile):
    assert badfile.check_file_exist() is False 
    assert badfile.check_s3_object_exist() is False 
    
