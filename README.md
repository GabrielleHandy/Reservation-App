>>> Hey! Welcome to Melon Reservations! <<<

I used sql/psql for my database.
python anf flask on the backend and javascript on the front


A challenge I came across was learning how to manipulate and  compare time. I used the python datetime module to format and do time comparisons. 

If I had more time I would have styled more, and added testing. I also wanted to add a way to remove and edit reservations. 








___________Install Instructions____________

1.clone repository


2. activate virtual env
>>> source evn/bin/activate

3. install requirements
>>> pip3 install -r requirements.txt

4.create a database named melon-reservations
>>> createdb melon-reservations

5.seed your database with the provided sql
>>> psql melon-reservations < melon-reservations.sql

6. You're all set! Run server.py
>>> python3 server.py