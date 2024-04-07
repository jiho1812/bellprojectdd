import hashlib

input_value = "4321"

# SHA-256 해시 알고리즘을 사용하여 해시 값을 생성
hash_value = hashlib.sha256(input_value.encode()).hexdigest()

print("해시 값:", hash_value)


