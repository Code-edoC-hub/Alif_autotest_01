import allure


def alu_message(response):
    req = response.request

    info_req = f"""
    Method: {req.method}\n\n
    URL: {req.url}\n\n
    Headers: {req.headers}\n\n
    Body: {req.body}\n\n
    """
    info_res=f"""
    Status: {response.status_code}\n\n
    Headers: {response.headers}\n\n
    Body: {response.text}\n\n
    """
    allure.attach(info_req, "Request", allure.attachment_type.TEXT)
    allure.attach(info_res, "Response", allure.attachment_type.TEXT)

def alu_assert(response):
    with allure.step("status code 200?"):
        assert response.status_code == 200, f"Not OK, but = {response.status_code}"

    with allure.step("Response not empty?"):
        data = response.json()
        assert len(data) > 0, "Response is empty"



