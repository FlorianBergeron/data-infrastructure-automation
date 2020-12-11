import os

def send_data_hdfs():
    filename = "top_hit.parquet"
    path_file = "./data/"
    folder_name = "top_hits" 

    create_folder = "hdfs dfs -mkdir " + folder_name
    export_dataset = "hdfs dfs -put " + path_file + filename + " " + folder_name

    os.system(create_folder)
    print(" (+) Create folder \'" + folder_name + "\' in HDFS.")

    os.system(export_dataset)
    print("\n (+) \'" + filename + "\' has been exported to folder\'" + folder_name + "\' in HDFS.")
