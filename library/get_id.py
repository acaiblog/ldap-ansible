#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import hashlib

def generate_id_from_string(type, name):
    hash_object = hashlib.sha1(name.encode())
    hash_hex = hash_object.hexdigest()

    hash_int = int(hash_hex, 16)

    if type == "gid":
        random_number = hash_int % (19999 - 10000 + 1) + 10000
    elif type == "uid":
        random_number = hash_int % (29999 - 20000 + 1) + 20000

    return random_number

def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', required=True),
            name=dict(type='str', required=True)
        )
    )
    state = module.params['state']
    name = module.params['name']

    if state == 'gid':
        result = generate_id_from_string('gid', name)
    elif state == 'uid':
        result = generate_id_from_string('uid', name)

    module.exit_json(changed=True, id=result)

if __name__ == '__main__':
    main()
