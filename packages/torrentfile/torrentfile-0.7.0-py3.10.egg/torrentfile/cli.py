#! /usr/bin/python3
# -*- coding: utf-8 -*-

#####################################################################
# THE SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#####################################################################
"""
Command Line Interface for TorrentFile project.

This module provides the primary command line argument parser for
the torrentfile package. The main_script function is automatically
invoked when called from command line, and parses accompanying arguments.

Functions:
    main_script: process command line arguments and run program.
"""

import logging
import sys
from argparse import ArgumentParser, HelpFormatter

from torrentfile import (VERSION, create, edit, info, magnet, recheck,
                         select_action)


def activate_logger():
    """
    Activate the builtin logging mechanism when passed debug flag from CLI.
    """
    logger = logging.getLogger()
    file_handler = logging.FileHandler(
        "torrentfile.log", mode="a+", encoding="utf-8"
    )
    console_handler = logging.StreamHandler(stream=sys.stderr)
    file_formatter = logging.Formatter(
        "%(asctime)s %(levelno)s %(module)s %(message)s",
        datefmt="%m-%d %H:%M:%S",
        style="%",
    )
    stream_formatter = logging.Formatter(
        "%(asctime)s %(levelno)s %(module)s %(message)s",
        datefmt="%m-%d %H:%M:%S",
        style="%",
    )
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(stream_formatter)
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.debug("Debug: ON")


class TorrentFileHelpFormatter(HelpFormatter):
    """
    Formatting class for help tips provided by the CLI.

    Subclasses Argparse.HelpFormatter.
    """

    def __init__(self, prog, width=45, max_help_positions=35):
        """
        Construct HelpFormat class for usage output.

        Parameters
        ----------
        prog : str
            Name of the program.
        width : int
            Max width of help message output.
        max_help_positions : int
            max length until line wrap.
        """
        super().__init__(
            prog, width=width, max_help_position=max_help_positions
        )

    def _split_lines(self, text, _):
        """
        Split multiline help messages and remove indentation.

        Parameters
        ----------
        text : str
            text that needs to be split
        _ : int
            max width for line.
        """
        lines = text.split("\n")
        return [line.strip() for line in lines if line]

    def _format_text(self, text):
        """
        Format text for cli usage messages.

        Parameters
        ----------
        text : str
            Pre-formatted text.

        Returns
        -------
        str
            Formatted text from input.
        """
        text = text % dict(prog=self._prog) if "%(prog)" in text else text
        text = self._whitespace_matcher.sub(" ", text).strip()
        return text + "\n\n"

    def _join_parts(self, part_strings):
        """
        Combine different sections of the help message.

        Parameters
        ----------
        part_strings : list
            List of argument help messages and headers.

        Returns
        -------
        str
            Fully formatted help message for CLI.
        """
        parts = self.format_headers(part_strings)
        return super()._join_parts(parts)

    @staticmethod
    def format_headers(parts):
        """
        Format help message section headers.

        Parameters
        ----------
        parts : list
            List of individual lines for help message.

        Returns
        -------
        list
            Input list with formatted section headers.
        """
        if parts and parts[0].startswith("usage:"):
            parts[0] = "Usage\n=====\n  " + parts[0][6:]
        headings = [i for i in range(len(parts)) if parts[i].endswith(":\n")]
        for i in headings[::-1]:
            parts[i] = parts[i][:-2].title()
            underline = "".join(["\n", "-" * len(parts[i]), "\n"])
            parts.insert(i + 1, underline)
        return parts


def execute(args=None):
    """
    Initialize Command Line Interface for torrentfile.

    Parameters
    ----------
    args : list
        Commandline arguments. default=None
    """
    if not args:
        if sys.argv[1:]:
            args = sys.argv[1:]
        else:
            args = ["-h"]

    parser = ArgumentParser(
        "torrentfile",
        description=(
            "Command line tools for creating, editing, checking and "
            "interacting with Bittorrent metainfo files"
        ),
        prefix_chars="-",
        formatter_class=TorrentFileHelpFormatter,
        conflict_handler="resolve",
    )

    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        dest="interactive",
        help="select program options interactively",
    )

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"torrentfile v{VERSION}",
        help="show program version and exit",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="debug",
        help="output debug information",
    )

    subparsers = parser.add_subparsers(
        title="Actions",
        dest="command",
        metavar="<create> <edit> <magnet> <recheck>",
    )

    create_parser = subparsers.add_parser(
        "c",
        help="""
        Create a torrent meta file.
        """,
        prefix_chars="-",
        aliases=["create", "new"],
        formatter_class=TorrentFileHelpFormatter,
    )

    create_parser.add_argument(
        "-a",
        "--announce",
        action="store",
        dest="announce",
        metavar="<url>",
        nargs="+",
        default=[],
        help="Alias for -t/--tracker",
    )

    create_parser.add_argument(
        "-p",
        "--private",
        action="store_true",
        dest="private",
        help="Create a private torrent file",
    )

    create_parser.add_argument(
        "-s",
        "--source",
        action="store",
        dest="source",
        metavar="<source>",
        help="Useful for cross-seeding",
    )

    create_parser.add_argument(
        "-m",
        "--magnet",
        action="store_true",
        dest="magnet",
        help="Output Magnet Link after creation completes",
    )

    create_parser.add_argument(
        "-c",
        "--comment",
        action="store",
        dest="comment",
        metavar="<comment>",
        help="Include a comment in file metadata",
    )

    create_parser.add_argument(
        "-o",
        "--out",
        action="store",
        dest="outfile",
        metavar="<path>",
        help="Output path for created .torrent file",
    )

    create_parser.add_argument(
        "-t",
        "--tracker",
        action="store",
        dest="tracker",
        metavar="<url>",
        nargs="+",
        default=[],
        help="""One or more Bittorrent tracker announce url(s).""",
    )

    create_parser.add_argument(
        "--noprogress",
        action="store_true",
        dest="noprogress",
        help="""
        Disable showing the progress bar during torrent creation.
        (Minimially improves performance of torrent file creation.)
        """,
    )

    create_parser.add_argument(
        "--meta-version",
        default="1",
        choices=["1", "2", "3"],
        action="store",
        dest="meta_version",
        metavar="<int>",
        help="""
        Bittorrent metafile version.
        Options = 1, 2 or 3.
        (1) = Bittorrent v1 (Default)
        (2) = Bittorrent v2
        (3) = Bittorrent v1 & v2 hybrid
        """,
    )

    create_parser.add_argument(
        "--piece-length",
        action="store",
        dest="piece_length",
        metavar="<int>",
        help="""
        Number of bytes for each chunk of data. (Default: None)
        Acceptable input values include integers 14-24, which
        are interpreted as the exponent for 2ⁿ, or any perfect
        power of two integer between 16Kib and 16MiB (inclusive).
        Examples:: [--piece-length 14] [--piece-length 16777216]
        """,
    )

    create_parser.add_argument(
        "-w",
        "--web-seed",
        action="store",
        dest="url_list",
        metavar="<url>",
        nargs="+",
        help="""
        One or more url(s) linking to a hosting the torrent contents.
        """,
    )

    create_parser.add_argument(
        "content",
        action="store",
        metavar="<content>",
        nargs="?",
        help="Path to content file or directory",
    )

    create_parser.set_defaults(func=create)

    edit_parser = subparsers.add_parser(
        "e",
        help="""
        Edit existing torrent meta file.
        """,
        aliases=["edit"],
        prefix_chars="-",
        formatter_class=TorrentFileHelpFormatter,
    )

    edit_parser.add_argument(
        "metafile",
        action="store",
        help="path to *.torrent file",
        metavar="<*.torrent>",
    )

    edit_parser.add_argument(
        "--tracker",
        action="store",
        dest="announce",
        metavar="<url>",
        nargs="+",
        help="""
        Replace current list of tracker/announce urls with one or more space
        seperated Bittorrent tracker announce url(s).
        """,
    )

    edit_parser.add_argument(
        "--web-seed",
        action="store",
        dest="url_list",
        metavar="<url>",
        nargs="+",
        help="""
        Replace current list of web-seed urls with one or more url(s)
        """,
    )

    edit_parser.add_argument(
        "--private",
        action="store_true",
        help="Make torrent private.",
        dest="private",
    )

    edit_parser.add_argument(
        "--comment",
        help="Replaces any existing comment with <comment>",
        metavar="<comment>",
        dest="comment",
        action="store",
    )

    edit_parser.add_argument(
        "--source",
        action="store",
        dest="source",
        metavar="<source>",
        help="Replaces current source with <source>",
    )

    edit_parser.set_defaults(func=edit)

    magnet_parser = subparsers.add_parser(
        "m",
        help="""
        Create magnet url from an existing Bittorrent meta file.
        """,
        aliases=["magnet"],
        prefix_chars="-",
        formatter_class=TorrentFileHelpFormatter,
    )

    magnet_parser.add_argument(
        "metafile",
        action="store",
        help="Path to Bittorrent meta file.",
        metavar="<*.torrent>",
    )

    magnet_parser.set_defaults(func=magnet)

    check_parser = subparsers.add_parser(
        "r",
        help="""
        Calculate amount of torrent meta file's content is found on disk.
        """,
        aliases=["recheck", "check"],
        prefix_chars="-",
        formatter_class=TorrentFileHelpFormatter,
    )

    check_parser.add_argument(
        "metafile",
        action="store",
        metavar="<*.torrent>",
        help="path to .torrent file.",
    )

    check_parser.add_argument(
        "content",
        action="store",
        metavar="<content>",
        help="path to content file or directory",
    )

    check_parser.set_defaults(func=recheck)

    info_parser = subparsers.add_parser(
        "i",
        help="""
        Show detailed information about a torrent file.
        """,
        aliases=["info"],
        prefix_chars="-",
        formatter_class=TorrentFileHelpFormatter,
    )

    info_parser.add_argument(
        "metafile",
        action="store",
        metavar="<*.torrent>",
        help="path to pre-existing torrent file.",
    )

    info_parser.set_defaults(func=info)

    args = parser.parse_args(args)

    if args.debug:
        activate_logger()

    if args.interactive:
        return select_action()

    return args.func(args)


main_script = execute


def main():
    """
    Initiate main function for CLI script.
    """
    execute()
