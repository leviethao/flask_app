Project được custom từ flask-skeleton
yêu cầu các modules:
    - flask
    - flask-skeleton
Lệnh generate skeleton: create-flask-app [Options] APPNAME

Cấu trúc lại thư mục theo ý muốn, trong đó:

/app/controllers/HomeController.py
-> Định nghĩa các hàm xử lý cho routes

/app/routes.py
-> Định nghĩa các routes

./__init__.py
-> Định nghĩa phương thức create_app

./manage.py
-> file thực thi chính



Run app: Mở cmd, cd vào thư mục gốc của project và chạy lệnh python ./manage.py

Các link test và output tương ứng:

http://localhost:5000
-> Hello, this is Home page


http://localhost:5000/user/hao/22/2.97
-> name: hao, age: 22, score: 2.97

http://localhost:5000/admin
-> hello admin

http://localhost:5000/person/admin
-> hello admin

http://localhost:5000/user/leviethao/10/9.5
-> name: leviethao, age: 10, score: 9.5

http://localhost:5000/add?a=5&b=10
-> 5 + 10 = 15


======== Link tham khảo ============
https://github.com/sheetalkumar105/flaskmvc
https://github.com/enwawerueli/flask-skeleton
https://www.tutorialspoint.com/flask/