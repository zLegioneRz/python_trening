
def test_test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_cont()
    app.session.logout()