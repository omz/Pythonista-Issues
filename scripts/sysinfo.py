import plistlib
import sys
import platform
from pathlib import Path
from objc_util import ObjCClass, on_main_thread
import clipboard


def get_pythonista_version_info():
    version = None
    bundle_version = None

    try:
        plist = plistlib.loads((Path(sys.executable).parent /  'Info.plist').read_bytes())
        version = plist['CFBundleShortVersionString']
        bundle_version = plist['CFBundleVersion']

    except Exception:
        pass

    return 'Pythonista {} ({})'.format(version or 'N/A', bundle_version or 'N/A')


def get_python_interpreter_info():
    return 'Default interpreter {}.{}.{}'.format(*sys.version_info)


def get_device_info():
    device = ObjCClass('UIDevice').currentDevice()
    main_screen = ObjCClass('UIScreen').mainScreen()
    native_size = main_screen.nativeBounds().size

    return 'iOS {}, model {}, resolution (portrait) {} x {} @ {}'.format(
        device.systemVersion(), platform.machine(),
        native_size.width, native_size.height, main_screen.nativeScale()
    )


@on_main_thread  # clipboard.set or freeze
def main():
    separator = '--- SYSTEM INFORMATION ---'

    info = '\n'.join([
        '**System Information**',
        '',
        '* {}, {}'.format(get_pythonista_version_info(), get_python_interpreter_info()),
        '* {}'.format(get_device_info()),
    ])

    print('\n'.join([separator, info, separator]))
    print('Please, attach everything between {} to your GitHub issue, many thanks.'.format(separator))
    clipboard.set(info)
    print('System information was just stored in the system clipboard. You can paste it with Cmd V.')


if __name__ == '__main__':
    main()
