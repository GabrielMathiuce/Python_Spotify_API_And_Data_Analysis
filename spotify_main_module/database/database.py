import getpass
import oracledb
from ..user import models


def main():
    print(models.UserModel.objects.raw("SELECT * FROM "))
    print(models.UserModel.objects)


if __name__ == '__main__':
    main()
