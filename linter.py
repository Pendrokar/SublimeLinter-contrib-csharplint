#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jānis Lukss
# Copyright (c) 2014 Jānis Lukss
#
# License: MIT
#

"""This module exports the Csharplint plugin class."""

import sublime
import shlex

# for completionscommon functions
import re
import glob
import os

from SublimeLinter.lint import Linter, util

class Csharplint(Linter):

    """Provides an interface to csharplint."""

    syntax = ("c#", "unityc#")

    base_cmd = (
        "gmcs.bat "
        " *"
        " -target:library"
        " -out:/tmp/errorcheck.dll"
        #" -out:stdout" doesn't work like that
        #" sdk:3.5" # Unity uses .NET 3.5
        #" -r:./*.dll" # Recursively add all libraries within the folder of file
    )
    regex = (
        r'^(?P<filename>.+\.cs)\((?P<line>\d+),(?P<col>\d+)\): (?:(?P<error>error)|(?P<warning>warning)) \w+: (?P<message>.+)'
    )
    tempfile_suffix = '.cs'
    error_stream = util.STREAM_BOTH  # errors are on stderr
    defaults = {
        '--filter=,': '',
    }
    #comment_re = r'\s*/[/*]'
    inline_settings = None
    inline_overrides = 'filter'

    executable = None
    executable_path = '<builtin>'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    multiline = False
    line_col_base = (1, 1)
    selectors = {}
    word_re = None

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method so that the error:
            No copyright message found.
            You should have a line: "Copyright [year] <Copyright Owner>"  [legal/copyright] [5]
        that appears on line 0 (converted to -1 because of line_col_base), can be displayed.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is not None and line == -1 and message:
            line = 0

        return match, line, col, error, warning, message, near

    def cmd(self):
        """
        Return the command line to execute.

        We override this method, so we can add extra flags and include paths
        based on the 'include_dirs' and 'extra_flags' settings.

        """

        result = self.base_cmd

        extra = []
        extra = self.get_setting("completesharp_assemblies", [])
        if len(extra) == 0:
            return result

        #result += ","
        result += " -r:"

        newextra = []
        window = sublime.active_window()
        for path in extra:
            newextra.extend(glob.glob(self.expand_path(path, window, False)))
        extra = newextra
        cmd = ""
        q = "\""

        result += ','.join([shlex.quote(newextra) for newextra in extra])
        #print("Result: $ '" + result + "'")
        #result += "%s%s%s" % (q, ";;--;;".join(extra), q)
        #
        result += " -nostdlib" # Unity has its own

        return result

    # following are copied from completionscommon package:
    def get_setting(self, key, default=None):
        try:
            s = sublime.active_window().active_view().settings()
            if s.has(key):
                return s.get(key)
        except:
            pass
        return self.get_view_settings().get(key, default)

    def expand_path(self, value, window=None, checkExists=True):
        if window == None:
            # Views can apparently be window less, in most instances getting
            # the active_window will be the right choice (for example when
            # previewing a file), but the one instance this is incorrect
            # is during Sublime Text 2 session restore. Apparently it's
            # possible for views to be windowless then too and since it's
            # possible that multiple windows are to be restored, the
            # "wrong" one for this view might be the active one and thus
            # ${project_path} will not be expanded correctly.
            #
            # This will have to remain a known documented issue unless
            # someone can think of something that should be done plugin
            # side to fix this.
            window = sublime.active_window()

        get_existing_files = \
            lambda m: [path \
                for f in window.folders() \
                for path in [os.path.join(f, m.group('file'))] \
                if checkExists and os.path.exists(path) or not checkExists
            ]
        value = re.sub(r'\${project_path:(?P<file>[^}]+)}', lambda m: len(get_existing_files(m)) > 0 and get_existing_files(m)[0] or m.group('file'), value)
        value = re.sub(r'\${env:(?P<variable>[^}]+)}', lambda m: os.getenv(m.group('variable')) if os.getenv(m.group('variable')) else "%s_NOT_SET" % m.group('variable'), value)
        value = re.sub(r'\${home}', os.getenv('HOME') if os.getenv('HOME') else "HOME_NOT_SET", value)
        value = re.sub(r'\${folder:(?P<file>[^}]+)}', lambda m: os.path.dirname(m.group('file')), value)
        value = value.replace('\\', '/')

        return value
