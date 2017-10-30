# Contributing guidelines

Thank you for you contribution. It's really appreciated.

Set of guidelines follows. Use your best judgment, the world is not black and white and these guidelines are not hard rules.

**Table of contents**

* [How can I contribute?](#how-can-i-contribute)
    * [Reporting bugs](#reporting-bugs)
* [Issue labels](#issue-labels)

## How can I contribute?

### Reporting bugs

#### Before submitting a bug report

* **Check** the [forum](https://forum.omz-software.com/category/5/pythonista) for a list of common issues and possible workarounds.
* **Check** wheter the issue you are experiencing is [already reported](https://github.com/omz/Pythonista-Issues/issues/). If it is already reported, you can click on the _Subscribe_ button to receive further development info or you can add more details.
* **Check** if you're using the [latest Pythonista version](https://itunes.apple.com/us/app/pythonista-3/id1085978097?ls=1&mt=8). Bug reports should be based on the latest available version. If you're using Pythonista beta version, test your issue with the latest available version from the Test Flight.

#### How do I submit a bug report?

* **Isolate problem** - The first step is to identify what the problem is. Saying "something is wrong" is not helpful. Saying what exactly is wrong, how to reproduce it, is.
* **Separate issues** - If you have multiple issues, please, file them separately.
* **Use clear and descriptive title** - title like "help system" is not helpful.
* **Steps to reproduce** - Include all steps how to reproduce your issue. More details, faster resolution. Don't just say what you did, but explain how you did it (tapping on, hw keyboard, ...).
* **Expected behavior** - If something doesn't work as expected, include what exactly should happen.
* **Sample code** - Sample code demonstrating your issue is very helpful. If it's short, include it directly in the issue. Read [Quoting code](https://help.github.com/articles/basic-writing-and-formatting-syntax/#quoting-code) to learn how to include code in the issue. [Gist](https://gist.github.com) is preferred in case your code is too long.
* **System information** - It's always good to attach system information.
* **Ask yourself** - Is my description detailed enough that everyone understands what's my problem?

#### System information

Here's an example of system information to attach (preformatted Markdown):

```
**System Information**

* Pythonista 3.1.1 (311015), Default interpreter 3.6.1
* iOS 11.0.3, model iPad, resolution (portrait) 2048.0 x 2732.0 @ 2.0
```

If you don't know from where to get this information, download and run [sysinfo.py](scripts/sysinfo.py) script.

Why? Some bugs may appear on specific device, specific iOS version and it's very helpful to know more about your system. Problem can be identified and fixed more quickly.

If you feel bad about sharing system information of your device, don't attach it. It's mandatory, but it's really helpful.

## Issue labels

* It's not required that every issue must have a label from every group
* Issue can have multiple labels from one group
* If there're no labels, issue wasn't reviewed yet

### Issue types

| Label | Open :mag_right: | Closed :mag_right: | Description |
| --- | --- | --- | --- |
| `bug` | [search][search-open-bug] | [search][search-closed-bug] | Confirmed bugs |
| `enhancement` | [search][search-open-enhancement] | [search][search-closed-enhancement] | Requests for enhancement |


### Issues components

| Label | Open :mag_right: | Closed :mag_right: | Description |
| --- | --- | --- | --- |
| `pythonista` | [search][search-open-pythonista] | [search][search-closed-pythonista] | Pythonista application itself (UI, editor, console, ...) |
| `internal-module` | [search][search-open-internal-module] | [search][search-closed-internal-module] | [Pythonista specific modules][pythonista-internal-modules] (`ui`, `console`, ...) |
| `3rd-party-module` | [search][search-open-3rd-party-module] | [search][search-closed-3rd-party-module] | [Bundled 3rd party modules][pythonista-module-index] minus [internal modules][pythonista-internal-modules] |

### Issue priorities

| Label | Open :mag_right: | Closed :mag_right: | Description |
| --- | --- | --- | --- |
| `crash` | [search][search-open-crash] | [search][search-closed-crash] | Pythonista crashes |
| `major` | [search][search-open-major] | [search][search-closed-major] | Serious issue, no workarounds, ... |
| normal | [search][search-open-normal] | [search][search-closed-normal] | This isn't actually a label, any issue without `major`, `minor` or `crash` labels is considered as an issue with normal priority |
| `minor` | [search][search-open-minor] | [search][search-closed-minor] | Nice to have feature |

[search-open-bug]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Abug
[search-closed-bug]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Abug
[search-open-enhancement]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement
[search-closed-enhancement]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Aenhancement
[search-open-pythonista]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Apythonista
[search-closed-pythonista]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Apythonista
[search-open-internal-module]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Ainternal-module
[search-closed-internal-module]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Ainternal-module
[search-open-3rd-party-module]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3A3rd-party-module
[search-closed-3rd-party-module]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3A3rd-party-module
[search-open-crash]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Acrash
[search-closed-crash]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Acrash
[search-open-major]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Amajor
[search-closed-major]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Amajor
[search-open-minor]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Aminor
[search-closed-minor]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Aminor
[search-open-normal]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen%20is%3Aissue%20-label%3Amajor%20-label%3Aminor%20-label%3Acrash
[search-closed-normal]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed%20is%3Aissue%20-label%3Amajor%20-label%3Aminor%20-label%3Acrash
[pythonista-internal-modules]: http://omz-software.com/pythonista/docs/ios/index.html
[pythonista-module-index]: http://omz-software.com/pythonista/docs/py-modindex.html