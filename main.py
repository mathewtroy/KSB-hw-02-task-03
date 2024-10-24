def generate_playfair_square(keyword):
    # Remove duplicates and replace 'J' with 'I'
    keyword = keyword.upper().replace('J', 'I')
    seen = []
    for char in keyword:
        if char not in seen and char.isalpha():
            seen.append(char)

    # Create the rest of the alphabet without 'J'
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in seen:
            seen.append(char)

    # Create a 5x5 Playfair square
    square = [seen[i:i + 5] for i in range(0, 25, 5)]
    return square


def find_position(square, char):
    # Find the row and column of a character in the Playfair square
    for i, row in enumerate(square):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None, None


def decrypt_playfair(ciphertext, keyword):
    # Generate the Playfair square using the keyword
    square = generate_playfair_square(keyword)
    plaintext = ''
    ciphertext = ciphertext.upper().replace(' ', '').replace('J', 'I')

    # Process the ciphertext in pairs of letters
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i + 1]

        # Find positions of each letter in the square
        row_a, col_a = find_position(square, a)
        row_b, col_b = find_position(square, b)

        if row_a == row_b:
            # If both letters are in the same row, move one column to the left
            plaintext += square[row_a][(col_a - 1) % 5]
            plaintext += square[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            # If both letters are in the same column, move one row up
            plaintext += square[(row_a - 1) % 5][col_a]
            plaintext += square[(row_b - 1) % 5][col_b]
        else:
            # If the letters form a rectangle, swap columns
            plaintext += square[row_a][col_b]
            plaintext += square[row_b][col_a]
        i += 2

    return plaintext


if __name__ == "__main__":

    ciphertext = '''WHTOZ MNLAF QNTGR FHPGT GRHLD KFLMF RLBMN RNQFL FTHCE HUMEC WMLGD KKYQB LRMDC VTPWH IQGHM KFYNK EGDKN YXLEQ DKUMP ECRNK ZNPTA BPTKN NRFLF TQA'''
    keyword = 'myska'

    decrypted_message = decrypt_playfair(ciphertext, keyword)
    print("Decrypted message:")
    print(decrypted_message)

    #   VIRTUALIZATIONTECHNOLOGIESENABLEMULTITENANCYCLOUDBUSINESSMODELSBYPROVIDINGASCALABLESHAREDRESOURCEPLATFORMFORALLTENANTS