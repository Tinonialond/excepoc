# block header (genesis block)
version = "01000000"
previousblock = "0000000000000000000000000000000000000000000000000000000000000000"
merkleroot = "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
time = "29ab5f49"
bits = "ffff001d"
nonce = "1dac2b7c"

# block header concatenation
blockheader = version + previousblock + merkleroot + time + bits + nonce

# convert hexadecimal string to byte sequence
bytes = [blockheader].pack("H*")

# SHA-256 (first round)
hash1 = Digest::SHA256.digest(bytes)

# SHA-256 (second round)
hash2 = Digest::SHA256.digest(hash1)

# convert from byte sequence back to hexadecimal string
blockhash = hash2.unpack("H*")[0]
