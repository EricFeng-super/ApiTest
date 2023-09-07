import pytest


# 单参数单次循环
@pytest.mark.parametrize('name', ['诺维茨基'])
def test_nbaplayer01(name):
    print('我是' + name)
    # assert name == 'AK47'


# 多参数单次循环
@pytest.mark.parametrize('name', ['garnett', '诺维茨基', 'AK47', '孙悟空'])
def test_nbaplayer02(name):
    print('我是' + name)
    # assert name == 'AK47'


# 多参数多次循环
@pytest.mark.parametrize('name,word', [('garnett', 'everything is nothing'), ('诺维茨基', '金鸡独立'), ('AK47', '打的你满地找牙'),
                                       ('孙悟空', '我会72变')])
def test_nbaplayer02(name, word):
    print(f'{name} 我的台词是:{word}')
    # assert name == 'AK47'
