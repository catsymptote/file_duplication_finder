from lib import file_hasher
print (file_hasher.md5("D:\\test_hash.txt"))
print (file_hasher.md5_with_blocksize("D:\\test_hash.txt", 4096))