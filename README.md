SublimeLinter-contrib-csharplint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-csharplint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-csharplint)

A linter(software) called 'csharplint' does not exist, this simply uses Mono or the default .NET framework available on Windows in error checking mode.

![C# error example](https://lh5.googleusercontent.com/-8SLnmiT3Uzw/VD1Wzt1czQI/AAAAAAAABbg/a63CSip0xt0/w813-h396-no/csharplinter.png)

![Unity C# Warning](https://lh4.googleusercontent.com/-9TlxxCqwPoU/VD1Wzhr9PhI/AAAAAAAABbc/9gxZ9ViXMMc/w895-h398-no/unitycsharplinter.png)

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that Mono or the default .NET framework is installed on your system. Mono installations that come with software may also be used, like in the case of Unity 3D.

### Linter configuration
In order for `csharplint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `csharplint`, you can proceed to install the SublimeLinter-contrib-csharplint plugin if it is not yet installed.

Currently the package is set very specifically for a Window's user and has no configuration options. Please modify at the linter.py file according to your needs.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control*(Unavailable)*, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `csharplint`. Among the entries you should see `SublimeLinter-contrib-csharplint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-csharplint provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline][inline-settings].

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|foo|Something.|&#10003;| |
|bar|Something else.| |&#10003;|

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
