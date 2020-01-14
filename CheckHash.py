from bitcoin.rpc import RawProxy
import hashlib
import sys
import struct

p = RawProxy()

height = sys.argv[1]
block_hash = p.getblockhash(int(height))
block_header = p.getblockheader(block_hash)

def little_endian(value, is_number = False):
        if is_number == True:
                value = struct.pack("<I", value).encode('hex')
                return value
        else:
                binary = value.decode('hex')
                value = binary[::-1].encode('hex_codec')
                return value

header_hex = str(little_endian(block_header['versionHex']) + little_endian(block_header['previousblockhash']) +
              little_endian(block_header['merkleroot']) + str(little_endian(block_header['time'], is_number=True)) +
              little_endian(str(block_header['bits'])) + str(little_endian(block_header['nonce'], is_number=True)))

header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
calculated_hash = hash[::-1].encode('hex_codec')

print(block_hash)
print(calculated_hash)
if block_hash == calculated_hash:
        print("Hashes match.")
else:
        print("Hashes does not match.")
		
		
		
	

