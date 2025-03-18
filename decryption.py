# Caesar Cipher Decryption


def decrypt_caesar(cipher_text) :

    # Loop Of all possible shifts (0 to 25)
    for shift in range(26) :  
        decrypted_text=""  # Space for current shift decryption
        
        # Processing each character in the ciphertext (decryption)
        for letter in cipher_text :
            if letter.isalpha() :  # Check if the character is a letter or not
               
                ascii_base=65 if letter.isupper() else 97
                
                
                """
                DECRYPTION FORMULA

                Decrypted character = chr(((ord(ciphert_text)-base-shift)%26)+base)

                """
                # Decrypt the character within the alphabet range
                decrypted_text += chr((ord(letter)-ascii_base-shift)%26+ascii_base)
            else :
                # Keeping the character as it is if it is not a letter
                decrypted_text+=letter
        
        # Displaying decrypted text for current shift
        print(f"Shift {shift} : {decrypted_text}")
        
        
        # User FEEDBACK

        user_feedback=input("Does this look correct to you ? (yes/y or no/n) :").strip().lower()
        if user_feedback in ["yes","y"] :  # EXITS If the user is satisfied with the decryption
            return decrypted_text
        elif user_feedback not in ["no","n"] :  # Handling the invalid Input
            print("Invalid input . Please Answer with 'yes/y' or 'no/n' .")
    
    # if all shifts are over
    # The text decryption failed to work. Check the 'CIPHERTEXT' entry again to retry the operation.

# Take the ciphertext input from the user
cipher_text=input("Enter the Ciphertext to Decrypt : ")
final_result=decrypt_caesar(cipher_text)
print("\nFinal Decrypted Text :",final_result)


# END
