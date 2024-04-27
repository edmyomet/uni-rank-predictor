from __format import FormatModule


if __name__ == '__main__':
    module = FormatModule()
    module.main()
    module.merge()
    print(module.df)
    