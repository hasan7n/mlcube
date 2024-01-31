# Code adapted from
# https://github.com/mlcommons/medperf/blob/8b98dd89fdd56777dce650a4d8c29565c660f108/cli/medperf/logging/filters/redacting_filter.py
import logging


class NewlineFilter(logging.Filter):
    def filter(self, record):
        record.msg = self.remove_newlines(record.msg)
        if isinstance(record.args, dict):
            for k in record.args.keys():
                record.args[k] = self.remove_newlines(record.args[k])
        else:
            record.args = tuple(self.remove_newlines(arg) for arg in record.args)
        return True

    def remove_newlines(self, msg):
        if isinstance(msg, str):
            return msg.replace("\n", "\\n")
        return msg


def setup_file_logger(name):
    logger = logging.getLogger(name)
    logger.addFilter(NewlineFilter())
    return logger
