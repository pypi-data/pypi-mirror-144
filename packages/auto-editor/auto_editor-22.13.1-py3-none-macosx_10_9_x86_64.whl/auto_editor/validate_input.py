import os
import re
import sys
from typing import List, Optional

from auto_editor.utils.progressbar import ProgressBar
from auto_editor.utils.log import Log
from auto_editor.ffwrapper import FFmpeg


class MyLogger:
    @staticmethod
    def debug(msg):
        pass

    @staticmethod
    def warning(msg):
        print(msg, file=sys.stderr)

    @staticmethod
    def error(msg):
        if "'Connection refused'" in msg:
            pass
        else:
            print(msg, file=sys.stderr)


def parse_bytes(bytestr) -> Optional[int]:
    # Parse a string indicating a byte quantity into an integer.
    matchobj = re.match(r'(?i)^(\d+(?:\.\d+)?)([kMGTPEZY]?)$', bytestr)
    if matchobj is None:
        return None
    number = float(matchobj.group(1))
    multiplier = 1024.0 ** 'bkmgtpezy'.index(matchobj.group(2).lower())
    return round(number * multiplier)


def download_video(my_input: str, args, ffmpeg: FFmpeg, log: Log) -> str:
    log.conwrite('Downloading video...')
    if ' @' in my_input:
        max_height = my_input[my_input.index(' @') + 2 :].strip()
        download_format = f'bestvideo[ext=mp4][height<={max_height}]+bestaudio[ext=m4a]'

        my_input = my_input[: my_input.index(' ')]
    else:
        download_format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'

    outtmpl = re.sub(r'\W+', '-', os.path.splitext(my_input)[0]) + '.mp4'

    if args.download_dir is not None:
        outtmpl = os.path.join(args.download_dir, outtmpl)

    try:
        import yt_dlp
    except ImportError:
        log.import_error('yt-dlp')

    if not os.path.isfile(outtmpl):
        ytbar = ProgressBar(args.progress)
        ytbar.start(100, 'Downloading')

        def my_hook(d: dict) -> None:
            if d['status'] == 'downloading':
                ytbar.tick(float(d['_percent_str'].replace('%', '')))

        def abspath(path: Optional[str]) -> Optional[str]:
            if path is None:
                return None
            return os.path.abspath(path)

        ydl_opts = {
            'outtmpl': outtmpl,
            'ffmpeg_location': ffmpeg.path,
            'format': download_format,
            'ratelimit': parse_bytes(args.limit_rate),
            'logger': MyLogger(),
            'cookiefile': abspath(args.cookies),
            'download_archive': abspath(args.download_archive),
            'progress_hooks': [my_hook],
        }

        for item, key in ydl_opts.items():
            if item is None:
                del ydl_opts[key]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([my_input])
        except yt_dlp.utils.DownloadError as error:
            if 'format is not available' in str(error):
                del ydl_opts['format']
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([my_input])
            else:
                log.error('yt-dlp: Download Error.')

        log.conwrite('')
    return outtmpl


def valid_input(inputs: List[str], ffmpeg: FFmpeg, args, log: Log) -> List[str]:
    new_inputs = []

    for my_input in inputs:
        if os.path.isfile(my_input):
            _, ext = os.path.splitext(my_input)
            if ext == '':
                log.error('File must have an extension.')
            new_inputs.append(my_input)

        elif my_input.startswith('http://') or my_input.startswith('https://'):
            new_inputs.append(download_video(my_input, args, ffmpeg, log))
        else:
            if os.path.isdir(my_input):
                log.error('Input must be a file or a URL.')
            log.error(f'Could not find file: {my_input}')

    return new_inputs
