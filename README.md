
# Hash-Verify

hash-verify is a Python script designed to verify the integrity of files by comparing the provided hash with the calculated hash. It supports multiple hash algorithms, making it versatile and easy to use for various applications.

## Features
Supports six hash algorithms: md5, sha1, sha256, sha3_256, sha512, sha3_512.\
Interactive command-line input for file path, expected hash, and hash algorithm.\
Cross-platform compatibility.


## Installation

For installing the script simply clone into this repo and start using it.

```bash
  git clone https://github.com/buggymaytricks/Hash-Verify.git
```
    
## Using the Script

After clonning the repo. 
Simply run the script by

```bash
  python3 hash-verify.py
```

It will ask for the hash algorithm to verify the file.\
Lets suppose I want to verify a file I downloaded from kali.org for vmware.\
For verification purposes they have provided a SHA256 hash for the file, and the hash is : *fcb1fea5279471d7015a3837e68e24eefa05f3b5e1f8ad6fb6a3c85a658619aa*

```bash
  Which hash to check? : sha256
```

Then it will ask for the file path you wish to verify.\
The kali virtual machine file is in zip form so I'll paste the path for that file, dont forget to remove double quotes in the path.\
In my case : 

```bash
  Which hash to check? : sha256
  Enter the full path for the file : D:\Python projects\Hash-Verify\kali-linux-2024.2-vmware-amd64.7z

```

Then it will ask for the orignal hash, so I'll put the hash they have mentioned on the site.

```bash
  Which hash to check? : sha256
  Enter the full path for the file : D:\Python projects\Hash-Verify\Hash-Verify\kali-linux-2024.2-vmware-amd64.7z
  Enter the orignal hash : fcb1fea5279471d7015a3837e68e24eefa05f3b5e1f8ad6fb6a3c85a658619aa
```

Then the script will start its work.\
And after calculating the hash for the file it will compare both one from the website and the calculated hash and then give us the results, If the file is verified or the verification failed!

```bash
  Which hash to check? : sha256
  Enter the full path for the file : D:\Python projects\Hash-Verify\Hash-Verify\kali-linux-2024.2-vmware-amd64.7z
  Enter the orignal hash : fcb1fea5279471d7015a3837e68e24eefa05f3b5e1f8ad6fb6a3c85a658619aa
  Be Patient!
  orignal    : fcb1fea5279471d7015a3837e68e24eefa05f3b5e1f8ad6fb6a3c85a658619aa
  calculated : fcb1fea5279471d7015a3837e68e24eefa05f3b5e1f8ad6fb6a3c85a658619aa
  SHA256 verified.
```


