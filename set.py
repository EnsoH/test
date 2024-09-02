import time

# following = ["alex", "did", "fakaer", "alex", "clown"]
# filter_foll = sorted(list(set(following)))

# print(following)
# print(filter_foll)


def list_speed():
    start_time = time.time()
    following = [
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
    ]
    for i in following:
        pass

    end_time = time.time()
    exc_time = end_time - start_time
    print(f"время выполнение --  {exc_time}")


def set_speed():
    start_time = time.time()
    following_set = {
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
        "alex",
        "did",
        "fakaer",
        "alex",
        "clown",
    }
    for i in following_set:
        pass

    end_time = time.time()
    exc_time = end_time - start_time
    print(f"время выполнение --  {exc_time}")


list_speed()
# set_speed()
