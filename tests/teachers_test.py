# def test_get_assignments_teacher_1(client, h_teacher_1):
#     response = client.get(
#         '/teacher/assignments',
#         headers=h_teacher_1
#     )

#     assert response.status_code == 200

#     data = response.json['data']
#     for assignment in data:
#         assert assignment['teacher_id'] == 1


# def test_get_assignments_teacher_2(client, h_teacher_2):
#     response = client.get(
#         '/teacher/assignments',
#         headers=h_teacher_2
#     )

#     assert response.status_code == 200

#     data = response.json['data']
#     for assignment in data:
#         assert assignment['teacher_id'] == 2
#         assert assignment['state'] in ['SUBMITTED', 'GRADED']


# def test_grade_assignment_cross(client, h_teacher_2):
#     """
#     failure case: assignment 1 was submitted to teacher 1 and not teacher 2
#     """
#     response = client.post(
#         '/teacher/assignments/grade',
#         headers=h_teacher_2,
#         json={
#             "id": 1,
#             "grade": "A"
#         }
#     )

#     assert response.status_code == 400
#     data = response.json

#     assert data['error'] == 'FyleError'


# def test_grade_assignment_bad_grade(client, h_teacher_1):
#     """
#     failure case: API should allow only grades available in enum
#     """
#     response = client.post(
#         '/teacher/assignments/grade',
#         headers=h_teacher_1,
#         json={
#             "id": 1,
#             "grade": "AB"
#         }
#     )

#     assert response.status_code == 400
#     data = response.json

#     assert data['error'] == 'ValidationError'


# def test_grade_assignment_bad_assignment(client, h_teacher_1):
#     """
#     failure case: If an assignment does not exists check and throw 404
#     """
#     response = client.post(
#         '/teacher/assignments/grade',
#         headers=h_teacher_1,
#         json={
#             "id": 100000,
#             "grade": "A"
#         }
#     )

#     assert response.status_code == 404
#     data = response.json

#     assert data['error'] == 'FyleError'


# def test_grade_assignment_draft_assignment(client, h_teacher_1):
#     """
#     failure case: only a submitted assignment can be graded
#     """
#     response = client.post(
#         '/teacher/assignments/grade',
#         headers=h_teacher_1
#         , json={
#             "id": 2,
#             "grade": "A"
#         }
#     )

#     assert response.status_code == 400
#     data = response.json

#     assert data['error'] == 'FyleError'

# def test_grade_assignment(client, h_teacher_1):
#     response = client.post(
#         '/teacher/assignments/grade',
#         headers=h_teacher_1,
#         json={
#             "id": 1,
#             "grade": "A"
#         }
#     )
#     assert response.status_code == 200
#     data = response.json['data']
#     assert data['state'] == 'GRADED'
#     assert data['grade'] == 'A'

# def test_grade_already_graded_assignment(client, h_teacher_1):
#     """
#     failure case: Cannot grade an already graded assignment
#     """
#     response = client.post(
#         '/teacher/assignments/grade',
#         headers=h_teacher_1,
#         json={
#             "id": 1,  # Assuming this assignment is already graded
#             "grade": "B"
#         }
#     )
#     assert response.status_code == 400
#     data = response.json
#     assert data['error'] == 'FyleError'
#     assert data['message'] == 'only a submitted assignment can be graded'

# def test_grade_assignment_with_invalid_grade(client, h_teacher_1):
#     """
#     failure case: API should allow only grades available in enum
#     """
#     response = client.post(
#         '/teacher/assignments/grade',
#         headers=h_teacher_1,
#         json={
#             "id": 1,
#             "grade": "AB"  # Invalid grade
#         }
#     )
#     assert response.status_code == 400
#     data = response.json
#     assert data['error'] == 'ValidationError'

# def test_access_teacher_assignments_without_principal_header(client):
#     response = client.get('/teacher/assignments')
#     assert response.status_code == 401
#     data = response.json
#     assert data['error'] == 'FyleError'
#     assert data['message'] == 'principal not found'
from core.models.assignments import AssignmentStateEnum, GradeEnum

def test_get_assignments_teacher_1(client, h_teacher_1):
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_1
    )
    assert response.status_code == 200
    data = response.json['data']
    for assignment in data:
        assert assignment['teacher_id'] == 1

def test_get_assignments_teacher_2(client, h_teacher_2):
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_2
    )
    assert response.status_code == 200
    data = response.json['data']
    for assignment in data:
        assert assignment['teacher_id'] == 2
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED.value, AssignmentStateEnum.GRADED.value]

def test_grade_assignment_cross(client, h_teacher_2):
    """
    Failure case: Assignment 1 was submitted to teacher 1 and not teacher 2.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            "id": 1,
            "grade": "A"
        }
    )
    assert response.status_code == 400
    data = response.json
    assert data['error'] == 'FyleError'
    assert data['message'] == 'This assignment belongs to some other teacher'

def test_grade_assignment_bad_grade(client, h_teacher_1):
    """
    Failure case: API should allow only grades available in enum.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,
            "grade": "AB"
        }
    )
    assert response.status_code == 400
    data = response.json
    assert data['error'] == 'ValidationError'

def test_grade_assignment_bad_assignment(client, h_teacher_1):
    """
    Failure case: If an assignment does not exist, check and throw 404.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 100000,
            "grade": "A"
        }
    )
    assert response.status_code == 404
    data = response.json
    assert data['error'] == 'FyleError'

def test_grade_assignment_draft_assignment(client, h_teacher_1):
    """
    Failure case: Only a submitted assignment can be graded.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 2,
            "grade": "A"
        }
    )
    assert response.status_code == 400
    data = response.json
    assert data['error'] == 'FyleError'
    assert data['message'] == 'only a submitted assignment can be graded'

def test_grade_assignment(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,
            "grade": "A"
        }
    )
    assert response.status_code == 200
    data = response.json['data']
    assert data['state'] == 'GRADED'
    assert data['grade'] == 'A'

def test_grade_already_graded_assignment(client, h_teacher_1):
    """
    Failure case: Cannot grade an already graded assignment.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,  # Assuming this assignment is already graded
            "grade": "B"
        }
    )
    assert response.status_code == 400
    data = response.json
    assert data['error'] == 'FyleError'
    assert data['message'] == 'only a submitted assignment can be graded'

def test_grade_assignment_with_invalid_grade(client, h_teacher_1):
    """
    Failure case: API should allow only grades available in enum.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,
            "grade": "AB"  # Invalid grade
        }
    )
    assert response.status_code == 400
    data = response.json
    assert data['error'] == 'ValidationError'

def test_access_teacher_assignments_without_principal_header(client):
    response = client.get('/teacher/assignments')
    assert response.status_code == 401
    data = response.json
    assert data['error'] == 'FyleError'
    assert data['message'] == 'principal not found'