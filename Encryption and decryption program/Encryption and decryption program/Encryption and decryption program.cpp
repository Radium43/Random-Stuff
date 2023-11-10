#include <iostream>
#include <fstream>
#include <string>
#include <ctime> 
#include <cstdlib>  
using namespace std;

string encrypt(string message, int key) {
    string result = "";

    for (char& ch : message) {
        if (isalpha(ch)) {
            char base = isupper(ch) ? 'A' : 'a';
            result += static_cast<char>((ch - base + key) % 26 + base);
        }
        else {
            result += ch;
        }
    }

    return result;
}

string decrypt(string encryptedMessage, int key) {
    return encrypt(encryptedMessage, 26 - key);
}

int main() {
    srand(time(0));
    int key = rand() % 25 + 1;
    string message;

    cout << "Encryption Key: " << key << endl;
    cout << "Enter the message: ";
    getline(cin, message);

    string encryptedMessage = encrypt(message, key);
    cout << "Encrypted message: " << encryptedMessage << endl;
    string decryptedMessage = decrypt(encryptedMessage, key);
    cout << "Decrypted message: " << decryptedMessage << endl;

    return 0;
}
