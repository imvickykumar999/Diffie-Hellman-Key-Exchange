import socket

# Parameters from the Laboratory: The Interactive Math
P = 23  # Public Modulus
G = 5   # Public Generator (Base)

def main():
    # 1. Select Private Key (a)
    private_a = 6
    print(f"[STEP 1] Client (Alice) selected private key: {private_a}")

    # 2. Generate Public Key (A)
    # A = g^a mod p
    public_a = pow(G, private_a, P)
    print(f"[STEP 2] Computed Public Key (A): {public_a}")

    # Set up networking
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(('localhost', 65432))
        
        # 3. Send Public Key (A) to Bob
        client_socket.sendall(str(public_a).encode())
        print(f"[STEP 3] Sent Public Key (A) to Bob.")

        # 4. Receive Public Key (B) from Bob
        data = client_socket.recv(1024).decode()
        public_b = int(data)
        print(f"[STEP 4] Received Bob's Public Key (B): {public_b}")

        # 5. Calculate Shared Secret (s)
        # s = B^a mod p
        shared_secret = pow(public_b, private_a, P)
        
        print("\n" + "="*30)
        print(f"SHARED SECRET DERIVED: {shared_secret}")
        print("="*30)
        print("Success! Alice and Bob now have the same key.")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()