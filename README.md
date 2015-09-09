# fluent-logger-sublimetext

fluentd logging tool for sublime text editor

## Install

You can install from [Package Control](https://sublime.wbond.net/).

__Package Control: Install Package__ > Select __fluent-logger-sublimetext__

## Settings

|fieldname|default|description|
|:----:|:----:|:----:|
|tagprefix|"sublime"|tag prefix of fluentd|
|host|"localhost"|host of fluentd|
|port|24224|port of fluentd|

## Records

Those fields are shared with all records

|fieldname|description|example data|
|:----:|:----:|:----:|
|version|the version number of editor|3083|
|platform|the platform, which may be "osx", "linux" or "windows"|osx|
|arch|the CPU architecture, which may be "x32" or "x64"|x64|
|file_name|the full name file the file associated with the buffer, or None if it doesn't exist on disk|example.py|
|size|number of character in the file|4349|
|viewport_extent|the width and height of the viewport|[768.0, 769.0]|
|layout_extent|the width and height of the layout|[1092.0, 3402.0]|
|line_height|the light height used in the layout|27.0|
|em_width|the typical character width used in the layout|12.0|
|change_count|the current change count|34|
|encoding|the encoding currently associated with the file|UTF-8|
|line_endings|the line endings used by the current file|Unix|
|overwrite_status|the overwrite status, which the user normally toggles via the insert key|false|
|syntax|the syntax file name|Packages/Python/Python.tmLanguage|

### sublime.on_new

Called when a new buffer is created.

### sublime.on_clone

Called when a view is cloned from an existing one.

### sublime.on_load

Called when the file is finished loading.

### sublime.on_pre_close

Called when a view is about to be closed.

### sublime.on_close

Called when a view is closed.

### sublime.on_pre_save

Called just before a view is saved.

### sublime.on_post_save

Called after a view has been saved.

### sublime.on_modified

Called after changes have been made to a view.

### sublime.on_selection_modified

Called after the selection has been modified in a view.

### sublime.on_activated

Called when a view gains input focus.

### sublime.on_deactivated

Called when a view loses input focus.

|fieldname|description|example data|
|:----:|:----:|:----:|
|active_time|the seconds of time, which the view actived|2.293574810028076|

### sublime.on_text_command

Called when a text command is issued.

|fieldname|description|example data|
|:----:|:----:|:----:|
|command_name|the name of running command|open_dir|
|args|the arguments of running command|{"dir":"$packages"}|

### sublime.on_window_command

Called when a window command is issued.

|fieldname|description|example data|
|:----:|:----:|:----:|
|command_name|the name of running command|open_dir|
|args|the arguments of running command|{"dir":"$packages"}|

### sublime.post_text_command

Called after a text command has been executed.

|fieldname|description|example data|
|:----:|:----:|:----:|
|command_name|the name of running command|open_dir|
|args|the arguments of running command|{"dir":"$packages"}|

### sublime.post_window_command

Called after a window command has been executed.

|fieldname|description|example data|
|:----:|:----:|:----:|
|command_name|the name of running command|open_dir|
|args|the arguments of running command|{"dir":"$packages"}|

### sublime.on_query_context

Called when determining to trigger a key binding with the given context key.

|fieldname|description|example data|
|:----:|:----:|:----:|
|key|the name of context key|snake_running|
|operator|the name of operator name, which may be "OP_EQUAL", "OP_NOT_EQUAL", "OP_REGEX_MATCH", "OP_NOT_REGEX_MATCH", "OP_REGEX_CONTAINS" or "OP_NOT_REGEX_CONTAINS"|OP_EQUAL|
|operand|the operand|true|
|match_all|it should be used if the context relates to the selections: does every selection have to match|false|

### sublime.on_query_completions

Called when the completion list is requested.

|fieldname|description|example data|
|:----:|:----:|:----:|
|prefix|the text entered so far|dat|
|locations|array of points in view where the completion should be inserted|[4228]|

## License

MIT
