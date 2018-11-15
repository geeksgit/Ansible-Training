#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def sayHello(msg):
  return  msg


def main():
  module = AnsibleModule(
    argument_spec=dict(
      message=dict(type='str', required='yes'),
    )
  )
  
  message = module.params['message']
  response = sayHello ( message )
  module.exit_json(meta=response, changed=False)
#  module.fail_json(msg="**************** Fatal error occured**************")

main()
