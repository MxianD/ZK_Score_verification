import json
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# read public key
def load_public_key(path):
    with open(path, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())

# verify signature
def verify_signature(public_key, signature, data):
    try:
        public_key.verify(
            base64.b64decode(signature),
            data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print("key verification fail: ", e)
        return False

# read json files
def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

# verify `proof_signed_by_institution.json`
def verify_proof(input_file, institution_public_key):
    signed_data = load_json(input_file)


    signed_json_str = json.dumps(signed_data["data"], separators=(",", ":")).encode()

    institution_signature = signed_data["institution_signature"]


    print("raw data of institute signature:", signed_json_str)
    print("Base64 format data of institute signature:", institution_signature)


    try:
        decoded_sig = base64.b64decode(institution_signature)
        print("decoded signature:", decoded_sig)
    except Exception as e:
        print("Base64 decoded failed:", e)
        return None

    institution_verified = verify_signature(institution_public_key, institution_signature, signed_json_str)

    if institution_verified:
        print("success!")
        return signed_data
    else:
        print("failed!")
        return None


if __name__ == "__main__":
    institution_public_key = load_public_key("../keys/institution_public.pem")  


    verified_proof = verify_proof("../proof/proof_signed_by_institution.json", institution_public_key)
    
    if verified_proof:
        print("success!")
