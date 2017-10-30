# Contributing guidelines

Thank you for you contribution. It's really appreciated.

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
* **System information** - It's always good to attach system information. Your issue can be iPhone, iPad, iOS, Python interpreter version specific. Example (preformatted Markdown for GitHub issues):

```
**System Information**

* Pythonista 3.1.1 (311015), Default interpreter 3.6.1
* iOS 11.0.3, model iPad, resolution (portrait) 2048.0 x 2732.0 @ 2.0
```

If you don't know from where to get this information, download and run [sysinfo.py](scripts/sysinfo.py) script.

## Issue labels

### Type of issue

| Label | Open :mag_right: | Closed :mag_right: Description |
| --- | --- | --- | --- |
| `bug` | [search][search-open-bug] | [search][search-closed-bug] | Confirmed bugs |
| `enhancement` | [search][search-open-enhancement] | [search][search-closed-enhancement] | Requests for enhancement |

[search-open-bug]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Abug
[search-closed-bug]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Abug
[search-open-enhancement]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement
[search-closed-enhancement]: https://github.com/omz/Pythonista-Issues/issues?q=is%3Aclosed+is%3Aissue+label%3Aenhancement
