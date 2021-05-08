block_size = 4096
def calculate_storage(filesize):
    return block_size * ((filesize + block_size - 1) // block_size)