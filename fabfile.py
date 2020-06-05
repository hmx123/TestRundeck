import fabric

def update_project():
    conn = fabric.Connection('myaliyun' , user = 'root', connect_kwargs={"password": "forever1`"})
    conn.put('./', '/home/')
