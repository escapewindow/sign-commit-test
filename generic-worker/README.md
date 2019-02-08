Public GPG keys for generic-worker go here.

To create new keys for Windows worker types:

- edit generate_keys.sh to add or remove worker types or to change the key type and curve algorithm
- run the key generation script
  - export the private key with a command like:
    ```bash
    gpg2 --no-default-keyring --keyring $key_valid_start_$key_valid_end_gecko-b-win.gpg --armor --export-secret-key noreply-$worker_type@mozilla.com
    ```
    eg:
    ```
    gpg2 --no-default-keyring --keyring 2018-11-13_2019-05-13_gecko-b-win.gpg --armor --export-secret-key noreply-gecko-3-b-win2012@mozilla.com
    ```
- commit and push new public keys to this repo
- allow a few hours for the public keys to propagate
- manually add the private key to the worker type during the ami generation step in OpenCloudConfig by connecting to the ami generation instance over SSH or RDP and writing the key to C:\generic-worker\cot.key