import hw3_1

def test_print_hello(capsys):
    hw3_1.print_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"*10, "Failed to print Hello 10 times"
    
# To run this test, you need to type into the terminal: pytest hw3_1_test.py
