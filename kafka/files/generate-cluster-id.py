# Python script to generate base64 encoded UUID for KRaft clusters.
# The script generates a UUID string and removes the hyphens from it. The string is then encoded to a base64 string and the first STRING_LENGTH chars are exported to a file OUTPUT_FILE.
import uuid
from base64 import b64encode

OUTPUT_FILE = "kafka-cluster-id"
STRING_LENGTH = 22

uuid_string = ''.join(str(uuid.uuid1()).split('-')).encode('ascii')
output = b64encode(uuid_string)[0:STRING_LENGTH].decode()

with open(OUTPUT_FILE, "w") as fp:
    fp.write(output)
