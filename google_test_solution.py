import logging
import sys

"""
    Author: Sangeeta Gupta
    Date : 7th September 2019
    Objective : find minimum number of rows created
"""
def solution(A: []) -> int:
    """Your solution goes here."""

    student_rows = {A[0]:[]}
    for item in A[1:]:
        for count in list(student_rows.keys()):
            if item < count:
                student_rows.get(count).append(item)
            else:
                student_rows[item] = []

    return len(student_rows.keys())


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    A = [int(x) for x in input[0].split(",")]
    sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
    logging.basicConfig(filename='logger.txt', level=logging.DEBUG,
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    # log user login
    logging.info('root logged in')
    try:
        main()
    except KeyError:
        print('Key couldn\'t be found!')
        logging.info('Exception occurred', exc_info=True)

    except TypeError:
        print('Expected input as a line separated by commas')
        logging.info('Exception occurred', exc_info=True)

    except Exception as e:
        print(e)
        logging.info('Exception occurred', exc_info=True)

    finally:
        # log user log out
        logging.info('root logged out.')
