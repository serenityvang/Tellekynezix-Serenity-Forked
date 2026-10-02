# =====================================================================
# Secure Networking & Quantum Cryptography Module (Avatar GUI Component)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Academic Capstone Prototyping Artifact
# Prepared by: John Nonye, Nolan Murphy, Serenity Vang, and Vejay Deonarine[cite: 2, 3]
# Institutional Context: St. Cloud State University (SE-490/491)
# Note: This file contains a generic local simulation model for academic 
# interface testing purposes and local telemetry visualization[cite: 2].
# =====================================================================

import hashlib
import json
import time

class QuantumBlock:
    def __init__(self, index, previous_hash, telemetry_data, pqc_signature):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.telemetry_data = telemetry_data  # Configuration or telemetry stream data[cite: 2]
        self.pqc_signature = pqc_signature    # Didactic signature representation
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "telemetry_data": self.telemetry_data,
            "pqc_signature": self.pqc_signature
        }, sort_keys=True).encode()
        return hashlib.sha3_256(block_string).hexdigest()

class AvatarQuantumPipeline:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return QuantumBlock(0, "0", {"status": "INITIALIZED"}, "PQC_GENESIS_SIGNATURE")

    def get_latest_block(self):
        return self.chain[-1]

    def add_telemetry_record(self, telemetry_data, pqc_signature):
        prev_block = self.get_latest_block()
        new_block = QuantumBlock(
            index=len(self.chain),
            previous_hash=prev_block.hash,
            telemetry_data=telemetry_data,
            pqc_signature=pqc_signature
        )
        self.chain.append(new_block)
        return new_block

# Local prototyping execution block
if __name__ == "__main__":
    pipeline = AvatarQuantumPipeline()
    sample_data = {"tab": "Cloud Computing", "action": "save_config", "packet": "mock_stream_0x99"}
    mock_pqc_sig = "ML-DSA-Sig-Placeholder-9000"
    
    block = pipeline.add_telemetry_record(sample_data, mock_pqc_sig)
    print(f"Block successfully generated! Hash: {block.hash}")

