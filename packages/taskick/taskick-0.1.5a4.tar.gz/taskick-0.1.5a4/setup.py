# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taskick']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'schedule>=1.1.0,<2.0.0', 'watchdog>=2.1.6,<3.0.0']

setup_kwargs = {
    'name': 'taskick',
    'version': '0.1.5a4',
    'description': '',
    'long_description': '# Taskick\n\nTaskick is an event-driven Python library that automatically executes scripts or any commands.\nIt not only automates tedious routine tasks and operations, but also makes it easy to develop [applications](#toy-example).\n\nUsers can concentrate on developing scripts to run, and simply create a configuration file (YAML) to automatically execute scripts triggered by any date, time, or event.\n\nThe main features of Taskick are as follows\n\n- Script execution timing can be managed in a configuration file (YAML).\n- Can specify datetime and directory/file operations as task triggers.\n- Execution schedules can be specified in Crontab format.\n- [Watchdog](https://github.com/gorakhargosh/watchdog) is used to detect directory and file operations. It is also possible to specify any [events API](https://python-watchdog.readthedocs.io/en/stable/api.html#module-watchdog.events) on the configuration file.\n\n## Installation\n\n```shell\n$ pip install taskick\n$ python -m taskick\nTaskick 0.1.5a4\nusage: __main__.py [-h] [--verbose] [--version] [--file FILE [FILE ...]]\n                   [--log_config LOG_CONFIG]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --verbose, -v         increase the verbosity of messages: \'-v\' for normal\n                        output, \'-vv\' for more verbose output and \'-vvv\' for\n                        debug\n  --version, -V         display this application version and exit\n  --file FILE [FILE ...], -f FILE [FILE ...]\n                        select task configuration files (YAML)\n  --log_config LOG_CONFIG, -l LOG_CONFIG\n                        select a logging configuration file (YAML or other)\n$ python -m taskick -V\nTaskick 0.1.5a4\n```\n\n## Toy Example\n\nHere is a toy-eample that converts a PNG image to PDF.\nIn this sample, Taskick starts a script when it detects that a PNG image has been saved to a specific folder.\nThe script converts the PNG to PDF and saves it in another folder.\nFor more information, please see the [project page](https://github.com/atsuyaide/taskick-example).\n\nFirst, clone [taskick-example](https://github.com/atsuyaide/taskick-example).\n\n```shell\ngit clone https://github.com/atsuyaide/taskick-example.git\n```\n\nGo to the cloned directory and start Taskick.\n\n```shell\n$ cd taskick-example\n$ pip install -r requirements.txt\n$ python -m taskick -f welcome.yaml main.yaml -vv\nINFO:taskick:Loading: welcome.yaml\nINFO:taskick:Processing: Welcome_taskick\nINFO:taskick:Startup execution option is selected.\nINFO:taskick:Registered: Welcome_taskick\nINFO:taskick:Loading: main.yaml\nINFO:taskick:Processing: remove_files_in_input_folder\nINFO:taskick:Startup execution option is selected.\nINFO:taskick:Registered: remove_files_in_input_folder\nINFO:taskick:Processing: png2pdf\nINFO:taskick:Registered: png2pdf\nINFO:taskick:Executing: Welcome_taskick\nINFO:taskick:"remove_files_in_input_folder" is waiting for "Welcome_taskick" to finish.\nSun Mar 27 00:10:45 JST 2022 Welcome to Taskick!\nwaiting 5 seconds...\nINFO:taskick:Executing: remove_files_in_input_folder\n```\n\nWhen a PNG image is saved in the input folder, a converted PDF file is output in the output folder.\nFiles in the input folder are automatically deleted at startup or every minute.\n\n\n![png2gif](https://github.com/atsuyaide/taskick/raw/main/png_to_pdf.gif)\n\nThese tasks are controlled by `main.yaml` and managed by Taskick. These tasks are controlled by Taskick, and the behavior of the tasks is controlled by `main.yaml` and `welcome.yaml`.\n',
    'author': 'Atsuya Ide',
    'author_email': 'atsuya.ide528@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/atsuyaide/taskick',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
