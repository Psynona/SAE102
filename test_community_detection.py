def create_network_test():
    assert create_network(["Alice","Bobby","Alice","Charles"]) == {"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}
    assert create_network(["Anna","Eric","Marc","Axel","Eric","Marc","Anna","Marc"]) == {"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}
    assert create_network(["Alice","Bobby","Dominique","Charles"]) == {"Alice": ["Bobby"], "Bobby":["Alice"], "Dominique":["Charles"], "Charles":["Dominique"]}

create_network_test()


def get_people_test():
    assert get_people({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}) == ["Alice","Bobby","Charles"]
    assert get_people({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}) == ["Anna","Eric","Marc","Axel"]
    assert get_people({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]}) == ["Alice","Bobby","Charles","Dominique"]
    print("test ok")

get_people_test() 


def are_friends_test():
    assert are_friends({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}, "Alice", "Charles") == True
    assert are_friends({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}, "Marc", "Anna") == True
    assert are_friends({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]}, "Bobby", "Dominique") == False
    print("test ok")

are_friends_test() 


def all_his_friends_test():
    assert all_his_friends({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}, "Alice", ["Charles","Bobby"]) == True
    assert all_his_friends({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}, "Eric", ["Anna","Marc"]) == True
    assert all_his_friends({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]},"Bobby",["Dominique","Alice"]) == False
    print("test ok")

all_his_friends_test() 


def is_a_community_test():
    assert is_a_community({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}, ["Charles","Alice","Bobby"]) == False
    assert is_a_community({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}, ["Anna","Marc","Eric"]) == True
    assert is_a_community({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]}, ["Bobby","Dominique","Alice"]) == False
    print("test ok")

is_a_community_test() 
