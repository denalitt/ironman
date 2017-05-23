#!/usr/bin/env python

DOCUMENTATION='''
---
DOCUMENTATION GOES HERE
'''

EXAMPLE='''
EXAMPEL GOES HERE
'''


def main():

    module = AnsibleModule(
        argument_spec=dict(
            device=dict(required=True, type='str'),
            username=dict(required=True, type='str'),
            passwd=dict(required=True, type='str'),
            platform=dict(required=True, type='str'),
            tests=dict(required=True, type='list'),
        ),
        mutually_exclusive=(
            [],
        ),
        supports_check_mode=False
    )

    results = {}
    results['response'] = []
    results['response'].append("ALL GOOD HERE")

    module.exit_json(**results)


from ansible.module_utils.basic import *
if __name__ == "__main__":
    main()
