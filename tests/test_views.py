def test_blog_posts(posts):
    try:
        from blogicum.blog import posts as solution_posts
    except Exception as e:
        raise AssertionError(
            'При импорте списка `posts` из файла `blog/views.py` '
            f'произошла ошибка: {e}') from e
    assert solution_posts == posts, (
        'Убедитесь, что список с постами `posts` из файла `blog/views.py` '
        'соответствуют списку из задания.')
