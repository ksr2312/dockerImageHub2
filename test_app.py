from app import app

def test_home():
    response=app.test_client().get("/") ## checking home page response

    assert response.status_code==200 ## 200--> sucessful request
    assert response.data== b"Hello World!" ## checking if getting Hello World! in output