<h1>CryptoComms</h1>
<strong>A Python script for encrypted P2P communications</strong><br/>
<h2>Information</h2>
CryptoComms is a python script that uses the PyCrypto Library and a set of other modules in order to facilitate communication between two computers over an IP network. It encrypts messages using R.S.A. with variable key size and public exponent and transmits them over HTTP to the other party.<br/>
<h2>To Do</h2>
- [ ] Introduce key verification to prevent MitM attacks
- [ ] Use RSA for symmetric key exchange only, use AES-128 in GCM or CBC for data encryption
- [ ] Remove the ```eval``` and replace it with something secure
- [ ] Add full UTF-8 support to the interface and the messages
<br/>
<h2>Disclaimer</h2>
<strong>Currently this software is marked as <u>PROOF OF CONCEPT</u>. It may <u>NEVER</u> be used in a production enviroment or for any confidential communication. Even after the completion of the To-Do list, it has to be audited and tested before this state can change.</strong>
