#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

import os
import sys
from time import time

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(PLUGIN_DIR, 'libs'))

from fluent import sender, event

SETTINGS_FILE = 'fluent-logger.sublime-settings'

class FluentLoggerSublimetext(sublime_plugin.EventListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.settings = sublime.load_settings(SETTINGS_FILE)
        self.op_dict = {
            sublime.OP_EQUAL: 'OP_EQUAL',
            sublime.OP_NOT_EQUAL: 'OP_NOT_EQUAL',
            sublime.OP_REGEX_MATCH: 'OP_REGEX_MATCH',
            sublime.OP_NOT_REGEX_MATCH: 'OP_NOT_REGEX_MATCH',
            sublime.OP_REGEX_CONTAINS: 'OP_REGEX_CONTAINS',
            sublime.OP_NOT_REGEX_CONTAINS: 'OP_NOT_REGEX_CONTAINS'
        }
        sender.setup(
            str(self.settings.get('tagprefix')),
            host=str(self.settings.get('host')),
            port=int(self.settings.get('port'))
        )

    def _get_data_from_view(self, view):
        window = view.window()
        activated = self.settings.get('activated_data')
        data = {}

        if activated["version"]: data["version"] = sublime.version()
        if activated["platform"]: data["platform"] = sublime.platform()
        if activated["arch"]: data["arch"] = sublime.arch()
        if activated["file_name"]: data["file_name"] = view.file_name()
        if activated["size"]: data["size"] = view.size()
        if activated["viewport_extent"]: data["viewport_extent"] = view.viewport_extent()
        if activated["layout_extent"]: data["layout_extent"] = view.layout_extent()
        if activated["line_height"]: data["line_height"] = view.line_height()
        if activated["em_width"]: data["em_width"] = view.em_width()
        if activated["change_count"]: data["change_count"] = view.change_count()
        if activated["encoding"]: data["encoding"] = view.encoding()
        if activated["line_endings"]: data["line_endings"] = view.line_endings()
        if activated["overwrite_status"]: data["overwrite_status"] = view.overwrite_status()
        if activated["syntax"]: data["syntax"] = view.settings().get('syntax')

        return data

    def on_new(self, view):
        if not self.settings.get('activated_events')['on_new']: return
        event.Event('on_new', self._get_data_from_view(view))

    def on_clone(self, view):
        if not self.settings.get('activated_events')['on_clone']: return
        event.Event('on_clone', self._get_data_from_view(view))

    def on_load(self, view):
        if not self.settings.get('activated_events')['on_load']: return
        event.Event('on_load', self._get_data_from_view(view))

    def on_pre_close(self, view):
        if not self.settings.get('activated_events')['on_pre_close']: return
        event.Event('on_pre_close', self._get_data_from_view(view))

    def on_close(self, view):
        if not self.settings.get('activated_events')['on_close']: return
        event.Event('on_close', self._get_data_from_view(view))

    def on_pre_save(self, view):
        if not self.settings.get('activated_events')['on_pre_save']: return
        event.Event('on_pre_save', self._get_data_from_view(view))

    def on_post_save(self, view):
        if not self.settings.get('activated_events')['on_post_save']: return
        event.Event('on_post_save', self._get_data_from_view(view))

    def on_modified(self, view):
        if not self.settings.get('activated_events')['on_modified']: return
        event.Event('on_modified', self._get_data_from_view(view))

    def on_selection_modified(self, view):
        if not self.settings.get('activated_events')['on_selection_modified']: return
        event.Event('on_selection_modified', self._get_data_from_view(view))

    def on_activated(self, view):
        self.active_from = time()

        if not self.settings.get('activated_events')['on_activated']: return
        event.Event('on_activated', self._get_data_from_view(view))

    def on_deactivated(self, view):
        data = self._get_data_from_view(view)
        active_time = time() - self.active_from
        data['active_time'] = active_time
        self.active_from = None

        if not self.settings.get('activated_events')['on_deactivated']: return
        event.Event('on_deactivated', data)

    def on_text_command(self, view, command_name, args):
        if not self.settings.get('activated_events')['on_text_command']: return
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('on_text_command', data)

    def on_window_command(self, window, command_name, args):
        if not self.settings.get('activated_events')['on_window_command']: return
        view = window.active_view()
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('on_window_command', data)

    def post_text_command(self, view, command_name, args):
        if not self.settings.get('activated_events')['post_text_command']: return
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('post_text_command', data)

    def post_window_command(self, window, command_name, args):
        if not self.settings.get('activated_events')['post_window_command']: return
        data = self._get_data_from_view(view)
        data['command_name'] = command_name
        data['args'] = args
        event.Event('post_window_command', data)

    def on_query_context(self, view, key, operator, operand, match_all):
        if not self.settings.get('activated_events')['on_query_context']: return
        data = self._get_data_from_view(view)
        data['key'] = key
        data['operator'] = self.op_dict[operator]
        data['operand'] = operand
        data['match_all'] = match_all
        event.Event('on_query_context', data)

    def on_query_completions(self, view, prefix, locations):
        if not self.settings.get('activated_events')['on_query_completions']: return
        data = self._get_data_from_view(view)
        data['prefix'] = prefix
        data['locations'] = locations
        event.Event('on_query_completions', data)
