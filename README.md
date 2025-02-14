# ZK_Score_verification
Any entity can use zk proof to verify students' score.
How does it protect users' privacy and also prove they fit the requirements?

First, we use circom and snark.js to generate zk proof to prove that he meets the score requirements.
Second, zk proofs will be encrypted by institutions and user in turn.
Then, the college use public key of institution and user to decrypted the zk proof, and then verify the zk proof using public.json, and verification key.


### /proof
The folder proof under the zk_score_verification folder is used to store zk proof and others will be used when verifying student's score and id.
input.json: Used to generate zk proof, as a input.
proof_signed_by_institution.json: zk proof signed by institution
proof_signed_by_user.json: signed zk proof signed by user
proof.json: zk proof
verification key: used to verify zk proof.
public.json: public input, the college can use this to verify if zk proof is true.
### /scripts
The folder script under the zk_score_verification folder is used to store python scripts to generate important file and verify the zk proof.
### /keys
The folder keys under the zk_score_verification folder is used to store public key and private key of user and institution.
### /circom
This folder is used to store zk circuit, and we generate zk proof here.
#### /build
We generate zk proof here
#### /circomlib
A library used to write zk circuit
#### /proof
we use this to generate zk proof, the json file are the same as folder zk_score_verification/proof's
### sat_verifier.circom
This is zk circuit