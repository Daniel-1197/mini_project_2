import time

import pytest
from Pages.existuser_page import ExistingUserPage

def test_existuser(login):
    driver = login
    exist_user_page = ExistingUserPage(driver)

    try:
        exist_user_page.navigate_to_admin_menu()
        exist_user_page.wait_for_system_users_page()
        exist_user_page.search_user("New_user")

        assert exist_user_page.verify_user_in_list("New_user"), "User 'TestUser04' not found in the search results."
        print("New user 'New_user' successfully found in the user list.")
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")









