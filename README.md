คำสั่ง Build docker docker build -t dsproj:1.0.0 .

คำสั่ง run docker docker run --name dsproj -p 9999:9999 dsproj:1.0.0

คำสั่งเพิ่มรายวิชาใน python manage.py shell

from demo.models import Course Course.objects.create(course_code="CS103", course_name="Algorithms", credits=3) print(Course.objects.all())

python manage.py makemigrations python manage.py migrate

สร้าง venv ด้วยคำสั่ง python -m venv test
ใช้งาน venv ด้วยคำสั่ง .\test\Scripts\activate 

หน้าเว็บแสดงรายการรายวิชาในหลักสูตร
หน้าเว็บค้นหารายวิชาในหลักสูตรจากรหัสวิชา
หน้าเว็บค้นหารายวิชาในหลักสูตรจากชื่อวิชา
หน้าเว็บแก้ไขข้อมูลรายวิชาจากรหัสวิชา
หน้าเว็บลบรายวิชาจากรหัสวิชาที่กรอก

1.เข้าสู่ระบบ github
gh auth login 

2.สร้าง repoitory ใหม่ สร้างใน github เลย

3. โคลนไฟล์มา gh repo clone 
gh repo clone Supakorn4623/course-management
แล้วเข้าไปในโฟลเดอร์ที่เราโคลนมา 

4. สร้าง venv ด้วยคำสั่ง 
python -m venv  test

ใช้งาน venv ด้วยคำสั่ง
.\test\Scripts\activate


5.สร้าง project django 
django-admin startproject course

6.commit push
git add .
git commit -m ‘พิมพ์สื่งที่ทำ’
git push origin main 

7.สร้าง branch ในหน้า github 
สร้างเสร็จให้พิมพ์คำสั่งใน terminal
git checkout -b test
แล้วไปกดปุ่มใน vscode Publish Branch

8. สร้าง app django
python manage.py startapp test 
อย่าลืม INSTALLED_APPS ใน setting ด้วย

9. แก้ไข urls.py
path(‘ชื่อฟังก์ชั่น’,include(ชื่อฟังก์ชั่น.urls’))
อย่าลืมสร้างไฟล์ urls ใน app 

