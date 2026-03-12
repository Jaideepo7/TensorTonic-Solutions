def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code  
    chunked_txt = []
    step = chunk_size-overlap
    for i in range(0,len(tokens),step):
        chunk = []
        chunk = tokens[i:i+chunk_size]
        chunked_txt.append(chunk)

        if i + chunk_size >= len(tokens):
            break
    return chunked_txt