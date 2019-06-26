import os, struct

def encrypt_file(input_filepath, encryptor, keysize):
    fragment_size = 256 * keysize
    output_filepath = input_filepath + '.enc'
    input_size = os.path.getsize(input_filepath)

    with open(input_filepath, 'rb') as infile:
        with open(output_filepath, 'wb') as encfile:

            # write size of original file in the first 8 bits of encrypted file
            encfile.write(struct.pack('<Q', input_size))

            # write encrypted fragments of original file in blocks of 256*size(keysize) 

            while True:
                fragment = infile.read(fragment_size)
                # check if no more data to read
                if len(fragment) == 0:
                    break
                # (blocksize % keysize) must be 0. if not, pad it until 0
                elif (len(fragment) % 16) != 0:
                    print(keysize - len(fragment) % keysize)
                    fragment += b'0' * (keysize - len(fragment) % keysize)

                encfile.write(encryptor.encrypt(fragment))
                
    # exclude original file
    os.remove(input_filepath)



def decrypt_file(input_filepath, decryptor, keysize):
    fragment_size = 256 * keysize
    out_filename = os.path.splitext(input_filepath)[0]

    with open(input_filepath, 'rb') as infile:

        # read the original filesize from the first 8 bits of the encrypted file
        original_size = infile.read(struct.calcsize(8))
        original_size = struct.unpack('<Q', original_size)[0]

        with open(out_filename, 'wb') as outfile:
            # read data from file and decrypt it
            while True:
                fragment = infile.read(fragment_size)
                # check if no more data to read
                if len(fragment) == 0:
                    break   
                outfile.write(decryptor.decrypt(fragment))

            # truncate to orig size so if any padding made can be removed
            outfile.truncate(original_size)