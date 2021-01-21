# Learn by Doing: Python NSO Commit Flags

NSO has a ton of features. This repository is the first of a series which will show a simple use case, along with a feature. The purpose is dual:

1. See NSO applied to a variety of configuration situations and see how versatile it is..
1. Learn something new and have an example to follow

This example is a service package deploying:

**Loopback IP Address Configuration**

and the feature I am showcasing is:

**Commit Flags in Python**

This example assumes a working knowledge of services and NSO. 

## Installation

[Reserve the NSO Reservable Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology)

If you need to revisit some of the NSO Basics, you can [start here](https://developer.cisco.com/learning/lab/learn-nso-the-easy-way/step/1). 

The Python script is designed to be run on the system install NSO, but that server does not have git clone set up. You can create a file in the user home directory and copy the contents of the Python script into it and run it. Also note that you should run Python3 not simply Python (which goes to Python2)



```bash
~$ ssh developer@10.10.20.49
Warning: Permanently added '10.10.20.49' (ECDSA) to the list of known hosts.
Last login: Thu Jan 21 10:47:41 2021 from 192.168.254.12
[developer@nso ~]$
[developer@nso ~]$ pwd
/home/developer
[developer@nso ~]$ touch python_commit_flags.py
[developer@nso ~]$ nano python_commit_flags.py
[developer@nso ~]$ python3 python_commit_flags.py
```

## Sample Output

Here is some sample output:

```
Commit without dry-run

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.175    YES TFTP   up                    up
GigabitEthernet2       172.16.252.21   YES TFTP   up                    up
GigabitEthernet3       172.16.252.25   YES TFTP   up                    up
GigabitEthernet4       172.16.252.2    YES TFTP   up                    up
GigabitEthernet5       172.16.252.10   YES TFTP   up                    up
GigabitEthernet6       172.16.252.17   YES TFTP   up                    up
Loopback0              unassigned      YES unset  administratively down down
dist-rtr01#
Creating Interface Loopback Dry-Run NSO CLI Style:
{'dry-run': True, 'outformat': 'cli', 'local-node': ' devices {\n     device dist-rtr01 {\n         config {\n             interface {\n+                Loopback 1337 {\n+                    ip {\n+                        address {\n+                            primary {\n+                                address 192.168.1.1;\n+                                mask 255.255.255.252;\n+                            }\n+                        }\n+                    }\n+                }\n             }\n         }\n     }\n }\n'}
 devices {
     device dist-rtr01 {
         config {
             interface {
+                Loopback 1337 {
+                    ip {
+                        address {
+                            primary {
+                                address 192.168.1.1;
+                                mask 255.255.255.252;
+                            }
+                        }
+                    }
+                }
             }
         }
     }
 }

Creating Interface Loopback Dry-Run XML:
{'dry-run': True, 'outformat': 'xml', 'local-node': '<devices xmlns="http://tail-f.com/ns/ncs">\n  <device>\n    <name>dist-rtr01</name>\n    <config>\n      <interface xmlns="urn:ios">\n        <Loopback>\n          <name>1337</name>\n          <ip>\n            <address>\n              <primary>\n                <address>192.168.1.1</address>\n                <mask>255.255.255.252</mask>\n              </primary>\n            </address>\n          </ip>\n        </Loopback>\n      </interface>\n    </config>\n  </device>\n</devices>\n'}
<devices xmlns="http://tail-f.com/ns/ncs">
  <device>
    <name>dist-rtr01</name>
    <config>
      <interface xmlns="urn:ios">
        <Loopback>
          <name>1337</name>
          <ip>
            <address>
              <primary>
                <address>192.168.1.1</address>
                <mask>255.255.255.252</mask>
              </primary>
            </address>
          </ip>
        </Loopback>
      </interface>
    </config>
  </device>
</devices>

Creating Interface Loopback Dry-Run Native:
{'dry-run': True, 'outformat': 'native', 'device': {'dist-rtr01': 'interface Loopback1337\n ip redirects\n ip address 192.168.1.1 255.255.255.252\n no shutdown\nexit\n'}}
interface Loopback1337
 ip redirects
 ip address 192.168.1.1 255.255.255.252
 no shutdown
exit

Creating Interface Loopback Reverse Native Dry Run:
{'dry-run': True, 'outformat': 'native', 'device': {'dist-rtr01': 'no interface Loopback1337\n'}}
None
Commit without dry-run

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.175    YES TFTP   up                    up
GigabitEthernet2       172.16.252.21   YES TFTP   up                    up
GigabitEthernet3       172.16.252.25   YES TFTP   up                    up
GigabitEthernet4       172.16.252.2    YES TFTP   up                    up
GigabitEthernet5       172.16.252.10   YES TFTP   up                    up
GigabitEthernet6       172.16.252.17   YES TFTP   up                    up
Loopback0              unassigned      YES unset  administratively down down
Loopback1337           192.168.1.1     YES manual up                    up
dist-rtr01#
Creating Interface Loopback Dry-Run NSO CLI Style:
{'dry-run': True, 'outformat': 'cli', 'local-node': ' devices {\n     device dist-rtr01 {\n         config {\n             interface {\n-                Loopback 1337 {\n-                    ip {\n-                        address {\n-                            primary {\n-                                address 192.168.1.1;\n-                                mask 255.255.255.252;\n-                            }\n-                        }\n-                    }\n-                }\n             }\n         }\n     }\n }\n'}
 devices {
     device dist-rtr01 {
         config {
             interface {
-                Loopback 1337 {
-                    ip {
-                        address {
-                            primary {
-                                address 192.168.1.1;
-                                mask 255.255.255.252;
-                            }
-                        }
-                    }
-                }
             }
         }
     }
 }

Creating Interface Loopback Dry-Run XML:
{'dry-run': True, 'outformat': 'xml', 'local-node': '<devices xmlns="http://tail-f.com/ns/ncs">\n  <device>\n    <name>dist-rtr01</name>\n    <config>\n      <interface xmlns="urn:ios">\n        <Loopback xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"\n                  nc:operation="delete">\n          <name>1337</name>\n        </Loopback>\n      </interface>\n    </config>\n  </device>\n</devices>\n'}
<devices xmlns="http://tail-f.com/ns/ncs">
  <device>
    <name>dist-rtr01</name>
    <config>
      <interface xmlns="urn:ios">
        <Loopback xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"
                  nc:operation="delete">
          <name>1337</name>
        </Loopback>
      </interface>
    </config>
  </device>
</devices>

Creating Interface Loopback Dry-Run Native:
{'dry-run': True, 'outformat': 'native', 'device': {'dist-rtr01': 'no interface Loopback1337\n'}}
no interface Loopback1337

Creating Interface Loopback Reverse Native Dry Run:
{'dry-run': True, 'outformat': 'native', 'device': {'dist-rtr01': 'interface Loopback1337\n ip redirects\n ip address 192.168.1.1 255.255.255.252\n no shutdown\nexit\n'}}
None
Commit without dry-run

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.175    YES TFTP   up                    up
GigabitEthernet2       172.16.252.21   YES TFTP   up                    up
GigabitEthernet3       172.16.252.25   YES TFTP   up                    up
GigabitEthernet4       172.16.252.2    YES TFTP   up                    up
GigabitEthernet5       172.16.252.10   YES TFTP   up                    up
GigabitEthernet6       172.16.252.17   YES TFTP   up                    up
Loopback0              unassigned      YES unset  administratively down down
dist-rtr01#
[developer@nso ~]$
```

### Explanation

The script runs in the following order:
```python
  delete_loopback(dry_run=False)
  print_existing_interfaces()
  create_loopback(dry_run=True, dry_run_style="cli")
  create_loopback(dry_run=True, dry_run_style="xml")
  create_loopback(dry_run=True, dry_run_style="native")
  create_loopback(dry_run=False)
  print_existing_interfaces()
  delete_loopback(dry_run=True, dry_run_style="cli")
  delete_loopback(dry_run=True, dry_run_style="xml")
  delete_loopback(dry_run=True, dry_run_style="native")
  delete_loopback(dry_run=False)
  print_existing_interfaces()
```

It deletes the loopback, just in case it is already there (as if it is present, the dry-run results are not interesting). It then issues a "show ip interfaces brief" to the device, followed by a series of dry-run executions, showing the different outputs, including dry-run reverse. The script then actually creates the loopback, shows the dry-run for deleting the loopback, and then actually deletes it, finishing with another "show ip int brief."

All of the commit flags, at the time of this writing are:
```
commit_queue_async
commit_queue_sync
commit_queue_bypass
commit_queue_tag
commit_queue_lock
commit_queue_block_others
commit_queue_atomic
commit_queue_non_atomic
commit_queue_error_option
no_networking
no_revision_drop
no_overwrite
no_out_of_sync_check
no_lsa
use_lsa
no_deploy
reconcile_keep_non_service_config
reconcile_discard_non_service_config
dry_run_xml
dry_run_cli
dry_run_native
dry_run_native_reverse
```

They are also listed in the [Python API guide](https://developer.cisco.com/docs/nso/api/#!ncs-maapi/header-classes).

Another tip, if you are running in a system install, and your transaction handler `with` statement does not include the linux group for the user, it will not work:

```python
[developer@nso ~]$ python3 python_nso_commit_flags.py
Traceback (most recent call last):
  File "learn_by_doing.py", line 5, in <module>
    device_cdb = root.devices.device["dist-rtr01"]
  File "/opt/ncs/current/src/ncs/pyapi/ncs/maagic.py", line 1088, in __getitem__
    self._backend._exists(self._path + keystr))):
  File "/opt/ncs/current/src/ncs/pyapi/ncs/maagic.py", line 124, in _exists
    return self.exists(path)
  File "/opt/ncs/current/src/ncs/pyapi/ncs/maapi.py", line 1244, in proxy
    return real(self2.maapi, self2.th, *args, **kwargs)
  File "/opt/ncs/current/src/ncs/pyapi/ncs/maapi.py", line 400, in exists
    return True if _tm.maapi.exists(self.msock, th, path) else False
_ncs.error.Error: access denied (3): access denied
```
will occur if the following statement is used:

`with ncs.maapi.single_write_trans('admin', 'python') as t:`

as opposed to the following correct one, including the groups (relevant for system install, but a difference in code for local install testing

`with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:`
 
 the key statement added being `groups=['ncsadmin']`. This is not specific to commit flags, but worth mentioning as I ran into it while developing, as I usually develop in a local install, so did not have the `groups=['ncsadmin']` in my code originally. 

### TLDR

The code for adding a commit flag (without all the conditional baggage I added to make the script more flexible):
```python
with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
    #make a change
    root = ncs.maagic.get_root(t)
    device_cdb = root.devices.device["dist-rtr01"]
    device_cdb.config.ios__interface["Loopback"].create("1337")
    cp = ncs.maapi.CommitParams()
    # choose your flag method below
    cp.dry_run_native()
    # feed that cp object into the apply_params method
    r = t.apply_params(True, cp)
    print(r)
```

Thanks and credit to those in this [thread](https://community.cisco.com/t5/nso-developer-hub-discussions/is-there-a-way-to-get-quot-commit-dry-run-quot-from-python/td-p/4059445) 

[also this one, if you working with services.](https://community.cisco.com/t5/nso-developer-hub-discussions/get-python-action-to-display-dry-run-of-values-set-by-python-not/td-p/3730969)