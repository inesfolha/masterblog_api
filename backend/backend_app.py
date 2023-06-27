from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import file_handler

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = file_handler.load_file('posts.json')


def id_generator():
    """Generates a unique ID using UUID."""
    return str(uuid.uuid4())


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_posts():
    title = request.json.get('title')
    content = request.json.get('content')

    post_id = id_generator()
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    add_post = {'id': post_id, "title": title, "content": content}

    POSTS.append(add_post)
    file_handler.save_file('posts.json', POSTS)

    return jsonify(add_post), 201


@app.route('/api/posts/<string:post_id>', methods=['DELETE'])
def delete(post_id):
    post_to_delete = None
    for post in POSTS:
        if post['id'] == post_id:
            post_to_delete = post
            break

    if post_to_delete:
        POSTS.remove(post_to_delete)
        file_handler.save_file('posts.json', POSTS)
        return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200

    return jsonify({"error": "Post not found"}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
