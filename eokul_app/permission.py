def is_student_login(req, std_no) -> bool:
    return 'student' in req.session and req.session["student"].__contains__(std_no)

def is_admin_login(req, username) -> bool:
    return 'admin' in req.session and req.session["admin"].__contains__(username)