# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['workspace', 'workspace.examples', 'workspace.tests']

package_data = \
{'': ['*'],
 'workspace': ['.git/*',
               '.git/hooks/*',
               '.git/info/*',
               '.git/logs/*',
               '.git/objects/00/*',
               '.git/objects/03/*',
               '.git/objects/08/*',
               '.git/objects/0a/*',
               '.git/objects/18/*',
               '.git/objects/1a/*',
               '.git/objects/2c/*',
               '.git/objects/34/*',
               '.git/objects/36/*',
               '.git/objects/37/*',
               '.git/objects/42/*',
               '.git/objects/47/*',
               '.git/objects/48/*',
               '.git/objects/50/*',
               '.git/objects/56/*',
               '.git/objects/57/*',
               '.git/objects/5f/*',
               '.git/objects/66/*',
               '.git/objects/6a/*',
               '.git/objects/74/*',
               '.git/objects/75/*',
               '.git/objects/79/*',
               '.git/objects/85/*',
               '.git/objects/88/*',
               '.git/objects/92/*',
               '.git/objects/a7/*',
               '.git/objects/b5/*',
               '.git/objects/c5/*',
               '.git/objects/c9/*',
               '.git/objects/da/*',
               '.git/objects/e3/*',
               '.git/objects/e6/*',
               '.git/objects/e8/*',
               '.git/objects/eb/*',
               '.git/objects/ef/*',
               '.git/objects/f9/*',
               '.git/refs/tags/*',
               '.github/workflows/*',
               'images/*']}

modules = \
['conf_diff']
install_requires = \
['colorama>=0.4.4,<0.5.0']

extras_require = \
{':python_version >= "3.8"': ['importlib-metadata>=1.0,<2.0']}

setup_kwargs = {
    'name': 'conf-diff',
    'version': '0.6.5',
    'description': 'compare configuration files',
    'long_description': '[![license](https://img.shields.io/github/license/abatilo/actions-poetry.svg)](https://github.com/muhammad-rafi/conf_diff/blob/main/LICENSE)\n[![Pypi](https://img.shields.io/pypi/v/conf_diff.svg)](https://pypi.org/project/conf-diff/) \n[![Build Status](https://github.com/muhammad-rafi/conf_diff/actions/workflows/main.yml/badge.svg)](https://github.com/muhammad-rafi/conf_diff/actions)\n[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/muhammad-rafi/conf_diff)\n\n# Introduction\n\nThis module is built to provide you the configuration comparison between two configuration files and generates configuration differences either on the terminal or create a HTML output file based on the parameter provided to the module.\n\nNote: This module is built on the top of the Python built-in difflib module but modified to show you the colourful output and customised HTML template.\n\n## Features\n\n* Shows the configuration differences on the terminal window with colourful output.\n* Generate a HTML output file as a comparison report.\n\n## Installation\n\nInstall this module from PyPI:\n\n```sh\n\npip install conf-diff\n\n```\n\n## Usage:\n\n### Prerequisite\nAs this module compares the configuration difference between two config file, so we need to have two configuration files should be present in the same directory where you are running the script from or specify the absolute path for the configuration files. e.g. `"/Users/rafi/sandbox-nxos-1.cisco.com_before_config.cfg"` and `"/Users/rafi/sandbox-nxos-1.cisco.com_after_config.cfg"`\n\nYou may use either .cfg or .txt file extensions.\n\nIn the below example, I am using two output files of \'show running-config ntp\' from the Cisco NXOS always-on sandbox, assuming that, `sbx-nxos-mgmt.cisco.com_ntp_before.cfg` was taken before the change and `sbx-nxos-mgmt.cisco.com_ntp_after.cfg` after the change, and we want to see the configuration diffrence between them. You may name the filenames as you like or add the timestamp.\n\nImport the `conf_diff` module in your python script and instantiate a class object with both config output files as arguments.\n\n```python\n\nimport conf_diff\n\n# Instantiate a class object \'config_change\'\nconfig_change = conf_diff.ConfDiff("sbx-nxos-mgmt.cisco.com_ntp_before.cfg", "sbx-nxos-mgmt.cisco.com_ntp_after.cfg")\n\n# Display the output of the configuration difference on the terminal \nprint(config_change.diff())\n\n```\n\nThis will display the colourful configuration difference on the terminal. \n\n![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/cli_output.png)\n\nTo generate a html output file, add third argument as the expected output file name. e.g. `"sbx-nxos-mgmt.cisco.com_html_output.html"`\n\n```python\n\n # Instantiate a class object \'html_diff\'\nhtml_diff = conf_diff.ConfDiff("sbx-nxos-mgmt.cisco.com_ntp_before.cfg", "sbx-nxos-mgmt.cisco.com_ntp_after.cfg", "sbx-nxos-mgmt.cisco.com_html_output.html")\n\n# Generates a `sbx-nxos-mgmt.cisco.com_html_output.html` in your current directory unless expected absolute path is specified.\nhtml_diff.diff()\n\n```\nThis will generates a `sbx-nxos-mgmt.cisco.com_html_output.html` in your current directory unless expected absolute path is specified.\n\nSee the screenshot below for the `sbx-nxos-mgmt.cisco.com_html_output.html`\n\n![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/html_output_file.png)\n\n### Example\nIn this example, I am running a script with well known \'netmiko\' library and taking a backup of running config before and after the change. Then compare the configuration difference between these config files. See the [example](https://github.com/muhammad-rafi/conf_diff/tree/main/examples) directory. \n\n\n```python\n\nfrom netmiko import ConnectHandler\nimport conf_diff\nimport time\n\n# List of hosts or devices\nhosts_list = [\'sandbox-nxos-1.cisco.com\']\n\n# For loop to run through all the devices in the \'hosts_list\'\nfor host in hosts_list:\n    device = {\n        "device_type": "cisco_nxos",\n        "ip": host,\n        "username": "admin",\n        "password": "Admin_1234!",\n        "port": "22",\n    }\n\n    # Creating a network connection with the device\n    print(f"**** Connecting to {device[\'ip\']} **** ...\\n")\n    net_connect = ConnectHandler(**device)\n\n    # Sending \'show\' command to the device to take first configuration snapshot before updating the device\n    print(f"Connected to {device[\'ip\']}, Sending commands ...\\n")\n    current_config = net_connect.send_command("show running-config")\n\n    print(f"Saving pre-configuration change output for {device[\'ip\']} ...\\n")\n\n    # Opening a file in write mode to save the configuration before the change\n    with open(f"{device[\'ip\']}_before_config.cfg", "w") as f:\n        f.write(current_config)\n\n    print(f"{device[\'ip\']}_before_config.cfg has been saved ...\\n")\n\n    # List of configuration commands to the device\n    print(f"Updating the configuration for {device[\'ip\']}...\\n")\n    config_commands = [\'interface Ethernet1/22-28\',\n                       \'description testing python script\',\n                       \'switchport mode trunk\',\n                       \'switchport trunk allowed vlan 512,654,278\'\n                       ]\n\n    # Sending above configuration commands to updathe the device configuration\n    config_update = net_connect.send_config_set(config_commands)\n\n    # Sleep for 2 sec before take another configuration snapshot\n    time.sleep(2)\n\n    # Sending \'show\' command to the device again to take another configuration snapshot after the change\n    print(f"Saving post-configuration change output for {device[\'ip\']} ...\\n")\n    updated_config = net_connect.send_command("show running-config")\n\n    # Opening a file in write mode to save the configuration after the change\n    with open(f"{device[\'ip\']}_after_config.cfg", "w") as f:\n        f.write(updated_config)\n\n    print(f"{device[\'ip\']}_after_config.cfg has been saved ...\\n")\n\n    # Teardown the network connection with the device\n    net_connect.disconnect()\n\n    # To print the colourful output on the terminal\n    config_diff = conf_diff.ConfDiff(f"{device[\'ip\']}_before_config.cfg", f"{device[\'ip\']}_after_config.cfg")\n    print(config_diff.diff())\n\n    # To generate a HTML output file\n    html_diff = conf_diff.ConfDiff(f"{device[\'ip\']}_before_config.cfg", f"{device[\'ip\']}_after_config.cfg", "html_diff_output.html")\n    html_diff.diff()\n\n```\n\n## Issues\nPlease raise an issue or pull request if you find something wrong with this module.\n\n## Authors\n[Muhammad Rafi](https://github.com/muhammad-rafi)\n\n## License\n[Cisco Sample Code License, Version 1.1](https://developer.cisco.com/site/license/cisco-sample-code-license/)\n',
    'author': 'Muhammad Rafi',
    'author_email': 'murafi@cisco.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/muhammad-rafi/conf_diff',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
