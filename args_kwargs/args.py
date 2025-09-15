def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


if __name__ == '__main__':
    test_var_args('yasoob', 'python', 'eggs', 'test')
