import os
from api import get_data_api
from hdfs import send_data_hdfs

if __name__ == "__main__":
    try:
        os.mkdir(data)
    except:
        pass

    get_data_api()
    send_data_hdfs()
