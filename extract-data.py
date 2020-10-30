from sqlalchemy import create_engine

db_string = "postgres://localhost/amontourdeprogrammer"

print('extraire des données')

db = create_engine(db_string)

result_set = db.execute("select topics.title, posts.raw from topics inner join posts on posts.topic_id = topics.id;")

print("<h1>Archives « À mon tour de programmer »</h1>")

print("<em>à partir de backup du discourse</em>")

print("<dl>")
for r in result_set:
    print("<dt>", r[0], "</dt>")
    print("<dd>", r[1], "</dd>")
print("<dl>")

