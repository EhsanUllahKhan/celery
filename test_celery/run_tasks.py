from .tasks import add
import time
if __name__ == '__main__':
    result = add.delay(2,2)
    print(f'Task result: {result.result}')