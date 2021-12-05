## ASSIGNMENT 1 | COL759

Team Members:
Dipen Kumar (2018CS50098)
Manoj Kumar (2018CS50411)

## Run the Program —

1.	`make enc` [this will run encryption, on `input.txt` with key `mat.txt` and dump the decrypted string in `out.txt`]
    You can also run the encryption program on your custom input file with custom matrix
    file and have your output in a file name of your choice
    `python encrypt.py <input_text_file> <key_matrix.txt> <encrypted_text.txt>`

2.	`make dec` [this will run decryption, on `out.txt` with key `mat.txt` and dump the decrypted text in `res.txt`]
    This command fires-
    `python decrypt.py <encrypted file> <matrix file> <result file>`

3.  `python main.py <cipher text> <simple text> <complete cipher text>`
    you can also run the program on default testcase using below make command
    `make getkey` [default are ciphertext.txt, simpleText.txt, completeCipherText.txt]
    Here simpleText means the plain text that is supposed to encrypt.



## Implementation Approach:
### Part A:
it encrypts the given plain text using the following equation:
$$C = KP$$
where K is the key matrix of shape n x n. P is the column matrix of shape n x 1. Using this equation, we get C, a column matrix of shape n x 1. We divided the plain text to many chunks of size n and reshaped them to column matrices of shape n x 1. We calculated separated cipher matrices C and merged the cipher text back.

1.  encrypt.py does Hill cipher encryption using key and plaintext.
    It only considers the capital alphabets from the input string. All the ciphered text
    will be in uppercase letters.

    The program cleans the plain text input i.e. removes spaces and punctuations,
    and convertes every letter to uppercase. This then conversts the text to
    a matrix of hill cipher where numbers are filled column wise. Calculates
    chiper text array as k.P(mod 26). This again is converted to text.

2.  decrypt.py does Hill cipher decryption of the encrypted text output.
    There will be no space or punctuations. All the ciphered text will
    be in uppercase letters. There might be extra 'X' letters at the end.

    Converts encrypted text to matrix of hill cipher
    Calculates modulo inverse of key matrix.
    Deciphered text array is calculated using P=(k^-1).C(mod 26)
    which is further converted to text which is our required deciphered text.

### Part B:
    It is implemented in `main.py` :
1. read cipherText, simpleText and copleteCipherText.
2. for k = 2 to 11, check for each:
    i. if length of cipherText is less then k * k or length of completeCipherText % k is non zero, then it is impossible to have a key of shape k * k, hence we go for next k.
    ii. take different combinations of k * k sized ciphertext and simpleText such as first combination is (0 to k * k), second combination is (1 to k * k+1) etc.
        a. For each combination, we try to find the key using K = CP^(-1) if exists.
        b. if key is valid, check for the given cipherText and simpleText.
        c. if the decrypted text is same as simpleText, then go for the completeCipherText and decrypt it.
        e. if the decrypted complete text has IC of range  0.05 to 0.08 (nearby 0.06 which is IC for english language), we assume it to be the original key of size k * k
