from cryptography.hazmat.primitives.asymmetric import mldsa
from cryptography.exceptions import InvalidSignature

# ML-DSA key generation
def generate_ml_dsa_key():
    private_key = mldsa.MLDSA65PrivateKey.generate()
    public_key = private_key.public_key()

    return private_key, public_key


#def save_private_key

#def save_public_key

#def load_private_key

#def load_public_key

# ML-DSA Signature
def sign_data(private_key, data):
    return private_key.sign(data)

# ML-DSA Verify Signature
def verify_signature(signature, data, public_key):

    try:
        public_key.verify(signature, data)
        return True
    
    except InvalidSignature:
        return False

    
