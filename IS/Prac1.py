def main():
    # The given string
    s = "HelloWorld"
    
    # We will store the results in these lists
    and_results = []
    xor_results = []

    # 127 in binary is 01111111
    mask = 127

    # Iterate over each character in the string
    for char in s:
        # Convert char to its ASCII value
        ascii_value = ord(char)

        # Perform AND and XOR with 127
        and_result = ascii_value & mask
        xor_result = ascii_value ^ mask

        # Convert the results back to characters, if they are printable ASCII values
        # Otherwise, keep them as numbers
        and_char = chr(and_result) if 32 <= and_result <= 126 else and_result
        xor_char = chr(xor_result) if 32 <= xor_result <= 126 else xor_result

        # Append the results to the lists
        and_results.append(and_char)
        xor_results.append(xor_char)

    # Display results
    print("Original String:", s)
    print("AND with 127:", and_results)
    print("XOR with 127:", xor_results)

if __name__ == "__main__":
    main()