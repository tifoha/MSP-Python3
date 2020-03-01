

import os
import sys

print('Creating .tar.gz and .whl')
exit_status = os.system('python3 setup.py sdist bdist_wheel')

if not exit_status == 0:
    import traceback
    traceback.print_exc()
    sys.exit(exit_status)

print()

print('Uploading')
os.system('python3 -m twine upload --skip-existing dist/*')
