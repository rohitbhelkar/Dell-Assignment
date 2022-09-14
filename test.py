import requests
def test_get_colour():
    resp = requests.get("http://localhost:5000/colour/red")
    code = resp.status_code
    assert code == 200, "Item not found"

def test_post_colour():
    resp = requests.post("http://localhost:5000/colour/red")

    print(resp.content)
    print(code)
    assert code == 201, "Unable to add item"
    ## resp.text
    ## resp.content
    ## resp.json
    ## resp.headers


def test_post_memory():
    resp = requests.post("http://localhost:5000/memory/16")
    code = resp.status_code
    code = resp.status_code
    print(code)
    assert code == 201, "Unable to add item"
def test_get_memory():
    resp = requests.get("http://localhost:5000/memory/16")
    code = resp.status_code
    assert code == 200, "Item not found"

test_post_memory()
test_get_memory()
