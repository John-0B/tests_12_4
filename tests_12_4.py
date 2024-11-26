import logging
import new_runner as runner
import unittest


class RunnerTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s / %(levelname)s / %(message)s')

    def test_walk(self):
        try:
            a_walker = runner.Runner('Mathew', -10)
            a_walker.walk()
            logging.info('test_walk выполнен успешно')
        except ValueError as val:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            a_runner = runner.Runner(1, 10)
            a_runner.run()
            logging.info('test_run выполнен успешно')
        except TypeError as typ:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)




