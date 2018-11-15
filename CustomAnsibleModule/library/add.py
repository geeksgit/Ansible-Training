#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def myAdd(a,b):
  return a+b 


def main():
  module = AnsibleModule(
    argument_spec=dict(
      firstinput=dict(type='float', required='yes'),
      secondinput=dict(type='float', required='yes'),
    )
  )
  
  a = module.params['firstinput']
  b = module.params['secondinput']
  summ = myAdd ( a,b )
  module.exit_json(meta=summ, changed=False)
#  module.fail_json(msg="**************** Fatal error occured**************")

main()
