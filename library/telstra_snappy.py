#!/usr/bin/env python

DOCUMENTATION='''
---
DOCUMENTATION GOES HERE
'''

EXAMPLE='''
EXAMPEL GOES HERE
'''

from jnpr.jsnapy import SnapAdmin
from pprint import pprint
from jnpr.junos import Device


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

    config_data = {}
    config_data['hosts'][0]['device'] = module.params['device']
    config_data['hosts'][0]['username'] = module.params['username']
    config_data['hosts'][0]['passwd'] = module.params['passwd']
    config_data['tests'] = module.params['tests']

    js = SnapAdmin()
    snapchk = js.snapcheck(config_data, "pre")
    results = {}
    for val in snapchk:
        results['device'] = val.device
        results['result'] = val.result
        results['no_passed'] = val.no_passed
        results['no_failed'] = val.no_failed
        results['test_results'] = val.test_results

    module.exit_json(**results)


from ansible.module_utils.basic import *
if __name__ == "__main__":
    main()
