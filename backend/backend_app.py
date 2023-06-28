from flask import Flask, jsonify, request
from flask_cors import CORS
import file_handler

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = file_handler.load_file('posts.json')


def id_generator():
    if POSTS:
        last_id = POSTS[-1]['id']
    else:
        last_id = 0
    new_id = last_id + 1
    return new_id


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


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
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


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    for post in POSTS:
        if post['id'] == post_id:
            new_title = request.json.get('title', post['title'])
            new_content = request.json.get('content', post['content'])

            post['title'] = new_title
            post['content'] = new_content

            file_handler.save_file('posts.json', POSTS)

            updated_post = {
                "id": post_id,
                "title": new_title,
                "content": new_content
            }
            return jsonify(updated_post), 200

    return jsonify({"error": "Post not found"}), 404


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title = request.args.get('title')
    content = request.args.get('content')

    if not title and not content:
        return jsonify([])

    matching_posts = []
    for post in POSTS:
        if title and title.lower() in post['title'].lower():
            matching_posts.append(post)
        elif content and content.lower() in post['content'].lower():
            matching_posts.append(post)

    return jsonify(matching_posts)


@app.route('/api/posts', methods=['GET'])  # NOT WORKING
def sort_posts():
    sort_by = request.args.get('sort')
    direction = request.args.get('dir')

    valid_sort_fields = ['title', 'content']
    valid_sort_directions = ['asc', 'desc']

    if sort_by and direction:
        if sort_by not in valid_sort_fields or direction not in valid_sort_directions:
            return jsonify({"error": "Invalid sort field or direction"}), 400

        elif direction and direction.lower() == 'desc':
            sorted_posts = sorted(POSTS, key=lambda x: x[sort_by], reverse=True)
            return jsonify(sorted_posts)

        elif direction and direction.lower() == 'asc':
            sorted_posts = sorted(POSTS, key=lambda x: x[sort_by], reverse=False)
            return jsonify(sorted_posts)

    else:
        return jsonify(POSTS)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
