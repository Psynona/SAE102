from community_detection import *

def test_create_network():
    assert create_network(["Alice","Bobby","Alice","Charles"]) == {"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}
    assert create_network(["Anna","Eric","Marc","Axel","Eric","Marc","Anna","Marc"]) == {"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}
    assert create_network(["Alice","Bobby","Dominique","Charles"]) == {"Alice": ["Bobby"], "Bobby":["Alice"], "Dominique":["Charles"], "Charles":["Dominique"]}
    print("Test de la fonction create_network : ok")

def test_get_people():
    assert get_people({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}) == ["Alice","Bobby","Charles"]
    assert get_people({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}) == ["Anna","Eric","Marc","Axel"]
    assert get_people({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]}) == ["Alice","Bobby","Charles","Dominique"]
    print("Test de la fonction get_people : ok")

def test_are_friends():
    assert are_friends({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}, "Alice", "Charles") == True
    assert are_friends({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}, "Marc", "Anna") == True
    assert are_friends({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]}, "Bobby", "Dominique") == False
    print("Test de la fonction are_friends : ok")


def test_all_his_friends():
    assert all_his_friends({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}, "Alice", ["Charles","Bobby"]) == True
    assert all_his_friends({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}, "Eric", ["Anna","Marc"]) == True
    assert all_his_friends({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]},"Bobby",["Dominique","Alice"]) == False
    print("Test de la fonction all_his_friends : ok")

def test_is_a_community():
    assert is_a_community({"Alice": ["Bobby","Charles"], "Bobby":["Alice"], "Charles":["Alice"]}, ["Charles","Alice","Bobby"]) == False
    assert is_a_community({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie"], "Charlie" : ["Bob"], "Dominique" : ["Alice"]}, ["Alice", "Bob", "Dominique"]) == False
    assert is_a_community({"Alice": ["Bobby"], "Bobby":["Alice"], "Charles":["Dominique"], "Dominique":["Charles"]}, ["Bobby","Dominique","Alice"]) == False
    print("Test de la fonction is_a_community : ok")

def test_find_community():
    assert find_community({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}, ["Alice", "Bob", "Charlie", "Dominique"]) == ["Alice", "Bob", "Dominique"]
    assert find_community({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}, ["Charlie", "Alice", "Bob", "Dominique"]) == ["Charlie", "Bob"]
    assert find_community({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}, ["Charlie", "Alice", "Dominique"]) == ["Charlie"]
    print("Test de la fonction find_community : ok")


def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}, ["Alice", "Bob", "Charlie"]) == ["Bob", "Alice", "Charlie"]
    assert order_by_decreasing_popularity({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}, ["Axel", "Marc", "Eric"]) == ["Marc", "Eric", "Axel"]
    assert order_by_decreasing_popularity({"Alice": ["Bobby", "Dominique", "Charles"], "Bobby":["Alice"], "Charles":["Dominique", "Alice"],"Dominique":["Charles", "Alice"]}, ["Bobby", "Charles", "Alice"]) == ["Alice", "Charles", "Bobby"]
    print("Test de la fonction order_by_decreasing_popularity : ok")

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}) == ["Bob", "Alice", "Dominique"]
    assert find_community_by_decreasing_popularity({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}) == ["Marc", "Eric", "Anna"]
    assert find_community_by_decreasing_popularity({"Alice": ["Bobby", "Dominique", "Charles"], "Bobby":["Alice"], "Charles":["Dominique", "Alice"],"Dominique":["Charles", "Alice"]}) == ["Alice", "Charles", "Dominique"]
    print("Test de la fonction find_community_by_decreasing_popularity : ok")
    

def test_find_community_from_person():
    assert find_community_from_person({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}, "Alice") == ["Alice", "Bob", "Dominique"]
    assert find_community_from_person({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}, "Charlie") == ["Charlie", "Bob"]
    assert find_community_from_person({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}, "Anna") == ["Anna", "Marc", "Eric"]
    print("Test de la fonction find_community_from_person : ok")


def test_find_max_community():
    assert find_max_community({"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}) == ["Alice", "Bob", "Dominique"]
    assert find_max_community({"Anna":["Eric","Marc"], "Eric":["Anna","Marc"], "Marc":["Axel","Eric","Anna"], "Axel":["Marc"]}) == ["Anna", "Marc", "Eric"]
    assert find_max_community({"Alice": ["Bobby", "Dominique", "Charles"], "Bobby":["Alice"], "Charles":["Dominique", "Alice"],"Dominique":["Charles", "Alice"]}) == ["Alice", "Dominique", "Charles"]
    print("Test de la fonction find_max_community : ok")


