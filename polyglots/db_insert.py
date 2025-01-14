import mysql.connector
from mysql.connector import Error

# MySQL 데이터베이스 연결 정보
DB_CONFIG = {
    "host": "localhost",  # 또는 서버 주소
    "user": "your_username",
    "password": "your_password",
    "database": "your_database"
}

# 데이터 삽입 함수 (write)
def write(user_email, word_mean, word_explain, word_example):
    try:
        # DB 연결
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # User 테이블에 데이터 삽입
        user_query = "INSERT INTO user (user_email, created_at) VALUES (%s, NOW())"
        cursor.execute(user_query, (user_email,))
        user_id = cursor.lastrowid  # 삽입된 User의 ID 가져오기

        # Word_Review 테이블에 데이터 삽입
        review_query = """
        INSERT INTO word_review (user_id, word_mean, word_explain, word_example, created_at, updated_at)
        VALUES (%s, %s, %s, %s, NOW(), NOW())
        """
        cursor.execute(review_query, (user_id, word_mean, word_explain, word_example))

        # 트랜잭션 커밋
        connection.commit()
        print("Data inserted successfully!")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# 데이터 읽기 함수 (read)
def read():
    try:
        # DB 연결
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # JOIN을 사용하여 두 테이블의 데이터 읽기
        query = """
        SELECT u.user_id, u.user_email, w.word_mean, w.word_explain, w.word_example, w.created_at
        FROM user u
        JOIN word_review w ON u.user_id = w.user_id
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        # 결과 출력
        for row in rows:
            print(f"User ID: {row[0]}, Email: {row[1]}, Word: {row[2]}, Explanation: {row[3]}, Example: {row[4]}, Created At: {row[5]}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# 테스트 실행
if __name__ == "__main__":
    # INSERT 테스트
    write(
        user_email="test@example.com",
        word_mean="Example Word",
        word_explain="This is the explanation of the word.",
        word_example="This is an example sentence using the word."
    )

    # SELECT 테스트
    read()
