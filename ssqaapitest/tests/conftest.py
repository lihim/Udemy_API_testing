# import logging
# from pprint import pformat
# import pytest
#
# # Configure the logger
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
# logger = logging.getLogger('MyLogger')
#
# @pytest.fixture(scope='session', autouse=True)
# def configure_logging():
#     # This fixture configures logging to use pretty printing
#     handler = logging.StreamHandler()
#     handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
#     logger.addHandler(handler)
#     logger.setLevel(logging.DEBUG)
#
# def pytest_runtest_logreport(report):
#     if report.when == 'call' and report.failed:
#         # Example of logging a complex data structure when a test fails
#         complex_data = {
#             'key1': 'value1',
#             'key2': [1, 2, 3],
#             'key3': {'nested_key1': 'nested_value1', 'nested_key2': [4, 5, 6]}
#         }
#         logger.info('Complex data structure:\n%s', pformat(complex_data))
