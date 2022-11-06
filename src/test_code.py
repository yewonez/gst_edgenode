from RequestAPI.requestAPI import *
from StreamAPI.rtsp_server import *
from dotenv import load_dotenv

def print_api_list():
  print("############## Edge Client -> Cloud Server ##############")
  print("Function List")
  print("1. set_register_edge_addr")
  print("2. post edge event to cloud server")
  print("3. open rtsp server")
  print("4. stop rtsp server")


if __name__ == "__main__":
    test123=None
    print_api_list()
    while True:
        user_input = int(
            input(
                "Select an API to call (1 to 4). You can press 0 to see the API List: "
            ))

        if user_input == 1:
            print("####set edge address to cloud server####")
            ret = set_register_edge_addr("test","http://127.0.0.1:1234/")
            print(ret)
            print("########################################")

        if user_input == 2:
            load_dotenv()
            print("####post edge event to cloud server####")
            ret = alert_event(0, "rtsp://admin:mdcl7726@192.168.2.4:554/Streaming/Channels/101/")
            print(ret)
            print("########################################")

        if user_input == 3:
            print("####open rtsp server####")
            test_port = "3002"
            test_rtspsrc = "rtsp://admin:mdcl7726@192.168.2.4:554/Streaming/Channels/101/"

            test123 = GstServer(test_port, test_rtspsrc)
            test123.start()
            print("#########################")

        if user_input == 4:
            print("####stop rtsp server####")
            test123.terminate_thread()
            test123.join()
            print("#########################")

        if user_input == 0:
            break
