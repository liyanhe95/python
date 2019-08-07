import pytest
#pytest 既可以通过命令行，也可以通过脚本来实现
if __name__ == '__main__':
    pytest.main(['-m smoke'])

#   pytest -m smoke
#   pytest -m login
