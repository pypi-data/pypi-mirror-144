import re
import sys
import traceback
from io import StringIO
from threading import Lock
from typing import List

from colored import attr

from . import TealConfig, TealLevel


class TealPrintBuffer:
    _mutex = Lock()
    _ascii: bool = False

    def __init__(self) -> None:
        self.buffer = StringIO()
        self.indent_stack: List[TealLevel] = []

    def error(
        self,
        message: str,
        push_indent: bool = False,
        pop_indent: bool = False,
        color: str = TealConfig.colors_default.error,
        exit: bool = False,
        print_exception: bool = False,
        print_report_this: bool = False,
    ) -> None:
        """Recommendation: Only use this when an error occurs and you have to exit the program.
           Add an error message in red to the buffer. Can print the exception.
           If exit=True, it flushes all messages before exiting.
           Optionally prints a "Please report this and paste the above message"
           Call flush() to print the messages.

        Args:
            message (str): The message to print
            push_indent (bool): If messages after this should be indented by one level. Call pop_indent() to unindent
            pop_indent (bool): If messages after this should be unindented by one level. Call push_indent() to indent
            color (str): Optional color of the message, defaults to TealConfig.colors_default.error
            exit (bool): If the program should exit after printing the error. Also flushes messages
            print_exception (bool): Set to true to print an exception
            print_report_this (bool): Set to true to add an "Please report this..." message at the end
        """
        self._add_to_buffer_on_level(message, push_indent, pop_indent, color, TealLevel.error)
        if print_exception:
            exception = traceback.format_exc()
            self._add_to_buffer_on_level(exception, False, False, color, TealLevel.error)
        if print_report_this:
            self._add_to_buffer_on_level(
                "!!! Please report this and paste the above message !!!", False, False, color, TealLevel.error
            )
        if exit:
            self.flush()
            sys.exit(1)

    def warning(
        self,
        message: str,
        push_indent: bool = False,
        pop_indent: bool = False,
        color: str = TealConfig.colors_default.warning,
        exit: bool = False,
    ) -> None:
        """Add an orange warning message to the buffer.
           If exit=True, it flushes all messages before exiting.
           Call flush() to print the messages.

        Args:
            message (str): The message to print
            push_indent (bool): If messages after this should be indented by one level. Call pop_indent() to unindent
            pop_indent (bool): If messages after this should be unindented by one level. Call push_indent() to indent
            color (str): Optional color of the message, defaults to TealConfig.colors_default.warning
            exit (bool): If the program should exit after printing the warning. Also flushes messages
        """
        self._add_to_buffer_on_level(message, push_indent, pop_indent, color, TealLevel.warning, exit)

    def info(self, message: str, push_indent: bool = False, pop_indent: bool = False, color: str = "") -> None:
        """Add a message to the buffer if TealConfig.level has been set to debug/verbose/info.
           Call flush() to print the messages.

        Args:
            message (str): The message to print
            push_indent (bool): If messages after this should be indented by one level. Call pop_indent() to unindent
            pop_indent (bool): If messages after this should be unindented by one level. Call push_indent() to indent
            color (str): Optional color of the message
        """
        self._add_to_buffer_on_level(message, push_indent, pop_indent, color, TealLevel.info)

    def verbose(self, message: str, push_indent: bool = False, pop_indent: bool = False, color: str = "") -> None:
        """Add a message to the buffer if TealConfig.level has been set to debug/verbose.
           Call flush() to print the messages.

        Args:
            message (str): The message to print
            push_indent (bool): If messages after this should be indented by one level. Call pop_indent() to unindent
            pop_indent (bool): If messages after this should be unindented by one level. Call push_indent() to indent
            color (str): Optional color of the message
        """
        self._add_to_buffer_on_level(message, push_indent, pop_indent, color, TealLevel.verbose)

    def debug(self, message: str, push_indent: bool = False, pop_indent: bool = False, color: str = "") -> None:
        """Add a message to the buffer if the TealConfig.level has been set to debug.
           Call flush() to print the messages.

        Args:
            message (str): The message to print
            push_indent (bool): If messages after this should be indented by one level. Call pop_indent() to unindent
            pop_indent (bool): If messages after this should be unindented by one level. Call push_indent() to indent
            color (str): Optional color of the message
        """
        self._add_to_buffer_on_level(message, push_indent, pop_indent, color, TealLevel.debug)

    def push_indent(self, level: TealLevel) -> None:
        """Add indentation for all messages, but only if level is would be shown"""
        self.indent_stack.append(level)

    def pop_indent(self) -> None:
        """
        Remove indentation for all messages. Note that nothing will happen if push_indent() was
        called with a level that wouldn't be shown.

        For example:
            TealConfig.level = TealLevel.info
            TealPrint.push_indent(TealLevel.warning)
            TealPrint.info("Will be indented by 1 level")
            TealPrint.push_indent(TealLevel.verbose)
            TealPrint.info("Will still be indented by 1 level")
            TealPrint.pop_indent()
            TealPrint.info("Will still be indented by 1 level...")
            TealPrint.pop_indent()
            TealPrint.info("Not indentend")
        """
        self.indent_stack.pop()

    def clear_indent(self) -> None:
        """
        Removes all indentation. Note that calling pop() will throw an exception now.
        Recommended to use before exiting the app or returning from an excetpion.
        """
        self.indent_stack.clear()

    def _add_to_buffer_on_level(
        self,
        message: str,
        push_indent: bool,
        pop_indent: bool,
        color: str,
        level: TealLevel,
        exit: bool = False,
    ) -> None:
        """Prints the message if the level is equal or lower to the specified"""
        if TealConfig.level.value >= level.value:
            try:
                # Indent message
                indent_level = self._get_indent_level()
                if indent_level > 0:
                    message = "".ljust(indent_level * TealConfig.indent_by, TealConfig.indent_char) + message
                if len(color) > 0:
                    message = f"{color}{message}{attr('reset')}"

                # Remove colors if not supported
                if not TealConfig.colors_enabled or not TealConfig.unicode_enabled:
                    message = TealPrintBuffer._remove_colors_from_string(message)

                # Convert to ascii if unicode is disabled or not supported
                if not TealConfig.unicode_enabled:
                    message = TealPrintBuffer._remove_unicode_from_string(message)
                    message = message.encode("utf-8", "ignore").decode("ascii", "ignore")

                self._add_to_buffer(message)

                if exit:
                    self.flush()
                    sys.exit(1)

            except UnicodeEncodeError:
                # Some consoles can't use utf-8, encode into ascii instead, and use that
                # in the future
                TealConfig.unicode_enabled = False
                self._add_to_buffer_on_level(message, False, False, color, level, exit)

        # Always push indent
        if push_indent:
            self.push_indent(level)
        # Always pop indent
        if pop_indent:
            self.pop_indent()

    def _get_indent_level(self) -> int:
        count = 0
        for level in self.indent_stack:
            if TealConfig.level.value >= level.value:
                count += 1
        return count

    def _add_to_buffer(self, message: str) -> None:
        """Mostly used for mocking purposes"""
        self.buffer.write(message + "\n")

    def flush(self) -> None:
        """Prints the messages in the buffer"""
        self.buffer.seek(0)

        # Make sure we only print one message at a time
        TealPrintBuffer._mutex.acquire()
        try:
            print(self.buffer.read(), flush=True, end="")
        finally:
            TealPrintBuffer._mutex.release()

        self.buffer = StringIO()

    @staticmethod
    def _remove_unicode_from_string(string: str) -> str:
        """Remove all unicode characters from a string"""
        return "".join(c for c in string if ord(c) < 128)

    @staticmethod
    def _remove_colors_from_string(string: str) -> str:
        """Removes all color characters from a string"""
        return re.sub(r"\x1b\[\d+m", "", string)
