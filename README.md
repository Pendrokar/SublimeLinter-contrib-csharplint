SublimeLinter-contrib-csharplint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-csharplint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-csharplint)

A linter(software) called 'csharplint' does not exist, this simply uses Mono or the C# framework available on Windows.

![C# error example](https://lh5.googleusercontent.com/-8SLnmiT3Uzw/VD1Wzt1czQI/AAAAAAAABbg/a63CSip0xt0/w813-h396-no/csharplinter.png)

![Unity C# Warning](https://lh4.googleusercontent.com/-9TlxxCqwPoU/VD1Wzhr9PhI/AAAAAAAABbc/9gxZ9ViXMMc/w895-h398-no/unitycsharplinter.png)

## Everything after this sentence is the default README that is created by Sublime Linter 3:

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `csharplint` is installed on your system. To install `csharplint`, do the following:

1. Install Other.

1. Install `csharplint` by typing the following in a terminal:
   ```
   <package manager> install csharplint
   ```


**Note:** This plugin requires `csharplint` __version__ or later.

### Linter configuration
In order for `csharplint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `csharplint`, you can proceed to install the SublimeLinter-contrib-csharplint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `csharplint`. Among the entries you should see `SublimeLinter-contrib-csharplint`. If that entry is not highlighted, use the keyboard or mouse to select it.

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
