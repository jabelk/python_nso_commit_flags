import ncs

def create_loopback(dry_run=True, dry_run_style="cli"):
  with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
      root = ncs.maagic.get_root(t)
      device_cdb = root.devices.device["dist-rtr01"]
      device_cdb.config.ios__interface["Loopback"].create("1337")
      device_cdb.config.ios__interface.Loopback["1337"].ip.address.primary.address = "192.168.1.1"
      device_cdb.config.ios__interface.Loopback["1337"].ip.address.primary.mask = "255.255.255.252" 
      cp = ncs.maapi.CommitParams()
      if dry_run == True: 
        if dry_run_style == "cli":
          cp.dry_run_cli()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Dry-Run NSO CLI Style: ")
          print(r)
          print (r.get("local-node"))
        if dry_run_style == "xml":
          cp.dry_run_xml()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Dry-Run XML: ")
          print(r)
          print (r.get("local-node"))
        if dry_run_style == "native":
          cp.dry_run_native()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Dry-Run Native: ")
          print(r)
          print (r.get("device").get("dist-rtr01"))
        if dry_run_style == "reverse":
          cp.dry_run_native_reverse()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Reverse Native Dry Run: ")
          print(r)
          print (r.get("local-node"))
      else:
        print("Commit without dry-run")
        t.apply()

def delete_loopback(dry_run=True, dry_run_style="cli"):
  with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
      root = ncs.maagic.get_root(t)
      device_cdb = root.devices.device["dist-rtr01"]
      del device_cdb.config.ios__interface.Loopback["1337"]
      cp = ncs.maapi.CommitParams()
      if dry_run == True: 
        if dry_run_style == "cli":
          cp.dry_run_cli()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Dry-Run NSO CLI Style: ")
          print(r)
          print (r.get("local-node"))
        if dry_run_style == "xml":
          cp.dry_run_xml()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Dry-Run XML: ")
          print(r)
          print (r.get("local-node"))
        if dry_run_style == "native":
          cp.dry_run_native()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Dry-Run Native: ")
          print(r)
          print (r.get("device").get("dist-rtr01"))
        if dry_run_style == "reverse":
          cp.dry_run_native_reverse()
          r = t.apply_params(True, cp)
          print("Creating Interface Loopback Reverse Native Dry Run: ")
          print(r)
          print (r.get("local-node"))
      else:
        print("Commit without dry-run")
        t.apply()
 
def print_existing_interfaces():
  with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
    root = ncs.maagic.get_root(t)
    device_cdb = root.devices.device["dist-rtr01"]
    input1 = device_cdb.live_status.ios_stats__exec.any.get_input()
    input1.args = ["show ip interface brief"]
    show_command = device_cdb.live_status.ios_stats__exec.any(input1).result
    print (show_command)




if __name__ == "__main__":
  delete_loopback(dry_run=False)
  print_existing_interfaces()
  create_loopback(dry_run=True, dry_run_style="cli")
  create_loopback(dry_run=True, dry_run_style="xml")
  create_loopback(dry_run=True, dry_run_style="native")
  create_loopback(dry_run=True, dry_run_style="reverse")
  create_loopback(dry_run=False)
  print_existing_interfaces()
  delete_loopback(dry_run=True, dry_run_style="cli")
  delete_loopback(dry_run=True, dry_run_style="xml")
  delete_loopback(dry_run=True, dry_run_style="native")
  delete_loopback(dry_run=True, dry_run_style="reverse")
  delete_loopback(dry_run=False)
  print_existing_interfaces()