import logging


class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename="D:\\Projects\\nopcommerceApp\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levename)s: %(message)s',
        #                     force=True
        #                     )
        logging.basicConfig(filename='D:\\Projects\\totalfit_web\\logs\\ramexample.log',
                            level=logging.DEBUG, force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
