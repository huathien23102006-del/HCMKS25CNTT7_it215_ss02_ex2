"""
    Phần 1: Phân tích lỗi

    1. Endpoint hiện tại trong source code là gì?

    Endpoint hiện tại là:

    GET /student

    Vì trong code có:

    @app.get("/student")
    def get_student():

    2. Vì sao gọi GET /students bị lỗi 404 Not Found?

    Vì trong FastAPI chưa khai báo route /students.

    Hiện tại chỉ có:

    @app.get("/student")

    nên khi gọi:

    GET /students

    FastAPI không tìm thấy đường dẫn tương ứng và trả về lỗi:

    404 Not Found

    3. Vì sao tên endpoint /student chưa phù hợp với yêu cầu lấy danh sách sinh viên?

    Vì /student là dạng số ít, thường dùng để lấy một sinh viên.

    Ví dụ:

    GET /student/1

    có thể hiểu là lấy sinh viên có id = 1.

    Trong khi yêu cầu là lấy toàn bộ danh sách nên phải dùng dạng số nhiều:

    GET /students

    4. Vì sao dòng return students[0] chưa đúng với yêu cầu nghiệp vụ?

    Vì:

    students[0]

    chỉ lấy phần tử đầu tiên trong danh sách.

    Kết quả chỉ trả về:

    {
        "id": 1,
        "name": "An"
    }

    Trong khi yêu cầu là trả về toàn bộ danh sách sinh viên.

    Cần trả về:

    return students

    5. API đúng theo yêu cầu khách hàng nên có đường dẫn là gì?

    API đúng là:

    GET /students
"""

from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]


@app.get("/students")
def get_students():
    return students