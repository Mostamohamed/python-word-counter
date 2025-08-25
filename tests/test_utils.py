from utils import count_words

def test_count_words(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("hello world")
    assert count_words(str(file)) == 2
