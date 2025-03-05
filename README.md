คำสั่ง Build docker docker build -t dsproj:1.0.0 .

คำสั่ง run docker docker run --name dsproj -p 9999:9999 dsproj:1.0.0

คำสั่งเพิ่มรายวิชาใน python manage.py shell

from demo.models import Course Course.objects.create(course_code="CS103", course_name="Algorithms", credits=3) print(Course.objects.all())

python manage.py makemigrations python manage.py migrate

สร้าง venv ด้วยคำสั่ง python -m venv test
ใช้งาน venv ด้วยคำสั่ง .\test\Scripts\activate 
