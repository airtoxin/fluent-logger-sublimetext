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

    def _get_data_from_view(self, view):
        window = view.window()
        return {
            "version": sublime.version(),
            "platform": sublime.platform(),
            "arch": sublime.arch(),
            "file_name": view.file_name(),
            "size": view.size(),
            "viewport_extent": view.viewport_extent(),
            "layout_extent": view.layout_extent(),
            "line_height": view.line_height(),
            "em_width": view.em_width(),
            "change_count": view.change_count(),
            "encoding": view.encoding(),
            "line_endings": view.line_endings(),
            "overwrite_status": view.overwrite_status(),
            "syntax": view.settings().get('syntax'),
            "project": window.project_data() if hasattr(window, 'project_data') else None,
            "folders": window.folders()
        }

    def on_new(self, view):
        event.Event('on_new', self._get_data_from_view(view))

    def on_clone(self, view):
        event.Event('on_clone', self._get_data_from_view(view))

    def on_load(self, view):
        event.Event('on_load', self._get_data_from_view(view))

    def on_pre_close(self, view):
        event.Event('on_pre_close', self._get_data_from_view(view))

    def on_close(self, view):
        event.Event('on_close', self._get_data_from_view(view))

    def on_pre_save(self, view):
        event.Event('on_pre_save', self._get_data_from_view(view))

    def on_post_save(self, view):
        event.Event('on_post_save', self._get_data_from_view(view))

    def on_modified(self, view):
        event.Event('on_modified', self._get_data_from_view(view))

    def on_selection_modified(self, view):
        event.Event('on_selection_modified', self._get_data_from_view(view))

    def on_activated(self, view):
        event.Event('on_activated', self._get_data_from_view(view))

    def on_deactivated(self, view):
        event.Event('on_deactivated', self._get_data_from_view(view))

    def on_text_command(self, view, command_name, args):
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('on_text_command', data)

    def on_window_command(self, window, command_name, args):
        view = window.active_view()
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('on_window_command', data)

    def post_text_command(self, view, command_name, args):
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('post_text_command', data)

    def post_window_command(self, window, command_name, args):
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('post_window_command', data)

    def on_query_context(self, view, key, operator, operand, match_all):
        data = self._get_data_from_view(view)
        data['key'] = key
        data['operator'] = operator
        data['operand'] = operand
        data['match_all'] = match_all
        event.Event('on_query_context', data)

    def on_query_completions(self, view, prefix, locations):
        data = self._get_data_from_view(view)
        data['prefix'] = prefix
        data['locations'] = locations
        event.Event('on_query_completions', data)
