import json
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# read private key of institute
def load_private_key(path):
    with open(path, "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)

# Institute use priavte key to sign data
def sign_data(private_key, data):
    return private_key.sign(
        data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

# read JSON file
def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

# save JSON file
def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Institute sign `proof.json`
def sign_proof(input_file, institution_private_key, output_file):
    # read raw JSON data
    data = load_json(input_file)
    json_str = json.dumps(data).encode()

    signature = sign_data(institution_private_key, json_str)
    signature_b64 = base64.b64encode(signature).decode()

    signed_data = {
        "data": json_str.decode(),
        "institution_signature": signature_b64
    }

    save_json(output_file, signed_data)

# main process
if __name__ == "__main__":
    institution_private_key = load_private_key("../keys/institution_private.pem") 

    sign_proof("../proof/proof.json", institution_private_key, "../proof/proof_signed_by_institution.json")

    print("generate institute signature success!")
