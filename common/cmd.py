import os
from common.error import CustomError

def cmd(commond):
    return os.popen(commond)



if __name__ == "__main__":

    ret =cmd("tasklist")
    data = ret.read()
    if "hawkeye" not in data:
        raise CustomError("小助手未启动")