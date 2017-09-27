import hashlib



def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if ashexstr else hasher.digest())


def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


#[(fname, hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.md5()))
#    for fname in fnamelst]


#[(fname, hashlib.md5(open(fname, 'rb').read()).digest()) for fname in fnamelst]



def md5_single(fname):
    hashlib.md5()


def md5_with_blocksize(fname, blocksize):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(blocksize), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


#fname = "D:\\test_hash.txt"
#print(md5(fname))
#fname = "D:\\test_ha.mp4"
#print(md5(fname))
#print(md5_with_blocksize(fname, 4096))
#fname = "D:\\test_hash.txt"
#print(md5_with_blocksize(fname, 2048))
