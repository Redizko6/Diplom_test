import sender_requests

def positive_assert():
    kit_responce = sender_requests.get_new_order()
    assert kit_responce.status_code == 200

def test_check_new_order():
    positive_assert()