if __name__ == "__main__":
    import os
    import threading

    def ping(host):
        print("... pinging ", host)
        ping_out = os.popen("ping " + host, "r")
        while True:
            line = ping_out.readline()
            if not line:
                break
            print(line)

    ips = list(map(str, input().split()))

    threads = [threading.Thread(target=ping, args=(ip,)) for ip in ips]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
