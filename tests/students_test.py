# def test_get_assignments_student_1(client, h_student_1):
#     response = client.get(
#         '/student/assignments',
#         headers=h_student_1
#     )

#     assert response.status_code == 200

#     data = response.json['data']
#     for assignment in data:
#         assert assignment['student_id'] == 1


# def test_get_assignments_student_2(client, h_student_2):
#     response = client.get(
#         '/student/assignments',
#         headers=h_student_2
#     )

#     assert response.status_code == 200

#     data = response.json['data']
#     for assignment in data:
#         assert assignment['student_id'] == 2


# def test_post_assignment_null_content(client, h_student_1):
#     """
#     failure case: content cannot be null
#     """

#     response = client.post(
#         '/student/assignments',
#         headers=h_student_1,
#         json={
#             'content': None
#         })

#     assert response.status_code == 400


# def test_post_assignment_student_1(client, h_student_1):
#     content = 'ABCD TESTPOST'

#     response = client.post(
#         '/student/assignments',
#         headers=h_student_1,
#         json={
#             'content': content
#         })

#     assert response.status_code == 200

#     data = response.json['data']
#     assert data['content'] == content
#     assert data['state'] == 'DRAFT'
#     assert data['teacher_id'] is None


# def test_submit_assignment_student_1(client, h_student_1):
#     response = client.post(
#         '/student/assignments/submit',
#         headers=h_student_1,
#         json={
#             'id': 2,
#             'teacher_id': 2
#         })

#     assert response.status_code == 200

#     data = response.json['data']
#     assert data['student_id'] == 1
#     assert data['state'] == 'SUBMITTED'
#     assert data['teacher_id'] == 2


# def test_assignment_resubmit_error(client, h_student_1):
#     response = client.post(
#         '/student/assignments/submit',
#         headers=h_student_1,
#         json={
#             'id': 2,
#             'teacher_id': 2
#         })
#     error_response = response.json
#     assert response.status_code == 400
#     assert error_response['error'] == 'FyleError'
#     assert error_response["message"] == 'only a draft assignment can be submitted'

# def test_submit_assignment_without_teacher(client, h_student_1):
#     response = client.post(
#         '/student/assignments/submit',
#         headers=h_student_1,
#         json={
#             "id": 2  # Assuming this is a valid draft assignment
#         }
#     )
#     assert response.status_code == 400
#     data = response.json
#     assert data['error'] == 'ValidationError'
#     assert 'teacher_id' in data['message']

# def test_access_student_assignments_without_principal_header(client):
#     response = client.get('/student/assignments')
#     assert response.status_code == 401
#     data = response.json
#     assert data['error'] == 'FyleError'
#     assert data['message'] == 'principal not found'


def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )
    assert response.status_code == 200
    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1

def test_get_assignments_student_2(client, h_student_2):
    response = client.get(
        '/student/assignments',
        headers=h_student_2
    )
    assert response.status_code == 200
    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 2

def test_post_assignment_null_content(client, h_student_1):
    """
    Failure case: Content cannot be null.
    """
    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': None
        })
    assert response.status_code == 400
    data = response.json
    assert data['error'] == 'ValidationError'

def test_post_assignment_student_1(client, h_student_1):
    content = 'ABCD TESTPOST'
    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })
    assert response.status_code == 200
    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None

def test_submit_assignment_student_1(client, h_student_1):
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })
    assert response.status_code == 200
    data = response.json['data']
    assert data['student_id'] == 1
    assert data['state'] == 'SUBMITTED'
    assert data['teacher_id'] == 2

def test_assignment_resubmit_error(client, h_student_1):
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })
    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'only a draft assignment can be submitted'

def test_submit_assignment_without_teacher(client, h_student_1):
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            "id": 2  # Assuming this is a valid draft assignment
        }
    )
    assert response.status_code == 400
    data = response.json
    assert data['error'] == 'ValidationError'
    assert 'teacher_id' in data['message']

def test_access_student_assignments_without_principal_header(client):
    response = client.get('/student/assignments')
    assert response.status_code == 401
    data = response.json
    assert data['error'] == 'FyleError'
    assert data['message'] == 'principal not found'