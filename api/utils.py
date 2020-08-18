import os
import logging


def get_base_dir():
    # the base dir is "../.."
    return os.path.dirname(os.path.dirname(__file__))


class FeedRecommendLogging:
    def __init__(self, logger_name=__name__, logger_level=logging.INFO, logger_file="log/k8s_learn.log"):
        # Create a logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)

        self.log_path = os.path.join(get_base_dir(), logger_file)

        # Create a FileHandler to write log into file
        fh = logging.FileHandler(self.log_path, 'a', encoding='utf-8')
        fh.setLevel(logger_level)

        # Create a StreamHandler to write log into cmd
        ch = logging.StreamHandler()
        ch.setLevel(logger_level)

        # define log format
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add hadlers to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLogger(self):
        return self.logger


logger = FeedRecommendLogging().getLogger()

if __name__ == '__main__':
    t_l = FeedRecommendLogging().getLogger()


    def demo_logger():
        t_l.info("info test")
        t_l.warning("warning test")
        t_l.error("error test")


    demo_logger()
