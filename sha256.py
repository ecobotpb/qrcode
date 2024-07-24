import hashlib

data = 'QualquerCoisa'
hash_object = hashlib.sha256()
hash_object.update(data.encode('utf-8'))

# obtendo o valor hash como uma string hexadecimal

hash_hex = hash_object.hexdigest()

print(f"O hash SHA-256 dos dados inseridos é:\n{hash_hex}")