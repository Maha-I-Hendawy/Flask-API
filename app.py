from flask import Flask, request, jsonify



app = Flask(__name__)



API_KEY = '98e2a2efe7eee11a855e37655abd'


def check_key():
	key = request.headers.get('x-api-key')
	if key != API_KEY:
		return jsonify({"message": "unauthorized"}, 403)





users = [{"id": 1, "name": "Kiki"}, {"id": 2, "name": "Jiji"}, {"id": 3, "name": "Jojo"}]

# get a list of all users


@app.route('/api/users', methods=['GET'])
def get_users():
	auth = check_key()
	if auth:
		return auth

	return jsonify({'users': users})

	
# add a new user


@app.route('/api/users', methods=['POST'])
def add_user():
	auth = check_key()
	if auth:
		return auth
	else:
		if request.method == 'POST':
			data = request.get_json()
			user = {"id": data['id'], "name": data['name']}
			users.append(user)
			return jsonify({"users": users})
		else:
			return "No user added"



# get one user

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	auth = check_key()
	if auth:
		return auth
	else:
		user = [user for user in users if user['id'] == user_id]
		return jsonify({"user": user})


# update one user

@app.route('/api/users/<int:user_id>/update', methods=['PUT'])
def update_user(user_id):
	auth = check_key()
	if auth:
		return auth
	else:

		if request.method == 'PUT':
			user = [user for user in users if user['id'] == user_id]
			data = request.get_json()
			user[0]['name'] = data['name']
			return jsonify({'users': users})

		return "No user updated"


# delete one user

@app.route('/api/users/<int:user_id>/delete', methods=['DELETE'])
def delete_user(user_id):
	auth = check_key()
	if auth:
		return auth
	else:

		if request.method == 'DELETE':
			user = [user for user in users if user['id'] == user_id]
			users.remove(user[0])
			return jsonify({'users': users})

		return "No user deleted"





posts = [{"id": 1, "title": "first post", "content": "first content", "user_id": 1}, 
{"id": 2, "title": " second post", "content": "second contenrt", "user_id": 1}, 
{"id": 3, "title": "third post", "content": "third contenrt", "user_id": 1}, 
{"id": 4, "title": "new post", "content": "new content", "user_id": 2}, 
{"id": 7, "title": " new post", "content": "new contenrt", "user_id": 2}, 
{"id": 8, "title": "new post", "content": "new contenrt", "user_id": 2}, 
{"id": 9, "title": "new post", "content": "new content", "user_id": 3}, 
{"id": 10, "title": "new post", "content": "new contenrt", "user_id": 3}, 
{"id": 12, "title": "new post", "content": "new contenrt", "user_id": 3}]


# get all posts 

@app.route('/api/posts', methods=['GET'])
def get_posts():
	auth = check_key()
	if auth:
		return auth
	else:
		return jsonify({"posts": posts})


# get all posts by a users

@app.route('/api/users/<int:user_id>/posts', methods=['GET'])
def get_posts_by_user(user_id):
	auth = check_key()
	if auth:
		return auth
	else:

		postsByuser = [post for post in posts if post["user_id"] == user_id]
		return jsonify({"posts": postsByuser})


# get post by id

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
	auth = check_key()
	if auth:
		return auth
	else:

		post = [post for post in posts if post['id'] == post_id]
		return jsonify({'post': post[0]})

# create one post

@app.route('/api/users/<int:user_id>/posts', methods=['POST'])
def add_post(user_id):
	auth = check_key()
	if auth:
		return auth
	else:

		if request.method == 'POST':
			user = [user for user in users if user["id"] == user_id]
			data = request.get_json()
			post = {"id": data['id'], "title": data['title'], "content": data['content'], "user_id": user[0]['id']}
			posts.append(post)
			return jsonify({"posts": posts})
		return "No posts added"


# get one post by a user

@app.route('/api/users/<int:user_id>/posts/<int:post_id>', methods=['GET'])
def get_post_by_user(user_id, post_id):
	auth = check_key()
	if auth:
		return auth
	else:

		user = [user for user in users if user["id"] == user_id]
		post = [post for post in posts if post['user_id'] == user[0]['id'] and post['id'] == post_id]
		return jsonify({"post": post})



# update a post by a user

@app.route('/api/users/<int:user_id>/posts/<int:post_id>/update', methods=['PUT'])
def update_post_by_user(user_id, post_id):
	auth = check_key()
	if auth:
		return auth
	else:

		if request.method == 'PUT':
			user = [user for user in users if user["id"] == user_id]
			post = [post for post in posts if post['user_id'] == user[0]['id'] and post['id'] == post_id]
			data = request.get_json()
			post[0]['title'] = data['title']
			post[0]['content'] = data['content']
			return jsonify({"post": post})
		return "No posts updated"




# delete a post by a user

@app.route('/api/users/<int:user_id>/posts/<int:post_id>/delete', methods=['DELETE'])
def delete_post_by_user(user_id, post_id):
	auth = check_key()
	if auth:
		return auth
	else:

		if request.method == 'DELETE':
			user = [user for user in users if user["id"] == user_id]
			post = [post for post in posts if post['user_id'] == user[0]['id'] and post['id'] == post_id]

			return jsonify({"posts": posts})
		else:
			"No posts deleted"
		



comments = [{'id': 1, 'comment': "comment 1", "user_id": 1, "post_id": 1}, {'id': 2, 'comment': "comment 2", "user_id": 1, "post_id": 2}, {'id': 3, 'comment': "comment 3", "user_id": 1, "post_id": 2}]


# get all comments on a post 

@app.route('/api/posts/<int:post_id>/comments', methods=['GET'])
def get_comments_on_post(post_id):
	auth = check_key()
	if auth:
		return auth
	else:
		
		post = [post for post in posts if post['id'] == post_id]
		comment = [comment for comment in comments if comment['post_id'] == post[0]['id']]
		return jsonify({"comments": comment})




