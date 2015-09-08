#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

import os
import sys
from types import MethodType

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(PLUGIN_DIR, 'libs'))

from fluent import sender, event

SETTINGS_FILE = 'fluent-logger-sublimetext.sublime-settings'

class FluentLoggerSublimetext(sublime_plugin.EventListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.settings = sublime.load_settings(SETTINGS_FILE)
        sender.setup(
            str(self.settings.get('tagprefix')),
            host=str(self.settings.get('host')),
            port=int(self.settings.get('port'))
        )

    def on_new(self, view):
        event.Event('on_new', {})

    def on_clone(self, view):
        event.Event('on_clone', {})

    def on_load(self, view):
        event.Event('on_load', {})

    def on_pre_close(self, view):
        event.Event('on_pre_close', {})

    def on_close(self, view):
        event.Event('on_close', {})

    def on_pre_save(self, view):
        event.Event('on_pre_save', {})

    def on_post_save(self, view):
        event.Event('on_post_save', {})

    def on_modified(self, view):
        event.Event('on_modified', {})

    def on_selection_modified(self, view):
        event.Event('on_selection_modified', {})

    def on_activated(self, view):
        event.Event('on_activated', {})

    def on_deactivated(self, view):
        event.Event('on_deactivated', {})

    def on_text_command(self, view, command_name, args):
        event.Event('on_text_command', {})

    def on_window_command(self, window, command_name, args):
        event.Event('on_window_command', {})

    def post_text_command(self, view, command_name, args):
        event.Event('post_text_command', {})

    def post_window_command(self, window, command_name, args):
        event.Event('post_window_command', {})

    def on_query_context(self, view, key, operator, operand, match_all):
        event.Event('on_query_context', {})

