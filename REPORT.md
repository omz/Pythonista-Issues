# How to write a good bug report?

## Isolate problem

The first step is to identify what the problem is. Saying "something is wrong" is not helpful.
saying what exactly is wrong, how to reproduce it, is.

## Latest version

Check if you are using the [latest version](https://itunes.apple.com/us/app/pythonista-3/id1085978097?ls=1&mt=8).
Bug reports should be based on the latest available version.

If you're using Pythonista beta version, test your issue with the latest available version from the Test Flight.

## Known issue

Please, check whether the issue you are experiencing is [already reported](https://github.com/omz/Pythonista-Issues/issues/).
If it is already reported, you can click on the _Subscribe_ button to receive further development info or you can add more details.
Otherwise [file a new issue](https://github.com/omz/Pythonista-Issues/issues/new).

## Separate issues

If you have multiple issues, please, file them separately.

## System information

It's always good to attach system information. Your issue can be iPhone, iPad, iOS, Python interpreter version specific.
Example (preformatted Markdown for GitHub issues):

```
**System Information**

* Pythonista 3.1.1 (311015), Default interpreter 3.6.1
* iOS 11.0.3, model iPad, resolution (portrait) 2048.0 x 2732.0 @ 2.0
```

If you don't know from where to get this information, download and run [sysinfo.py](scripts/sysinfo.py) script.

## Steps to reproduce

Include all steps how to reproduce your issue. More details, faster resolution.

## Sample code

Sample code demonstrating your issue is very helpful. If it's short, include it directly in the issue.
Read [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) to learn how to include
code in the issue.

[Gist](https://gist.github.com) is preferred in case your code is long.
