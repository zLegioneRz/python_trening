

def test_test_delete_first_group(app):
    app.group.delete_first_group()
    app.session.logout()
