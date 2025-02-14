import json
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def load_private_key(path):
    with open(path, "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)


def sign_data(private_key, data):
    return private_key.sign(
        data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )


def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def sign_proof_by_user(input_file, user_private_key, output_file):

    signed_data = load_json(input_file)
    signed_json_str = json.dumps(signed_data).encode()

    user_signature = sign_data(user_private_key, signed_json_str)
    user_signature_b64 = base64.b64encode(user_signature).decode()

    signed_data["user_signature"] = user_signature_b64

    save_json(output_file, signed_data)

if __name__ == "__main__":
    user_private_key = load_private_key("../keys/user_private.pem") 

    sign_proof_by_user("../proof/proof_signed_by_institution.json", user_private_key, "../proof/proof_signed_by_user.json")

    print("generate user signature success!")
